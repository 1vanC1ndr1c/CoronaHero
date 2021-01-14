import time

import pygame


def start_game(character, platforms, boxes, dis, gloves, inf_per, masks, sinks, walls, viruses, rects):
    shootable_objects = []
    shootable_objects.extend(boxes)
    shootable_objects.extend(inf_per)
    shootable_objects.extend(platforms)
    shootable_objects.extend(viruses)

    spritesGroup = pygame.sprite.Group()

    for box in boxes:
        spritesGroup.add(box)

    for platform in platforms:
        spritesGroup.add(platform)

    window_x_size = 960
    window_y_size = 640
    pygame.init()
    win = pygame.display.set_mode((window_x_size, window_y_size))
    pygame.display.set_caption("Testing environment.")
    pos_change = 5
    run = True
    jump_count = 10
    last_shoot = current_shoot = time.time()
    mask_timer_start = mask_timer_end = -1
    death_timer_end = 0
    glove_counter_start = glove_counter_end = -1

    for rect in rects:
        print(rect)

    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if character.death_countdown is True:
            death_timer_end = time.time()
            if death_timer_end - character.death_timer_start >= 10:
                character.is_dead = True

        if character.is_dead is False:
            if not character.isJump:

                if keys[pygame.K_SPACE] and character.y_pos < window_y_size - character.height:
                    character.jump()
            else:
                check_collide = pygame.sprite.spritecollide(character, spritesGroup, False)
                print(check_collide)
                if len(check_collide) == 0:
                    neg = 1
                    if jump_count < 0:
                        neg = -1

                    character.y_pos -= int((jump_count ** 2) * 0.5 * neg)
                    character.set_rect_y(-int((jump_count ** 2) * 0.5 * neg))
                    print('X: ', character.x_pos)
                    print('Rect X: ', character.rect.x)
                    print('Y: ', character.y_pos)
                    print('Rect Y: ', character.rect.y)
                    jump_count -= 1
                else:
                    print(check_collide[0].rect.y)
                    character.y_pos -= int((jump_count ** 2) * 0.5) - 5
                    character.set_rect_y(-int((jump_count ** 2) * 0.5) - 5)
                    character.isJump = False
                    print('X: ', character.x_pos)
                    print('Rect X: ', character.rect.x)
                    print('Y: ', character.y_pos)
                    print('Rect Y: ', character.rect.y)
                    jump_count = 10

            if keys[pygame.K_LEFT] and character.x_pos > 0:
                character.move_left(-pos_change)
                print('X: ', character.x_pos)
                print('Rect X: ', character.rect.x)
                hit = pygame.sprite.spritecollide(character, spritesGroup, False)
                if len(hit) > 0:
                    character.move_left(pos_change)

            if keys[pygame.K_RIGHT] and character.x_pos < window_x_size - character.width:
                character.move_right(pos_change)
                hit = pygame.sprite.spritecollide(character, spritesGroup, False)
                print('X: ', character.x_pos)
                print('Rect X: ', character.rect.x)
                if len(hit) > 0:
                    character.move_right(-pos_change)

            if pygame.mouse.get_pressed(3)[0] is True:
                current_shoot = time.time()
                if current_shoot - last_shoot > 0.1:
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
            if character.check_if_near_box(box):
                if character.has_gloves is False:
                    character.start_death_countdown()
                box.move(pos_change, character)
                character.is_moving_box = True
            else:
                character.is_moving_box = False

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
        #gloves = [g for g in gloves if g.collected is False]

        for i in inf_per:
            win.blit(i.image_infected_person, (i.x_pos, i.y_pos))

        for mask in masks:
            mask.animate()
            win.blit(mask.image_mask, (mask.x_pos, mask.y_pos))
            if mask.check_if_collected(character) is True:
                character.mask_pick_up()
                mask_timer_start = time.time()
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

        for virus in viruses:
            if virus.dead_animation_done is False:
                character.check_if_hit(virus)
                virus.animate()
                win.blit(virus.image, (virus.x_pos, virus.y_pos))
            else:
                virus.kill()

        pygame.display.update()

    pygame.quit()
