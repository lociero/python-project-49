from random import randint
from brain_games.utils import get_greatest_common_divisor

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game_data(get_random_int=randint) -> tuple[str, str]:
    number_one = get_random_int(1, 100)
    number_two = get_random_int(1, 100)

    question = f'{number_one} {number_two}'
    answer = get_greatest_common_divisor(number_one, number_two)

    return question, str(answer)
