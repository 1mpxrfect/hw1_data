import math

def time_difference(hour1, hour2):
    sin1, cos1 = math.sin(2 * math.pi * hour1 / 24), math.cos(2 * math.pi * hour1 / 24)
    sin2, cos2 = math.sin(2 * math.pi * hour2 / 24), math.cos(2 * math.pi * hour2 / 24)
    diff_sin = sin2 - sin1
    diff_cos = cos2 - cos1
    diff = math.sqrt(diff_sin**2 + diff_cos**2)
    angle_diff = math.acos(diff)
    diff_hours = angle_diff * 24 / (2 * math.pi)
    if diff_hours > 12:
        diff_hours = 24 - diff_hours
    return diff_hours
