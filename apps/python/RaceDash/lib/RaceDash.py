from .Data import Data
from .Display import Display

class RaceDash:
    def __init__(self, scale):
        self.scale = scale | 1

    def add(self, module, options):
        options.x = options.x | 0
        options.y = options.y | 0
        options.scale = options.scale | self.scale

        module(Display, Data, options)
