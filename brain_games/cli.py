import prompt


def welcome_user():
    name = prompt.string('May I have you name? ')
    print(f'Hello, {name}!')
    return name
