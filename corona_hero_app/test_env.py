import pygame


def start_game(main_character):
    window_x_size = 960
    window_y_size = 640

    pygame.init()

    win = pygame.display.set_mode((window_x_size, window_y_size))

    pygame.display.set_caption("Testing environment.")

    pos_change = 1
    run = True

    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and main_character.x_pos > 0:
            main_character.x_pos -= pos_change

        if keys[pygame.K_RIGHT] and main_character.x_pos < window_x_size - main_character.width:
            main_character.x_pos += pos_change

        if keys[pygame.K_UP] and main_character.y_pos > 0:
            main_character.y_pos -= pos_change

        if keys[pygame.K_DOWN] and main_character.y_pos < window_y_size - main_character.height:
            main_character.y_pos += pos_change

        win.fill((0, 0, 0))

        win.blit(main_character.image, (main_character.x_pos, main_character.y_pos))

        main_character.animate()

        pygame.display.update()

    pygame.quit()
