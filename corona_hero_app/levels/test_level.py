import pygame
from corona_hero_app.sprites.main_character import MainCharacter
from corona_hero_app.sprites.virus import Virus
from corona_hero_app.sprites.platform import Platform
from corona_hero_app.sprites.box import Box
from corona_hero_app.sprites.disinfectant import Disinfectant
from corona_hero_app.sprites.gloves import Gloves
from corona_hero_app.sprites.mask import Mask
from corona_hero_app.sprites.sink import Sink
from corona_hero_app.sprites.wall import Wall
from corona_hero_app.sprites.virus import Virus
from corona_hero_app.sprites.infected_person import InfectedPerson
from corona_hero_app.engine.engine import start_game


def start_test_level():
    """
    Testing environment to see if the animations work.
    TODO Replace it with actual movement later on.
    """

    shootable_objects = []

    character = MainCharacter()  # Check the main character animation

    virus = Virus()  # ... or check the virus animation.
    virus.x_pos = 500
    virus.y_pos = 500
    virus.get_rect().x = 500
    virus.get_rect().y = 500

    platform1 = Platform()
    platform1.set_dimensions(100, 10)
    platform1.set_position(0, 600)

    platform2 = Platform()
    platform2.set_dimensions(100, 10)
    platform2.set_position(100, 600)

    platform3 = Platform()
    platform3.set_dimensions(100, 10)
    platform3.set_position(200, 600)

    box1 = Box()
    box1.set_position(370, 600)

    dis1 = Disinfectant()
    dis1.y_pos = 570
    dis1.x_pos = 90

    gloves = Gloves()
    gloves.y_pos = 570
    gloves.x_pos = 120

    inf_per = InfectedPerson()
    inf_per.y_pos = 460
    inf_per.x_pos = 170

    mask = Mask()
    mask.y_pos = 570
    mask.x_pos = 230

    sink = Sink()
    sink.y_pos = 570
    sink.x_pos = 260
    sink.get_rect().x = 570
    sink.get_rect().y = 260

    wall1 = Wall()
    wall2 = Wall()
    wall2.x_pos = 300

    start_game(character=character,
               platforms=[platform1, platform2, platform3],
               boxes=[box1],
               dis=[dis1],
               gloves=[gloves],
               inf_per=[inf_per],
               masks=[mask],
               sinks=[sink],
               walls=[wall1],
               viruses=[virus],
               rects=[platform1, platform2, platform3, box1]
               )
