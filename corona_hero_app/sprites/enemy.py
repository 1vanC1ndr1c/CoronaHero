import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from image_handler import split_animated_gif


class Enemy(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        # Get the virus skin.
        self._gif = Image.open(str(os.path.join(self._resources_path, 'Virus.gif')))
        self._images = split_animated_gif(self._gif)
        self.image = self._images[0]

        # Virus dimensions.
        self.width = 50
        self.height = 50
        self.set_dimensions(self.width, self.height)

        # Current virus position.
        self.x_pos = 0
        self.y_pos = 0

        # Previous virus position (used to determine the rotation direction.)
        self._x_pos_OLD = 0
        self._y_pos_OLD = 0
        self._direction = "Right."  # Flag that indicates the direction.

        # Gif frame counter.
        self._frame_counter = 0

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height
        for index in range(len(self._images)):  # Change the scale dimensions of every frame
            self._images[index] = smoothscale(self._images[index], (width, height))

    def animate(self):
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

        self._x_pos_OLD = self.x_pos  # Record the current position into self._x_pos_OLD.

    def death_animation(self):
        # TODO
        pass
