import sys
import asyncio
import websockets
import json
from datetime import datetime
import time
import copy

import match

################
## UTILS
################

def usage():
    return f"Usage: {sys.argv[0]} " + "{port} {match_name} {match_duration_seconds}"

def seconds(start, end):
    ss = 0

    _minsec = start.split(":")
    ss -= (int(_minsec[0]) * 60 + int(_minsec[1]))

    _minsec = end.split(":")
    ss += (int(_minsec[0]) * 60 + int(_minsec[1]))

    return ss

################
## STEPS
################

async def hello(ws):
    hello_msg = {
        "type": "hello",
        "username": "anonymous"
    }
    await ws.send(json.dumps(hello_msg))
    ans = await ws.recv()
    ans = json.loads(ans)
    if "errors" in ans or not ans["success"]:
        print("Error: Authorization error")
        exit(1)
    return ans["newUsername"]

async def create_match(ws, match_name):
    create_msg = {
        "type": "create",
        "name": match_name,
        "schema": { # use real schema
            "type": "object"
        },
        "value": match.INITIAL
    }
    await ws.send(json.dumps(create_msg))
    ans = await ws.recv()
    ans = json.loads(ans)
    if "errors" in ans or not ans["created"]:
        print("Error: Authorization error")
        exit(1)
    return ans["created"]

async def publish_match(ws, match_name, match_duration):
    changes = match.CHANGES

    total_seconds = 0
    if changes["FIRST_HALF"]:
        total_seconds += seconds(changes["FIRST_HALF"][0]["time"], changes["FIRST_HALF"][-1]["time"])
    total_seconds += 15 * 60
    if changes["SECOND_HALF"]:
        total_seconds += seconds(changes["SECOND_HALF"][0]["time"], changes["SECOND_HALF"][-1]["time"])

    sratio = 1.0 * match_duration / total_seconds
    now = datetime.now()

    # First half
    print("----- First Half -----")
    changes_list = copy.deepcopy(changes["FIRST_HALF"])
    while changes_list:
        c = changes_list.pop(0)
        update_msg = {
            "type": "update",
            "name": match_name,
            "updates": [
                {
                    "ops": c["ops"]
                }
            ]
        }
        await ws.send(json.dumps(update_msg))
        if changes_list:
            w = seconds(c["time"], changes_list[0]["time"])
            time.sleep(w * sratio)

    # Half time
    print("----- Half Time -----")
    half_time_seconds = 15 * 60
    time.sleep(half_time_seconds * sratio)

    # Second half
    print("----- Second Half -----")
    changes_list = copy.deepcopy(changes["SECOND_HALF"])
    while changes_list:
        c = changes_list.pop(0)
        update_msg = {
            "type": "update",
            "name": match_name,
            "updates": [
                {
                    "ops": c["ops"]
                }
            ]
        }
        await ws.send(json.dumps(update_msg))
        if changes_list:
            w = seconds(c["time"], changes_list[0]["time"])
            time.sleep(w * sratio)

async def start_client(match_name, port, match_duration):
    async with websockets.connect("ws://localhost:" + str(port)) as ws:
        print("Connection successfull")
        username = await hello(ws)
        print(f"Client username: {username}")
        match = await create_match(ws, match_name)
        await publish_match(ws, match_name, match_duration)
        # await websocket.send("Hello world!")
        # await websocket.recv()

################
## MAIN
################

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Error: missing arguments")
        print(usage())
        exit(1)
    
    port       = int(sys.argv[1])
    match_name = sys.argv[2]
    duration   = int(sys.argv[3])

    asyncio.run(start_client(match_name, port, duration))