import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite


class Enemy(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_enemy_L = Image.open(str(os.path.join(self._resources_path, 'virus-left.gif')))
        self.image_enemy_R = Image.open(str(os.path.join(self._resources_path, 'virus-right.gif')))
