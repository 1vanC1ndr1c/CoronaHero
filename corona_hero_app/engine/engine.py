import time

import pygame

import numpy as np

from corona_hero_app.sprites.energy_time import EnergyTime
from corona_hero_app.sprites.platform import Platform


def start_game(character, platforms, boxes, dis, gloves, inf_per, masks, sinks, walls, viruses, rects, doors,
               backgrounds):
    energy_time1 = EnergyTime(0, 0)
    energy_time2 = EnergyTime(0, 70)
    r = pygame.sprite.Group(rects)

    shootable_objects = []
    shootable_objects.extend(boxes)
    shootable_objects.extend(platforms)
    shootable_objects.extend(viruses)

    window_x_size = 1280
    window_y_size = 720
    pygame.init()
    win = pygame.display.set_mode((window_x_size, window_y_size))
    pygame.display.set_caption("Testing environment.")
    pos_change = 5
    run = True
    jump_count = 8
    last_shoot = current_shoot = time.time()
    mask_timer_start = mask_timer_end = -1
    energy_time_start_gloves = -1
    energy_time_start_masks = -1
    animate_start_gloves = True
    animate_start_mask = True
    death_timer_end = 0
    glove_counter_start = glove_counter_end = -1
    freefall_count = 1
    falling = False

    while run:

        for bg in backgrounds:
            win.blit(bg.image_cave, (bg.x_pos, bg.y_pos))
        pygame.time.delay(20)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if character.death_countdown is True:
            death_timer_end = time.time()
            if death_timer_end - character.death_timer_start >= 10:
                character.is_dead = True

        if character.is_dead is True:
            return False

        if character.is_dead is False:

            collision = pygame.sprite.spritecollideany(character, r)

            if collision is None or collision.y_pos < character.y_pos or (
                    collision.y_pos - character.y_pos) < character.height:
                character.y_pos += 10
                character.rect.y = character.y_pos
                freefall_count += 1
                falling = True
                if character.y_pos == 3000:
                    character.is_dead = True
            else:
                falling = False
                pass
                # print('Collision: ', collision.y_pos)
                # print('Character: ', character.y_pos)

            if not character.isJump and not falling:
                if keys[pygame.K_SPACE]:
                    character.jump()
            if character.isJump:
                if jump_count >= 0:
                    character.y_pos -= 30
                    character.rect.y = character.y_pos
                    jump_count -= 1
                    
                else:
                    character.isJump = False
                    jump_count = 10

            if keys[pygame.K_LEFT] and character.x_pos > 0:
                character.move_left(-pos_change)

            if keys[pygame.K_RIGHT] and character.x_pos < window_x_size - character.width:
                character.move_right(pos_change)

            if pygame.mouse.get_pressed(3)[0] is True:
                current_shoot = time.time()
                if current_shoot - last_shoot > 0.1:
                    character.shoot()
                last_shoot = current_shoot

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
            if not bullet_collided:
                win.blit(bullet.image_bullet, (bullet.x_pos, bullet.y_pos))
            else:
                bullet.kill()

        shootable_objects = [s for s in shootable_objects if s.is_dead is False]

        for platform in platforms:
            da = False
            if(character.y_pos+character.height - 10 >= platform.y_pos and character.y_pos+character.height - 10 <= platform.y_pos+platform.height):
                if(character.x_pos+character.width >= platform.x_pos and character.x_pos+character.width <= platform.x_pos + platform.width/2):
                    character.x_pos = platform.x_pos - character.width
                    da = True

                elif(character.x_pos <= platform.x_pos+platform.width and character.x_pos >= platform.x_pos + platform.width/2):
                    character.x_pos = platform.x_pos + platform.width
                    da = True

            if(character.isJump and da and (character.y_pos <= platform.y_pos+platform.height+20 and character.y_pos >= platform.y_pos)):
                jump_count = -1

            if(character.isJump and da and (character.y_pos <= platform.y_pos+platform.height+20 and character.y_pos >= platform.y_pos)):
                jump_count = -1

        for platform in platforms:
            win.blit(platform.image_grass, (platform.x_pos, platform.y_pos))

        if character.has_gloves:
            current_time = time.time()
            win.blit(energy_time1.gloves_icon, (energy_time1.x_pos, energy_time1.y_pos))
            win.blit(energy_time1.image_energy_time, (energy_time1.x_pos + 70, energy_time1.y_pos + 20))
            if animate_start_gloves:
                energy_time1.animate_start()
                animate_start_gloves = False
            if (current_time - energy_time_start_gloves) >= 1:
                energy_time_start_gloves = time.time()
                energy_time1.animate()
        else:
            energy_time1._frame_counter = 0
            energy_time1.animate_start()
            animate_start_gloves = True

        if character.is_masked:
            current_time = time.time()
            win.blit(energy_time2.mask_icon, (energy_time2.x_pos, energy_time2.y_pos))
            win.blit(energy_time2.image_energy_time, (energy_time2.x_pos + 70, energy_time2.y_pos + 20))
            if animate_start_mask:
                energy_time2.animate_start()
                animate_start_mask = False
            if (current_time - energy_time_start_masks) >= 1:
                energy_time_start_masks = time.time()
                energy_time2.animate()
        else:
            energy_time2._frame_counter = 0
            energy_time2.animate_start()
            animate_start_mask = True

        character.is_moving_box = False
        for box in boxes:
            win.blit(box.image_box, box.get_rect())
            if character.check_if_near_box(box):
                if character.has_gloves is False:
                    character.start_death_countdown()
                box.move(pos_change, character)
                character.is_moving_box = True

        for d in dis:
            d.animate()
            win.blit(d.image_disinfectant, (d.x_pos, d.y_pos))
            if d.check_if_collected(character) is True:
                character.disinfectant_pick_up()
        dis = [d for d in dis if d.collected is False]

        for g in gloves:
            if character.has_gloves is False:
                g.animate()
                win.blit(g.image_gloves, (g.x_pos, g.y_pos))
                if g.check_if_collected(character) is True:
                    character.gloves_pick_up()
                    glove_counter_start = time.time()
                    energy_time_start_gloves = time.time()
        # gloves = [g for g in gloves if g.collected is False]

        for mask in masks:
            mask.animate()
            win.blit(mask.image_mask, (mask.x_pos, mask.y_pos))
            if mask.check_if_collected(character) is True:
                character.mask_pick_up()
                mask_timer_start = time.time()
                energy_time_start_masks = time.time()
        masks = [m for m in masks if m.collected is False]

        if mask_timer_start != -1:
            mask_timer_end = time.time()
            if mask_timer_end - mask_timer_start > 30:
                mask_timer_end = mask_timer_start = -1
                character.mask_depleted()

        if glove_counter_start != -1:
            glove_counter_end = time.time()
            if glove_counter_end - glove_counter_start > 30:
                glove_counter_end = glove_counter_start = -1
                character.has_gloves = False

        for sink in sinks:
            if character.check_if_collided(sink):
                character.wash_hands()

            win.blit(sink.image_sink, (sink.x_pos, sink.y_pos))

        for door in doors:
            win.blit(door.door_entrance, (door.x_pos, door.y_pos))
            if door.check_if_hit(character) is True:
                pygame.quit()
                return True

        for virus in viruses:
            if virus.dead_animation_done is False:
                character.check_if_hit(virus)
                virus.animate()
                win.blit(virus.image, (virus.x_pos, virus.y_pos))
            else:
                virus.kill()

        pygame.display.update()

    pygame.quit()
