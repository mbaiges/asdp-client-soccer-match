import jsonpointer as jp

def apply_changes(o, changes):
    for change in changes:
        for path, op in change["ops"].items():
            pointer = jp.JsonPointer(path)
    
            op_type = op["type"]
            known_op = True
            if op_type == "set":
                pointer.set(o, op["value"], inplace=True)
            elif op_type == "unset":
                pointer.set(o, None, inplace=True)
            elif op_type == "numAdd":
                r = jp.resolve_pointer(o, path)
                if r is not None:
                    pointer.set(o, r + op["value"], inplace=True)
            elif op_type == "arrAppend":
                r = jp.resolve_pointer(o, path)
                if r is not None:
                    r.append(op["value"])
                    pointer.set(o, r, inplace=True)
            else:
                known_op = False