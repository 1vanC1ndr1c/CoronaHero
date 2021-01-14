import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite
from pygame.transform import smoothscale

from corona_hero_app.image_handler import split_animated_gif


class EnergyTime(Sprite):

    def __init__(self, start_pos_x: int, start_pos_y: int):
        Sprite.__init__(self)

        self._frame_counter = 0
        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self._image_energy_time_gif = Image.open(str(os.path.join(self._resources_path, 'Energy-Time-1.gif')))
        self._image_energy_time_gif = split_animated_gif(self._image_energy_time_gif)
        self.image_energy_time = self._image_energy_time_gif[0]

        self.width = 30
        self.height = 30
        self.set_dimensions(self.width, self.height)

        print(len(self._image_energy_time_gif))

        self.x_pos = start_pos_x
        self.y_pos = start_pos_y

    def animate_start(self):
        for i in range(1):
            self.image_energy_time = self._image_energy_time_gif[i]
        self._frame_counter = 2

    def animate(self):
        self.image_energy_time = self._image_energy_time_gif[self._frame_counter]  # Get the next image.
        self._frame_counter = self._frame_counter + 2
        if self._frame_counter >= len(self._image_energy_time_gif):  # Reset after the maximum number of frames.
            self._frame_counter = 0

    def set_dimensions(self, w, h):
        self.image_energy_time = smoothscale(self.image_energy_time, (w, h))

    def get_rect(self):
        return self.rect