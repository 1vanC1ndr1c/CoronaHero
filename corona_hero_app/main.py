import sys

from corona_hero_app.levels.level_1 import level_1
from corona_hero_app.levels.level_2 import level_2
from corona_hero_app.levels.level_3 import level_3
from corona_hero_app.levels.level_4 import level_4
from corona_hero_app.levels.level_5 import level_5
from corona_hero_app.levels.test_level import start_test_level


def main():
    # start_test_level()  # Start the testing environment.

    level_done = False
    while level_done is False:
        level_done = level_1(False)
    level_done = False
    while level_done is False:
        level_done = level_2(False)
    level_done = False
    while level_done is False:
        level_done = level_3(False)
    level_done = False
    while level_done is False:
        level_done = level_4(False)
    level_done = False
    while level_done is False:
        level_done = level_5(False)


if __name__ == '__main__':
    sys.exit(main())
