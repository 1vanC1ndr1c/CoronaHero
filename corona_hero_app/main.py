import sys

from corona_hero_app.levels.test_level import start_test_level
from corona_hero_app.levels.level_1 import level_1


def main():
    #start_test_level()  # Start the testing environment.
    level_1(False)


if __name__ == '__main__':
    sys.exit(main())
