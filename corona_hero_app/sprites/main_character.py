import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite

from corona_hero_app.gif_splitter import split_animated_gif


class MainCharacter(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        # Construct the path to the resources.
        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        # Get the player skin.
        self._gif = Image.open(str(os.path.join(self._resources_path, 'Hero-GoodSize-still.gif')))
        # Split the gif into separate images.
        self._images = split_animated_gif(self._gif)
        # Load the first image.
        self.image = self._images[0]

        # Player dimensions.
        self.width = 50
        self.height = 100

        # Current player position.
        self.x_pos = 0
        self.y_pos = 0

        # Gif frame counter.
        self._frame_counter = 0

    def animate(self):
        """
        Animates the player GIF.
        """
        # Get the next image based on the frame counter.
        self.image = self._images[self._frame_counter]
        # Increment the frame counter.
        self._frame_counter = self._frame_counter + 1

        # Reset the frame counter after the maximum number of frames (6).
        if self._frame_counter >= 6:
            self._frame_counter = 0
