import prompt
import math


def is_even(number: int) -> bool:
    return number % 2 == 0


def run_game(description, generate_data, user_name):
    print(description)
    game_counter = 0
    while game_counter < 3:
        question, answer = generate_data()
        print(f'Question: {question}')
        user_input = prompt.string('Your answer: ')
        if user_input == answer:
            print('Correct!')
            game_counter += 1
        else:
            info_one = f"'{user_input}' is wrong answer ;(."
            info_two = f"Correct answer was '{answer}'."
            print(f'{info_one} {info_two}')
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


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
