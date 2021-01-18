import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import split_animated_gif


class Virus(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        # Get the virus skin.
        self._moving_gif = Image.open(str(os.path.join(self._resources_path, 'Virus.gif')))
        self._images = split_animated_gif(self._moving_gif)
        self.image = self._images[0]

        # Get the virus death animation.
        self._death_animation = Image.open(str(os.path.join(self._resources_path, 'Virus_death.gif')))
        self._death_animation = split_animated_gif(self._death_animation)

        self.rect = self.image.get_rect()

        # Virus dimensions.
        self.width = 50
        self.height = 50
        self.set_dimensions(self.width, self.height)

        # Current virus position.
        self.x_pos = 0
        self.y_pos = 0

        self.rect.x = 0
        self.rect.y = 0
        self.rect.width = 50
        self.rect.height = 50

        # Previous virus position (used to determine the rotation direction.)
        self._x_pos_OLD = 0
        self._y_pos_OLD = 0
        self._direction = "Right."  # Flag that indicates the direction.

        # Gif frame counter.
        self._frame_counter = 0

        self.is_dead = False
        self.dead_animation_done = False

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height
        for index in range(len(self._images)):  # Change the scale dimensions of every frame
            self._images[index] = smoothscale(self._images[index], (width, height))
        for index in range(len(self._death_animation)):  # Change the scale dimensions of every frame
            self._death_animation[index] = smoothscale(self._death_animation[index], (width, height))

    def animate(self):

        if self.is_dead is True:
            self.image = self._death_animation[self._frame_counter]
            self._frame_counter = self._frame_counter + 1
            if self._frame_counter >= len(self._death_animation):
                self._frame_counter = 0
                self.dead_animation_done = True
                self.kill()
        else:
            self.image = self._images[self._frame_counter]  # Get the next image based on the frame counter.
            # Check the new position.
            if self.x_pos > self._x_pos_OLD:  # If it is going right.
                self._frame_counter = self._frame_counter + 1  # Get the next gif frame.
                self._direction = "Right."  # Indicate the rotation direction.
            elif self.x_pos < self._x_pos_OLD:  # If it is going left.
                self._frame_counter = self._frame_counter - 1  # Get the previous frame.
                self._direction = "Left."  # Indicate the rotation direction.

            elif self.x_pos == self._x_pos_OLD:  # If the virus is standing still.
                if self._direction == "Right.":  # If it used to go right before stopping.
                    self._frame_counter = self._frame_counter + 1  # Get the next frame (rotate right).
                elif self._direction == "Left.":  # If it used to go left before stopping.
                    self._frame_counter = self._frame_counter - 1  # Get the previous frame (rotate left).

            # Reset the frame counter after the maximum number or minimum number of frames.
            if self._frame_counter >= len(self._images):
                self._frame_counter = 0
            elif self._frame_counter < 0:
                self._frame_counter = len(self._images) - 1

        self.rect.x = self.x_pos
        self._x_pos_OLD = self.x_pos  # Record the current position into self._x_pos_OLD.

    def check_if_hit(self, bullet):
        bullet_range_x = range(bullet.x_pos, bullet.x_pos + bullet.width)
        bullet_range_y = range(bullet.y_pos, bullet.y_pos + bullet.height)

        self_range_x = range(self.x_pos, self.x_pos + self.width)
        self_range_y = range(self.y_pos, self.y_pos + self.height)

        if bool(set(bullet_range_x) & set(self_range_x)) is True:
            if bool(set(bullet_range_y) & set(self_range_y)):
                self._frame_counter = 0
                self.is_dead = True
                return True
        return False

    def get_rect(self):
        return self.rect

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.x_pos = x
        self.y_pos = y
