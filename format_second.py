def format_second(seconds: int | float):
    if isinstance(seconds, float):
        seconds = int(seconds)

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return f'{h}:{m}:{s}'
