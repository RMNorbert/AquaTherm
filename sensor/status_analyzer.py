def analyze_aquarium_status(lower_bound, upper_bound, temp, humidity, distance):
    status = ''
    if humidity < 40.0 or distance > 20:
        status += 'low water level with \n '
    if temp > upper_bound:
        status += 'high temperature'
    elif temp >= upper_bound - 0.5:
        status += 'approaching upper limit temperature'
    elif temp < lower_bound:
        status += 'suboptimal temperature'
    else:
        status += 'normal temperature'

    return status


def get_status(temperature, humidity, aquarium_type, distance):
    if aquarium_type == 'cold':
        return analyze_aquarium_status(15.0, 23.0, temperature, humidity, distance)
    elif aquarium_type == 'tropical':
        return analyze_aquarium_status(23.0, 29.5, temperature, humidity, distance)
    else:
        return analyze_aquarium_status(21.0, 25.5, temperature, humidity, distance)

