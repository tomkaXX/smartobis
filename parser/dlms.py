class DLMSAdapter:

    @staticmethod
    def iec_to_dlms(obis):

        # IEC: A.B.C.D.E
        # DLMS: A-B:C.D.E*F

        return f"{obis.a}-{obis.b}:{obis.c}.{obis.d}.{obis.e}*{obis.f}"

    @staticmethod
    def dlms_to_iec(code: str):

        a, rest = code.split("-")
        b, rest = rest.split(":")
        c, rest = rest.split(".", 1)
        d, rest = rest.split(".")
        e, f = rest.split("*")

        return f"{a}.{b}.{c}.{d}.{e}.{f}"
