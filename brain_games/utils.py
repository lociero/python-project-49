import math


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_greatest_common_divisor(num_one: int, num_two: int) -> int:
    min_number = min(num_one, num_two)
    for divisor in range(min_number, 0, -1):
        if num_one % divisor == 0 and num_two % divisor == 0:
            return divisor


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divisor = 2

    while divisor <= math.sqrt(number):
        if number % divisor == 0:
            return False
        divisor += 1

    return True
