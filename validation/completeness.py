def check_missing(values):

    missing = []

    for v in values:
        if v.value is None:
            missing.append(v.obis)

    return missing


def quality_flag(value):

    if value is None:
        return "MISSING"
    if value < 0:
        return "INVALID"
    return "OK"
