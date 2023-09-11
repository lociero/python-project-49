from random import randint
from brain_games.utils import is_prime


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_game_data(get_random_int=randint) -> tuple[str, str]:
    number = get_random_int(1, 100)

    question = f'{number}'
    answer = 'yes' if is_prime(number) else 'no'

    return question, str(answer)
