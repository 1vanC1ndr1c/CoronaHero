import sys

from corona_hero_app.sprites.main_character import MainCharacter
from corona_hero_app import test_env


def main():
    main_character = MainCharacter()
    test_env.start_game(main_character)


if __name__ == '__main__':
    sys.exit(main())
