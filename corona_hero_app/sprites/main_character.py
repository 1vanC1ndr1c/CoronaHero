import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from image_handler import split_animated_gif
from image_handler import transform_into_surface


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
        self._image_jump = Image.open(str(os.path.join(self._resources_path, 'Hero_Jump.png'))).convert("RGBA")
        self._image_jump = transform_into_surface(self._image_jump)

        # Get the player animation for shooting.
        self._image_shoot = Image.open(str(os.path.join(self._resources_path, 'Hero_Shoot.png'))).convert("RGBA")
        self._image_shoot = transform_into_surface(self._image_shoot)

        # Main image (changes to whatever the main character is currenly doing).
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

    def set_dimensions(self, w, h):
        self.width = w
        self.height = h
        # Set animation dimensions.
        self._images_still = [smoothscale(self._images_still[i], (w, h)) for i in range(len(self._images_still))]
        self._images_move_L = [smoothscale(self._images_move_L[i], (w, h)) for i in range(len(self._images_move_L))]
        self._images_move_R = [smoothscale(self._images_move_R[i], (w, h)) for i in range(len(self._images_move_R))]
        self._image_jump = smoothscale(self._image_jump, (w, h))
        self._image_shoot = smoothscale(self._image_shoot, (w, h))
        self.current_animation = smoothscale(self.current_animation, (w, h))

    def animate_standing_still(self):
        self._image_still = self._images_still[self._still_frame_counter]  # Get the next image.
        self._still_frame_counter = self._still_frame_counter + 1
        if self._still_frame_counter >= len(self._images_still):  # Reset after the maximum number of frames.
            self._still_frame_counter = 0
        self.current_animation = self._image_still  # Set the current animation to standing still.

    def jump(self):

        self.current_animation = self._image_jump
        self.isJump = True

    def shoot(self):
        self.current_animation = self._image_shoot

    def move_left(self):
        self._image_move_L = self._images_move_L[self._move_L_frame_counter]  # Get the next image.
        self._move_L_frame_counter = self._move_L_frame_counter + 1
        if self._move_L_frame_counter >= len(self._images_move_L):  # Reset after the maximum number of frames.
            self._move_L_frame_counter = 0
        self.current_animation = self._image_move_L  # Set the current animation to standing still.

    def move_right(self):
        self._image_move_R = self._images_move_R[self._move_R_frame_counter]  # Get the next image.
        self._move_R_frame_counter = self._move_R_frame_counter + 1
        if self._move_R_frame_counter >= len(self._images_move_R):  # Reset after the maximum number of frames.
            self._move_R_frame_counter = 0
        self.current_animation = self._image_move_R  # Set the current animation to standing still.

    def die(self):
        # TODO
        pass

    def wash_hands(self):
        # TODO
        pass
