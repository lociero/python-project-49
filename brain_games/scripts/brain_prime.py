from brain_games.games.brain_prime import generate_game_data, DESCRIPTION
from brain_games.cli import welcome_user
from brain_games.utils import run_game


def main():
    user_name = welcome_user()
    run_game(DESCRIPTION, generate_game_data, user_name)


if __name__ == '__main__':
    main()
