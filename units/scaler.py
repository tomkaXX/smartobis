def apply_scaler(value: float, scaler: int) -> float:
    return value * (10 ** scaler)


UNIT_MAP = {
    "W": "watt",
    "kWh": "kilowatt_hour",
    "V": "volt",
    "A": "ampere",
    "var": "var",
    "VA": "volt_ampere"
}
