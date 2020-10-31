import os
from pathlib import Path

from PIL import Image
from pygame.sprite import Sprite


class MainCharacter(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self._resources_path = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
        self._resources_path = os.path.join(self._resources_path, "resources", "sprites")
        self.image_main = Image.open(str(os.path.join(self._resources_path, 'Hero-GoodSize-still.gif')))
