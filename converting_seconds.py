def converting_seconds(seconds: int) -> str:
    """Функция конвертирует секунды в часы, минуты, секунды."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time = f"{hours} ч. {minutes} мин. {seconds} сек."
    return time
