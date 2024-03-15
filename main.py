import math

def to_polar(r, x, degrees=True):

    mag = math.sqrt(r**2 + x**2)
    angle_rad = math.atan2(x,r)
    angle_degrees = angle_rad * 180 / math.pi
    if degrees == False:
        return mag, angle_rad
    else:
        return mag, angle_degrees

def to_rect(mag, pf):

    angle_deg = math.acos(pf)

    r = mag * (math.cos(angle_deg))
    x = mag * (math.sin(angle_deg))
    return r, x


r = -3
x = -4


polar_result = to_polar(r,x)
print(polar_result)
# rect_result = to_rect(polar_result[0], polar_result[1])
# print(rect_result)

another_test = to_rect(20, 0.75)
print(another_test)











