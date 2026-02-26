def validate_obis(obis):

    for part in (obis.a, obis.b, obis.c, obis.d, obis.e, obis.f):
        if not (0 <= part <= 255):
            return False

    return True
