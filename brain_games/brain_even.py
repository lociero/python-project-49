from random import randint
from brain_games.utils import is_even


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game_data(get_random_int=randint) -> tuple[str, str]:
    random_number = get_random_int(0, 100)
    question = f'Question: {random_number}'
    answer = 'yes' if is_even(random_number) else 'no'
    return question, answer
