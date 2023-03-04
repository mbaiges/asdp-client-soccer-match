import jsonpointer as jp

def apply_changes(o, changes):
    res = o
    
    for change in changes:
        for path, op in change["ops"].items():
            pointer = jp.JsonPointer(path)

            op_type = op["type"]
            known_op = True
            if op_type == "set":
                if "/" == path:
                    res = op["value"]
                else:
                    pointer.set(res, op["value"], inplace=True)
            elif op_type == "unset":
                pointer.set(res, None, inplace=True)
            elif op_type == "numAdd":
                r = jp.resolve_pointer(res, path)
                if r is not None:
                    pointer.set(res, r + op["value"], inplace=True)
            elif op_type == "arrAppend":
                r = jp.resolve_pointer(res, path)
                if r is not None:
                    r.append(op["value"])
                    pointer.set(res, r, inplace=True)
            else:
                known_op = False

    return res