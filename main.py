import types


def fahrenheit_to_celsjusz(f: float) -> float:
    return round((f - 32) / 1.8, 2)


def celsjusz_to_fahrenheit(c: float) -> float:
    return round((c * 1.8) + 32, 2)


def transform(value: float, base: str, to: str) -> float:
    if base.lower() == 'c' and to.lower() == 'f':
        return celsjusz_to_fahrenheit(value)
    elif base.lower() == 'f' and to.lower() == 'c':
        return fahrenheit_to_celsjusz(value)


def transform_with_format(value: float, base: str, to: str) -> str:
    if base.lower() == 'c' and to.lower() == 'f':
        return format_temp_unit(celsjusz_to_fahrenheit(value), to)
    elif base.lower() == 'f' and to.lower() == 'c':
        return format_temp_unit(celsjusz_to_fahrenheit(value), to)


def format_temp_unit(value: float, unit: str) -> str:
    if unit == 'c':
        return f"{value}℃"
    elif unit == 'f':
        return f"{value}℉"
    else:
        return str(value)


print(transform_with_format(5, 'c', 'f'))
