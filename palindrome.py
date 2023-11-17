import re


def is_palindrome(line: str) -> bool:
    """Функция определяет является ли строка палиндромом."""
    line = re.sub(r"\W", "", line.lower())
    return line == "".join(reversed(line))
