import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import split_animated_gif
from corona_hero_app.image_handler import transform_into_surface

from corona_hero_app.sprites.bullet import Bullet


class MainCharacter(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        # Get the player animation for standing still.
        self._gif_still = Image.open(str(os.path.join(self._resources_path, 'Hero_Standing_Still.gif')))
        self._images_still = split_animated_gif(self._gif_still)
        self._image_still = self._images_still[0]

        # Get the player animation for moving left.
        self._gif_move_L = Image.open(str(os.path.join(self._resources_path, 'Hero_Move_Left.gif')))
        self._images_move_L = split_animated_gif(self._gif_move_L)
        self._image_move_L = self._images_move_L[0]

        # Get the player animation for moving right.
        self._gif_move_R = Image.open(str(os.path.join(self._resources_path, 'Hero_Move_Right.gif')))
        self._images_move_R = split_animated_gif(self._gif_move_R)
        self._image_move_R = self._images_move_R[0]

        # Get the player animation for jumping.
        self._image_jump_R = Image.open(str(os.path.join(self._resources_path, 'Hero_Jump_Right.png'))).convert("RGBA")
        self._image_jump_R = transform_into_surface(self._image_jump_R)
        self._image_jump_L = Image.open(str(os.path.join(self._resources_path, 'Hero_Jump_Left.png'))).convert("RGBA")
        self._image_jump_L = transform_into_surface(self._image_jump_L)

        # Get the player animation for shooting.
        self._image_shoot = Image.open(str(os.path.join(self._resources_path, 'Hero_Shoot.png'))).convert("RGBA")
        self._image_shoot = transform_into_surface(self._image_shoot)
        self.bullet_count = 30
        self.bullet_list = []

        # Main image (changes to whatever the main character is currently doing).
        self.current_animation = self._image_still

        # Player dimensions.
        self.width = 50
        self.height = 100
        self.set_dimensions(self.width, self.height)  # Set the dimensions of all the images.

        # Current player position.
        self.x_pos = 0
        self.y_pos = 0

        # Gif frame counters.
        self._still_frame_counter = 0
        self._move_L_frame_counter = 0
        self._move_R_frame_counter = 0

        self.isJump = False
        self.movement_direction = "Left."

    def set_dimensions(self, w, h):
        self.width = w
        self.height = h
        # Set animation dimensions.
        self._images_still = [smoothscale(self._images_still[i], (w, h)) for i in range(len(self._images_still))]
        self._images_move_L = [smoothscale(self._images_move_L[i], (w, h)) for i in range(len(self._images_move_L))]
        self._images_move_R = [smoothscale(self._images_move_R[i], (w, h)) for i in range(len(self._images_move_R))]
        self._image_jump_R = smoothscale(self._image_jump_R, (w, h))
        self._image_jump_L = smoothscale(self._image_jump_L, (w, h))
        self._image_shoot = smoothscale(self._image_shoot, (w, h))
        self.current_animation = smoothscale(self.current_animation, (w, h))

    def animate(self):
        self._image_still = self._images_still[self._still_frame_counter]  # Get the next image.
        self._still_frame_counter = self._still_frame_counter + 1
        if self._still_frame_counter >= len(self._images_still):  # Reset after the maximum number of frames.
            self._still_frame_counter = 0
        self.set_current_animation(self._image_still)  # Set the current animation to standing still.

        # BUllets logic.
        index_done = []
        for index, bullet in enumerate(self.bullet_list):
            bullet.bullet_travel()
            if bullet.x_pos < 0 or bullet.x_pos > 2000:
                index_done.append(index)
        self.bullet_list = [bullet for index, bullet in enumerate(self.bullet_list) if index not in index_done]

    def jump(self):
        if self.movement_direction == "Left.":
            self.current_animation = self._image_jump_L
        else:
            self.current_animation = self._image_jump_R
        self.isJump = True

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_list.append(Bullet(self.movement_direction, self.x_pos, self.y_pos))
            self.set_current_animation(self._image_shoot)
            self.bullet_count = self.bullet_count - 1
        else:
            self.bullet_count = 0

    def bullet_hit(self, bullet_index):
        del self.bullet_list[bullet_index]

    def move_left(self):
        self.movement_direction = "Left."
        self._image_move_L = self._images_move_L[self._move_L_frame_counter]  # Get the next image.
        self._move_L_frame_counter = self._move_L_frame_counter + 1
        if self._move_L_frame_counter >= len(self._images_move_L):  # Reset after the maximum number of frames.
            self._move_L_frame_counter = 0
        self.set_current_animation(self._image_move_L)  # Set the current animation to standing still.

    def move_right(self):
        self.movement_direction = "Right."
        self._image_move_R = self._images_move_R[self._move_R_frame_counter]  # Get the next image.
        self._move_R_frame_counter = self._move_R_frame_counter + 1
        if self._move_R_frame_counter >= len(self._images_move_R):  # Reset after the maximum number of frames.
            self._move_R_frame_counter = 0
        self.set_current_animation(self._image_move_R)  # Set the current animation to standing still.

    def die(self):
        # TODO
        pass

    def wash_hands(self):
        # TODO
        pass

    def set_current_animation(self, current_animation):
        if self.isJump is False:
            self.current_animation = current_animation
        else:
            if self.movement_direction == "Left.":
                self.current_animation = self._image_jump_L
            else:
                self.current_animation = self._image_jump_R
