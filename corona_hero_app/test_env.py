import pygame
from corona_hero_app.sprites.main_character import MainCharacter
from corona_hero_app.sprites.enemy import Enemy


def start_game():
    """
    Testing environment to see if the animations work.
    TODO Replace it with actual movement later on.
    """
    character = MainCharacter()  # Check the main character animation
    # character = Enemy()  # ... or check the virus animation.

    window_x_size = 960
    window_y_size = 640

    pygame.init()

    win = pygame.display.set_mode((window_x_size, window_y_size))

    pygame.display.set_caption("Testing environment.")

    pos_change = 5
    run = True

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

        if keys[pygame.K_UP] and character.y_pos > 0:
            character.y_pos -= pos_change

        if keys[pygame.K_DOWN] and character.y_pos < window_y_size - character.height:
            character.y_pos += pos_change

        win.fill((0, 0, 0))

        # Character
        if keys[pygame.K_SPACE] and character.y_pos < window_y_size - character.height:
            character.jump()
        if keys[pygame.K_F1]:
            character.shoot()

        win.blit(character.current_animation, (character.x_pos, character.y_pos))
        character.animate_standing_still()

        # Virus
        # character.animate()
        # win.blit(character.image, (character.x_pos, character.y_pos))

        pygame.display.update()

    pygame.quit()
