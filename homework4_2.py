def enough(cap, on, wait):
    if cap >= on + wait:
        return False
    else:
        return on + wait - cap