import os
from pathlib import Path

import pygame
from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import split_animated_gif
from corona_hero_app.image_handler import transform_into_surface

from corona_hero_app.sprites.bullet import Bullet

import time


class MainCharacter(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        # Get the player animation for standing still.
        self._gif_still = Image.open(str(os.path.join(self._resources_path, 'Hero_Standing_Still.gif')))
        self._images_still = split_animated_gif(self._gif_still)
        self._image_still = self._images_still[0]

        # Get the player animation for standing still while masked.
        self._gif_still_MASK = Image.open(str(os.path.join(self._resources_path, 'Hero_Standing_Still_Mask.gif')))
        self._images_still_MASK = split_animated_gif(self._gif_still_MASK)
        self._image_still_MASK = self._images_still_MASK[0]

        # Get the player animation for moving left.
        self._gif_move_L = Image.open(str(os.path.join(self._resources_path, 'Hero_Move_Left.gif')))
        self._images_move_L = split_animated_gif(self._gif_move_L)
        self._image_move_L = self._images_move_L[0]

        # Get the player animation for moving left while masked.
        self._gif_move_L_MASK = Image.open(str(os.path.join(self._resources_path, 'Hero_Move_Left_Mask.gif')))
        self._images_move_L_MASK = split_animated_gif(self._gif_move_L_MASK)
        self._image_move_L_MASK = self._images_move_L_MASK[0]

        # Get the player animation for moving right.
        self._gif_move_R = Image.open(str(os.path.join(self._resources_path, 'Hero_Move_Right.gif')))
        self._images_move_R = split_animated_gif(self._gif_move_R)
        self._image_move_R = self._images_move_R[0]

        # Get the player animation for moving right while masked.
        self._gif_move_R_MASK = Image.open(str(os.path.join(self._resources_path, 'Hero_Move_Right_Mask.gif')))
        self._images_move_R_MASK = split_animated_gif(self._gif_move_R_MASK)
        self._image_move_R_MASK = self._images_move_R_MASK[0]

        # Get the player animation for jumping.
        self._image_jump_R_gif = Image.open(
            str(os.path.join(self._resources_path, 'Hero_Jump_Right.gif')))
        self._image_jump_R_gif = split_animated_gif(self._image_jump_R_gif)
        self._image_jump_R = self._image_jump_R_gif[0]

        self._image_jump_L_gif = Image.open(
            str(os.path.join(self._resources_path, 'Hero_Jump_Left.gif')))
        self._image_jump_L_gif = split_animated_gif(self._image_jump_L_gif)
        self._image_jump_L = self._image_jump_L_gif[0]

        # Get the player animation for jumping while masked.
        self._image_jump_R_gif_MASK = Image.open(
            str(os.path.join(self._resources_path, 'Hero_Jump_Right_Mask.gif')))
        self._image_jump_R_gif_MASK = split_animated_gif(self._image_jump_R_gif_MASK)
        self._image_jump_R_MASK = self._image_jump_R_gif_MASK[0]

        self._image_jump_L_gif_MASK = Image.open(
            str(os.path.join(self._resources_path, 'Hero_Jump_Left_Mask.gif')))
        self._image_jump_L_gif_MASK = split_animated_gif(self._image_jump_L_gif_MASK)
        self._image_jump_L_MASK = self._image_jump_L_gif_MASK[0]

        # Get the player animation for shooting.
        self._image_shoot_left = Image.open(
            str(os.path.join(self._resources_path, 'Hero_Shoot_Left.png'))).convert("RGBA")
        self._image_shoot_left = transform_into_surface(self._image_shoot_left)

        self._image_shoot_right = Image.open(
            str(os.path.join(self._resources_path, 'Hero_Shoot_Right.png'))).convert("RGBA")
        self._image_shoot_right = transform_into_surface(self._image_shoot_right)

        # Get the player animation for shooting while masked.
        self._image_shoot_left_MASK = Image.open(
            str(os.path.join(self._resources_path, 'Hero_Shoot_Left_Mask.png'))).convert("RGBA")
        self._image_shoot_left_MASK = transform_into_surface(self._image_shoot_left_MASK)

        self._image_shoot_right_MASK = Image.open(
            str(os.path.join(self._resources_path, 'Hero_Shoot_Right_Mask.png'))).convert("RGBA")
        self._image_shoot_right_MASK = transform_into_surface(self._image_shoot_right_MASK)

        self.bullet_count = 0
        self.bullet_list = []

        # Get the dying animation.
        self._gif_die = Image.open(str(os.path.join(self._resources_path, 'Hero_Game_Over.gif')))
        self._gif_die = split_animated_gif(self._gif_die)
        self.image_die = self._gif_die[0]

        # Main image (changes to whatever the main character is currently doing).
        self.current_animation = self._image_still

        # Gif frame counters.
        self._still_frame_counter = 0
        self._move_L_frame_counter = 0
        self._move_R_frame_counter = 0
        self._die_animation_counter = 0
        self._jump_counter = 0

        self.x_movement_direction = "Left."  # Or "Right."
        self.y_movement_direction = "Up."  # Or "Down."
        self.current_movement_direction = "Left."  # "Left.", "Right", "Up.", "Down".

        self.isJump = False
        self.is_dead = False
        self.is_masked = False
        self.has_gloves = False

        self.death_countdown = False
        self.death_counter = 0
        self.death_timer_start = -1

        self.rect = self._image_still.get_rect()

        # Player dimensions.
        self.width = 50
        self.height = 100
        self.set_dimensions(self.width, self.height)  # Set the dimensions of all the images.

        # Collect all the animations.
        self._default_animations = []
        self._default_animations.append(self._images_still)
        self._default_animations.append(self._images_move_L)
        self._default_animations.append(self._images_move_R)
        self._default_animations.append(self._image_jump_R_gif)
        self._default_animations.append(self._image_jump_L_gif)
        self._default_animations.append(self._image_jump_R)
        self._default_animations.append(self._image_jump_L)
        self._default_animations.append(self._image_shoot_left)
        self._default_animations.append(self._image_shoot_right)

        # Current player position.
        self.x_pos = 0
        self.y_pos = 0

    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x
        self.rect.y = y

        print('Character X: ', self.x_pos)
        print('Character Y: ', self.y_pos)
        print('Character rect X: ', self.rect.x)
        print('Character rect Y: ', self.rect.y)

    def set_dimensions(self, w, h):
        self.width = w
        self.height = h
        self.rect.width = w
        self.rect.height = h
        self._images_still = [smoothscale(self._images_still[i], (w, h)) for i in range(len(self._images_still))]
        self._images_move_L = [smoothscale(self._images_move_L[i], (w, h)) for i in range(len(self._images_move_L))]
        self._images_move_R = [smoothscale(self._images_move_R[i], (w, h)) for i in range(len(self._images_move_R))]
        self._image_jump_R_gif = [smoothscale(self._image_jump_R_gif[i], (w, h)) for i in
                                  range(len(self._image_jump_R_gif))]
        self._image_jump_L_gif = [smoothscale(self._image_jump_L_gif[i], (w, h)) for i in
                                  range(len(self._image_jump_L_gif))]
        self._image_jump_R = smoothscale(self._image_jump_R, (w, h))
        self._image_jump_L = smoothscale(self._image_jump_L, (w, h))
        self._image_shoot_left = smoothscale(self._image_shoot_left, (w, h))
        self._image_shoot_right = smoothscale(self._image_shoot_right, (w, h))
        self._images_still_MASK = [smoothscale(self._images_still_MASK[i], (w, h)) for i in
                                   range(len(self._images_still_MASK))]
        self._images_move_L_MASK = [smoothscale(self._images_move_L_MASK[i], (w, h)) for i in
                                    range(len(self._images_move_L_MASK))]
        self._images_move_R_MASK = [smoothscale(self._images_move_R_MASK[i], (w, h)) for i in
                                    range(len(self._images_move_R_MASK))]
        self._image_jump_R_gif_MASK = [smoothscale(self._image_jump_R_gif_MASK[i], (w, h)) for i in
                                       range(len(self._image_jump_R_gif_MASK))]
        self._image_jump_L_gif_MASK = [smoothscale(self._image_jump_L_gif_MASK[i], (w, h)) for i in
                                       range(len(self._image_jump_L_gif_MASK))]
        self._image_jump_R_MASK = smoothscale(self._image_jump_R_MASK, (w, h))
        self._image_jump_L_MASK = smoothscale(self._image_jump_L_MASK, (w, h))
        self._image_shoot_left_MASK = smoothscale(self._image_shoot_left_MASK, (w, h))
        self._image_shoot_right_MASK = smoothscale(self._image_shoot_right_MASK, (w, h))
        self.current_animation = smoothscale(self.current_animation, (w, h))
        self._gif_die = [smoothscale(self._gif_die[i], (w, h)) for i in range(len(self._gif_die))]
        self.image_die = smoothscale(self.image_die, (w, h))

    def animate(self):
        if self.is_dead is False:
            self._image_still = self._images_still[self._still_frame_counter]  # Get the next image.
            self._still_frame_counter = self._still_frame_counter + 1
            if self._still_frame_counter >= len(self._images_still):  # Reset after the maximum number of frames.
                self._still_frame_counter = 0
            self.set_current_animation(self._image_still)  # Set the current animation to standing still.

            # Bullets logic.
            index_done = []
            for index, bullet in enumerate(self.bullet_list):
                bullet.bullet_travel()
                if bullet.x_pos < 0 or bullet.x_pos > 2000:
                    index_done.append(index)
                else:
                    bullet.kill()
            self.bullet_list = [bullet for index, bullet in enumerate(self.bullet_list) if index not in index_done]
        else:
            if self._die_animation_counter < len(self._gif_die):  # Reset after the maximum number of frames.
                self.image_die = self._gif_die[self._die_animation_counter]
                self.current_animation = self.image_die
                self._die_animation_counter = self._die_animation_counter + 1

    def bullet_hit(self, bullet_index):
        del self.bullet_list[bullet_index]

    def jump(self):
        if self.x_movement_direction == "Left.":
            self.current_animation = self._image_jump_L
        else:
            self.current_animation = self._image_jump_R
        self.isJump = True

    def shoot(self):

        if self.bullet_count > 0:
            self.bullet_list.append(Bullet(self.current_movement_direction, self.x_pos, self.y_pos))
            if self.current_movement_direction == "Left.":
                self.set_current_animation(self._image_shoot_left)
            else:
                self.set_current_animation(self._image_shoot_right)
            self.bullet_count = self.bullet_count - 1
        else:
            self.bullet_count = 0

    def move_left(self, x_pos_change):
        self.x_pos = self.x_pos + x_pos_change
        self.set_rect_x(x_pos_change)
        self.x_movement_direction = "Left."
        self.current_movement_direction = "Left."

        self._image_move_L = self._images_move_L[self._move_L_frame_counter]  # Get the next image.
        self._move_L_frame_counter = self._move_L_frame_counter + 1
        if self._move_L_frame_counter >= len(self._images_move_L):  # Reset after the maximum number of frames.
            self._move_L_frame_counter = 0
        self.set_current_animation(self._image_move_L)  # Set the current animation to standing still.

    def move_right(self, x_pos_change):
        self.x_pos = self.x_pos + x_pos_change
        self.set_rect_x(x_pos_change)
        self.x_movement_direction = "Right."
        self.current_movement_direction = "Right."

        self._image_move_R = self._images_move_R[self._move_R_frame_counter]  # Get the next image.
        self._move_R_frame_counter = self._move_R_frame_counter + 1
        if self._move_R_frame_counter >= len(self._images_move_R):  # Reset after the maximum number of frames.
            self._move_R_frame_counter = 0
        self.set_current_animation(self._image_move_R)  # Set the current animation to standing still.

    def die(self):
        self.is_dead = True

    def mask_pick_up(self):
        self.is_masked = True
        self.toggle_mask_animations()

    def mask_depleted(self):
        self.is_masked = False
        self.toggle_mask_animations()

    def toggle_mask_animations(self):
        if self.is_masked is True:
            self._images_still = self._images_still_MASK
            self._images_move_L = self._images_move_L_MASK
            self._images_move_R = self._images_move_R_MASK
            self._image_jump_R_gif = self._image_jump_R_gif_MASK
            self._image_jump_L_gif = self._image_jump_L_gif_MASK
            self._image_jump_R = self._image_jump_R_MASK
            self._image_jump_L = self._image_jump_L_MASK
            self._image_shoot_left = self._image_shoot_left_MASK
            self._image_shoot_right = self._image_shoot_right_MASK
        else:
            self._images_still = self._default_animations[0]
            self._images_move_L = self._default_animations[1]
            self._images_move_R = self._default_animations[2]
            self._image_jump_R_gif = self._default_animations[3]
            self._image_jump_L_gif = self._default_animations[4]
            self._image_jump_R = self._default_animations[5]
            self._image_jump_L = self._default_animations[6]
            self._image_shoot_left = self._default_animations[7]
            self._image_shoot_right = self._default_animations[8]

    def wash_hands(self):
        self.death_countdown = False
        self.death_timer_start = -1

    def disinfectant_pick_up(self):
        self.bullet_count = self.bullet_count + 30

    def gloves_pick_up(self):
        self.has_gloves = True

    def set_current_animation(self, current_animation):
        if self.isJump is False:
            self.current_animation = current_animation
        else:
            if self.x_movement_direction == "Left.":
                self.current_animation = self._image_jump_L
                self._image_jump_L = self._image_jump_L_gif[self._jump_counter]
                self._jump_counter = self._jump_counter + 1
                if self._jump_counter >= len(self._image_jump_L_gif):
                    self._jump_counter = 0
            else:
                self.current_animation = self._image_jump_R
                self._image_jump_R = self._image_jump_R_gif[self._jump_counter]
                self._jump_counter = self._jump_counter + 1
                if self._jump_counter >= len(self._image_jump_L_gif):
                    self._jump_counter = 0

    def set_rect_x(self, x_pos_change):
        self.rect = self.rect.move(x_pos_change, 0)

    def set_rect_y(self, y_pos_change):
        self.rect = self.rect.move(0, y_pos_change)

    def start_death_countdown(self):
        if self.death_countdown is False:
            self.death_timer_start = time.time()
            self.death_countdown = True

    def check_if_hit(self, virus):
        if self.death_countdown is False and self.is_masked is False:
            virus_range_x = range(virus.x_pos, virus.x_pos + virus.width)
            virus_range_y = range(virus.y_pos, virus.y_pos + virus.height)

            self_range_x = range(self.x_pos, self.x_pos + self.width)
            self_range_y = range(self.y_pos, self.y_pos + self.height)

            if bool(set(virus_range_x) & set(self_range_x)) is True:
                if bool(set(virus_range_y) & set(self_range_y)):
                    self.death_timer_start = time.time()
                    self.death_countdown = True

    def check_if_collided(self, collided_object):
        collided_object_range_x = range(collided_object.x_pos, collided_object.x_pos + collided_object.width)
        collided_object_range_y = range(collided_object.y_pos, collided_object.y_pos + collided_object.height)

        self_range_x = range(self.x_pos, self.x_pos + self.width)
        self_range_y = range(self.y_pos, self.y_pos + self.height)

        if bool(set(collided_object_range_x) & set(self_range_x)) is True:
            if bool(set(collided_object_range_y) & set(self_range_y)):
                return True
        return False

    def check_if_near_box(self, box):
        box_range_x = range(box.x_pos, box.x_pos + box.width)
        box_range_y = range(box.y_pos, box.y_pos + box.height)

        self_range_x = range(self.x_pos - 5, self.x_pos + self.width + 10)
        self_range_y = range(self.y_pos, self.y_pos + self.height)

        if bool(set(box_range_x) & set(self_range_x)) is True:
            if bool(set(box_range_y) & set(self_range_y)):
                return True
        return False
