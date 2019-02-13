def is_iterable(o):
    try:
        i = iter(o)
    except TypeError:
        return False
    else:
        return True

def flatten(l):
    for elt in l:
        if is_iterable(elt):
            yield from flatten(elt)
        else:
            yield elt

for elt in flatten([1, [2, [3, [[[4]]]]], 5]):
    print(elt)
