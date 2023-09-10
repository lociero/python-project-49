import prompt


def is_even(number: int) -> bool:
    return number % 2 == 0


def run_game(description, generate_data, user_name):
    print(description)
    game_counter = 0
    while game_counter < 3:
        question, answer = generate_data()
        print(question)
        user_input = prompt.string('Your answer: ')
        if user_input == answer:
            print('Correct!')
            game_counter += 1
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
