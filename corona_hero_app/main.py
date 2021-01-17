import sys

from corona_hero_app.levels.level_1 import level_1
from corona_hero_app.levels.level_2 import level_2
from corona_hero_app.levels.level_5 import level_5
from corona_hero_app.levels.test_level import start_test_level

def main():
    # start_test_level()  # Start the testing environment.
    level_2(False)

if __name__ == '__main__':
    sys.exit(main())
