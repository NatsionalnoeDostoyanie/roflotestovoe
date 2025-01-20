import math


def factorial(s: str) -> int:
    if not s:
        return 0

    return math.prod(math.factorial(ord(char)) for char in s)


print(factorial("Z V Z V Z V"))
