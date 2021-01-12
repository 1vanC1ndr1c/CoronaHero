import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import transform_into_surface
from corona_hero_app.image_handler import split_animated_gif


class Mask(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")

        self._image_mask_1_gif = Image.open(str(os.path.join(self._resources_path, 'Mask.gif')))
        self._image_mask_1_gif = split_animated_gif(self._image_mask_1_gif)

        self._image_mask_2_gif = Image.open(str(os.path.join(self._resources_path, 'Mask-v2.gif')))
        self._image_mask_2_gif = split_animated_gif(self._image_mask_2_gif)

        self._image_mask_3_gif = Image.open(str(os.path.join(self._resources_path, 'Mask-v3.gif')))
        self._image_mask_3_gif = split_animated_gif(self._image_mask_3_gif)

        self.image_mask = self._image_mask_1_gif[0]

        self.width = 30
        self.height = 30
        self.set_dimensions(self.width, self.height)

        self.x_pos = 0
        self.y_pos = 0

        self.collected = False

        self._frame_counter = 0

    def set_dimensions(self, w, h):
        self._image_mask_1_gif = [smoothscale(self._image_mask_1_gif[i], (w, h)) for i in
                                  range(len(self._image_mask_1_gif))]
        self._image_mask_2_gif = [smoothscale(self._image_mask_2_gif[i], (w, h)) for i in
                                  range(len(self._image_mask_2_gif))]
        self._image_mask_3_gif = [smoothscale(self._image_mask_3_gif[i], (w, h)) for i in
                                  range(len(self._image_mask_3_gif))]

    def animate(self):
        self.image_mask = self._image_mask_1_gif[self._frame_counter]  # Get the next image.
        self._frame_counter = self._frame_counter + 1
        if self._frame_counter >= len(self._image_mask_1_gif):  # Reset after the maximum number of frames.
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
