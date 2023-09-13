from brain_games.games.brain_gcd import generate_game_data, GAME_DESCRIPTION
from brain_games.cli import welcome_user
from brain_games.engine import run_game


def main():
    user_name = welcome_user()
    run_game(GAME_DESCRIPTION, generate_game_data, user_name)


if __name__ == '__main__':
    main()
