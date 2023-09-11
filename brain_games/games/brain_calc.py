from random import randint, choice


GAME_DESCRIPTION = 'What is the result of the expression?'


def generate_game_data(get_random_int=randint) -> tuple[str, str]:
    operators = ['+', '-', '*']
    operator = choice(operators)
    number_one = get_random_int(0, 25)
    number_two = get_random_int(0, 25)

    question = f'{number_one} {operator} {number_two}'

    match operator:
        case '+':
            answer = number_one + number_two
        case '-':
            answer = number_one - number_two
        case '*':
            answer = number_one * number_two
        case _:
            answer = ''

    return question, str(answer)
