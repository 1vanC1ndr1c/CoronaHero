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


def start_game():
    """
    Testing environment to see if the animations work.
    TODO Replace it with actual movement later on.
    """

    shootable_objects = []

    character = MainCharacter()  # Check the main character animation
    virus = Virus()  # ... or check the virus animation.

    window_x_size = 960
    window_y_size = 640

    platform1 = Platform()
    platform1.set_dimensions(100, 10)
    platform1.y_pos = 600
    shootable_objects.append(platform1)

    platform2 = Platform()
    platform2.set_dimensions(100, 10)
    platform2.y_pos = 600
    platform2.x_pos = 100
    shootable_objects.append(platform2)

    platform3 = Platform()
    platform3.set_dimensions(100, 10)
    platform3.y_pos = 600
    platform3.x_pos = 200
    shootable_objects.append(platform3)

    box1 = Box()
    box1.y_pos = 370
    box1.x_pos = 600
    shootable_objects.append(box1)

    dis1 = Disinfectant()
    dis1.y_pos = 570
    dis1.x_pos = 90

    gloves = Gloves()
    gloves.y_pos = 570
    gloves.x_pos = 120

    inf_per = InfectedPerson()
    inf_per.y_pos = 460
    inf_per.x_pos = 170
    shootable_objects.append(inf_per)

    mask = Mask()
    mask.y_pos = 570
    mask.x_pos = 230

    sink = Sink()
    sink.y_pos = 570
    sink.x_pos = 260

    wall1 = Wall()
    wall2 = Wall()
    wall2.x_pos = 300

    pygame.init()

    win = pygame.display.set_mode((window_x_size, window_y_size))

    pygame.display.set_caption("Testing environment.")

    pos_change = 5
    jump_pos_change = 10
    run = True
    jump_count = 10

    while run:

        pygame.time.delay(50)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and character.x_pos > 0:
            character.x_pos -= pos_change
            character.move_left()

        if keys[pygame.K_RIGHT] and character.x_pos < window_x_size - character.width:
            character.x_pos += pos_change
            character.move_right()

        if not character.isJump:
            if keys[pygame.K_UP] and character.y_pos > 0:
                character.y_pos -= pos_change

            if keys[pygame.K_DOWN] and character.y_pos < window_y_size - character.height:
                character.y_pos += pos_change

            if keys[pygame.K_SPACE] and character.y_pos < window_y_size - character.height:
                character.jump()
                if character.y_pos > 0:
                    character.y_pos -= jump_pos_change
                character.x_pos += pos_change
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1

                character.y_pos -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                character.isJump = False
                jump_count = 10
        if keys[pygame.K_F1]:  # Nije mi se dalo shvatiti kako staviti shoot na mouse, pa je na F1 :D
            character.shoot()

        win.fill((0, 0, 0))
        win.blit(wall1.image_wall_brighter, (wall1.x_pos, wall1.y_pos))
        win.blit(wall2.image_wall_darker, (wall2.x_pos, wall2.y_pos))

        win.blit(character.current_animation, (character.x_pos, character.y_pos))
        character.animate()

        # Bullet collision.
        for index, bullet in enumerate(character.bullet_list):
            win.blit(bullet.image_bullet, (bullet.x_pos, bullet.y_pos))
            for o in shootable_objects:
                if o.is_hit(bullet):
                    character.bullet_hit(index)

        # Virus follows the main character (for testing purposes).
        virus.x_pos = character.x_pos + 60
        virus.y_pos = character.y_pos
        win.blit(virus.image, (virus.x_pos, virus.y_pos))
        virus.animate()

        win.blit(platform1.image_grass, (platform1.x_pos, platform1.y_pos))
        win.blit(platform2.image_soil, (platform2.x_pos, platform2.y_pos))
        win.blit(platform3.image_concrete, (platform3.x_pos, platform3.y_pos))
        win.blit(box1.image_box, (box1.x_pos, box1.y_pos))
        win.blit(dis1.image_disinfectant, (dis1.x_pos, dis1.y_pos))
        win.blit(gloves.image_gloves, (gloves.x_pos, gloves.y_pos))
        win.blit(inf_per.image_infected_person, (inf_per.x_pos, inf_per.y_pos))
        win.blit(mask.image_mask_1, (mask.x_pos, mask.y_pos))
        win.blit(sink.image_sink, (sink.x_pos, sink.y_pos))
        pygame.display.update()

    pygame.quit()
