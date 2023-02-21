import jsonpointer as jp

def apply_changes(o, changes):
    for change in changes:
        for path, op in change["ops"].items():
            pointer = jp.JsonPointer(path)
    
            op_type = op["type"]
            known_op = True;
            if op_type == "set":
                pointer.set(o, op["value"], inplace=True)
            else:
                known_op = False