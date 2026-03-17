def demo_fct(val: int):
    if val == 5:
        return val
    elif val == -1:
        return 0
    elif val == 1000:
        c = val % 3
        c = (c + 1) // val
        return c
    else:
        return val - 1
