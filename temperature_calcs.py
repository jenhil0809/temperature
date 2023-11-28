def convert(unit_from, unit_to, val):
    # convert to celcius
    if unit_from == "kelvin":
        val -= 273
    elif unit_from == "farenheit":
        val -= 32
        val *= 5 / 9
    # then do other conversions
    if unit_to == "kelvin":
        val += 273
    elif unit_to == "farenheit":
        val /= 5 / 9
        val += 32
    return val
