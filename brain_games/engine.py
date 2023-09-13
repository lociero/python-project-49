import prompt


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