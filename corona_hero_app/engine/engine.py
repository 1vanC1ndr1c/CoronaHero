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

import time

def start_game(character, platforms, boxes, dis, gloves, inf_per, masks, sinks, walls, viruses, rects):
    shootable_objects = []
    shootable_objects.extend(boxes)
    shootable_objects.extend(inf_per)
    shootable_objects.extend(platforms)
    shootable_objects.extend(viruses)

    boxesGroup = pygame.sprite.Group()

    for box in boxes:
        boxesGroup.add(box)

    window_x_size = 960
    window_y_size = 640
    pygame.init()
    win = pygame.display.set_mode((window_x_size, window_y_size))
    pygame.display.set_caption("Testing environment.")
    pos_change = 5
    jump_pos_change = 10
    run = True
    jump_count = 10
    last_shoot = current_shoot = time.time()
    while run:

        pygame.time.delay(50)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if not character.isJump:
            if keys[pygame.K_UP] and character.y_pos > 0:
                character.move_up(-pos_change)
                for rect in rects:
                    if character.collide(rect):
                        character.move_up(pos_change)

            if keys[pygame.K_DOWN] and character.y_pos < window_y_size - character.height:
                character.move_down(pos_change)
                for rect in rects:
                    if character.collide(rect):
                        character.move_down(-pos_change)

            if keys[pygame.K_SPACE] and character.y_pos < window_y_size - character.height:
                character.jump()
                if character.y_pos > 0:
                    character.y_pos -= jump_pos_change
                    character.set_rect_y(-jump_pos_change)
                character.x_pos += pos_change
                character.set_rect_x(pos_change)
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1

                character.y_pos -= int((jump_count ** 2) * 0.5 * neg)
                character.set_rect_y(int((jump_count ** 2) * 0.5 * neg))
                jump_count -= 1
            else:
                character.isJump = False
                jump_count = 10

        if keys[pygame.K_LEFT] and character.x_pos > 0:
            character.move_left(-pos_change)
            for rect in rects:
                if character.collide(rect):
                    character.move_left(pos_change)

        if keys[pygame.K_RIGHT] and character.x_pos < window_x_size - character.width:
            character.move_right(pos_change)
            for rect in rects:
                if character.collide(rect):
                    character.move_right(-pos_change)

        if pygame.mouse.get_pressed(3)[0] is True:
            current_shoot = time.time()
            if current_shoot - last_shoot > 0.3:
                character.shoot()
            last_shoot = current_shoot

        win.fill((0, 0, 0))

        for wall in walls:  # First draw this (background)
            win.blit(wall.image_wall_brighter, (wall.x_pos, wall.y_pos))

        win.blit(character.current_animation, (character.x_pos, character.y_pos))
        character.animate()

        # Bullet collision.
        for index, bullet in enumerate(character.bullet_list):
            bullet_collided = False
            for o in shootable_objects:
                if o.check_if_hit(bullet):
                    character.bullet_hit(index)
                    bullet_collided = True
            if bullet_collided is False:
                win.blit(bullet.image_bullet, (bullet.x_pos, bullet.y_pos))
            else:
                bullet.kill()

        shootable_objects = [s for s in shootable_objects if s.is_dead is False]

        for platform in platforms:
            win.blit(platform.image_grass, (platform.x_pos, platform.y_pos))
        for box in boxes:
            win.blit(box.image_box, box.get_rect())
        for d in dis:
            win.blit(d.image_disinfectant, (d.x_pos, d.y_pos))
        for g in gloves:
            win.blit(g.image_gloves, (g.x_pos, g.y_pos))
        for i in inf_per:
            win.blit(i.image_infected_person, (i.x_pos, i.y_pos))
        for mask in masks:
            win.blit(mask.image_mask_1, (mask.x_pos, mask.y_pos))
        for sink in sinks:
            win.blit(sink.image_sink, (sink.x_pos, sink.y_pos))

        for virus in viruses:
            if virus.dead_animation_done is False:
                virus.animate()
                win.blit(virus.image, (virus.x_pos, virus.y_pos))
            else:
                virus.kill()

        pygame.display.update()

    pygame.quit()
