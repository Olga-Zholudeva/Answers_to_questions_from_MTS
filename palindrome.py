import re


def is_palindrome(line: str) -> bool:
    line = re.sub(r"\W", "", line.lower())
    return line == "".join(reversed(line))
