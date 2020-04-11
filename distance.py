from math import hypot
def distance(x1, y1, x2, y2):
    result = hypot(x1-x2, y1-y2)
    return round(result,2)