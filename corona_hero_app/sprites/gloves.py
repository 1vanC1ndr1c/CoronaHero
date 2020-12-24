import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface
from corona_hero_app.image_handler import split_animated_gif


class Gloves(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_gloves_gif = Image.open(str(os.path.join(self._resources_path, 'Gloves.gif')))
        self.image_gloves_gif = split_animated_gif(self.image_gloves_gif)
        self.image_gloves = self.image_gloves_gif[0]

        self.width = self.image_gloves.get_width()
        self.height = self.image_gloves.get_height()
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

        self._frame_counter = 0

        self.collected = False

    def set_dimensions(self, w, h):
        self.image_gloves = smoothscale(self.image_gloves, (w, h))
        self.image_gloves_gif = [smoothscale(self.image_gloves_gif[i], (w, h)) for i in
                                 range(len(self.image_gloves_gif))]

    def animate(self):
        self.image_gloves = self.image_gloves_gif[self._frame_counter]  # Get the next image.
        self._frame_counter = self._frame_counter + 1
        if self._frame_counter >= len(self.image_gloves_gif):  # Reset after the maximum number of frames.
            self._frame_counter = 0

    def check_if_collected(self, character):
        character_range_x = range(character.x_pos, character.x_pos + character.width)
        character_range_y = range(character.y_pos, character.y_pos + character.height)

        self_range_x = range(self.x_pos, self.x_pos + self.width)
        self_range_y = range(self.y_pos, self.y_pos + self.height)

        if bool(set(character_range_x) & set(self_range_x)) is True:
            if bool(set(character_range_y) & set(self_range_y)):
                self.collected = True
                return True
        return False
