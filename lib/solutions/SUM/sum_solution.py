# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    try:
        sum = x+y
        return sum
    except TypeError:
        print("TypeError: Provide two positive integer")

