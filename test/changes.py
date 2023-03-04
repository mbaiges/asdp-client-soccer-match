import sys
sys.path.insert(0, 'src/')
from changes import apply_changes

def test_apply_changes_set():
    err = []

    o = {
        "foo": "bar"
    }

    changes = [
        {
            "ops": {
                "/foo": {
                    "type": "set",
                    "value": "bar2"
                }
            }
        }
    ]

    o = apply_changes(o, changes)

    expected = "bar2"
    got = o["foo"]

    if expected != got:
        err.append(f'expected "{expected}" but got "{got}"')

    return err

def test_apply_changes_set_2():
    err = []

    o = {
        "foo": "bar"
    }

    changes = [
        {
            "ops": {
                "/": {
                    "type": "set",
                    "value": {
                        "foo": "bar2"
                    }
                }
            }
        }
    ]

    o = apply_changes(o, changes)

    expected = "bar2"
    got = o["foo"]

    if expected != got:
        err.append(f'expected "{expected}" but got "{got}"')

    return err

if __name__ == "__main__":
    errors = []

    e = test_apply_changes_set()
    if e:
        errors.append({
            "test": "test_apply_changes_set",
            "errors": e
        })
    e = test_apply_changes_set_2()
    if e:
        errors.append({
            "test": "test_apply_changes_set_2",
            "errors": e
        })

    if errors:
        print("Errors:")
        print(errors)
        exit(1)
    else:
        print("Tests run successfully")
        exit(0)
