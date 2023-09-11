from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def generate_game_data(get_random_int=randint) -> tuple[str, str]:
    start_number = get_random_int(0, 20)
    step = get_random_int(1, 5)
    progression_length = 10
    index_to_hide = get_random_int(0, progression_length - 1)

    progression = []
    for index in range(0, progression_length):
        number_in_progression = start_number + index * step
        progression.append(str(number_in_progression))

    answer = progression[index_to_hide]
    progression[index_to_hide] = '..'
    question = ' '.join(progression)

    return question, answer
