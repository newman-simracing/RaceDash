from .Data import Data
from .Widget import Widget

class RaceDash:
    modules = []
    intervals = []

    def __init__(self, scale, opacity):
        self.scale = scale | 1
        self.opacity = opacity | 1

        self.update()

    def add(self, module, options, interval):
        options.x = options.x | 0
        options.y = options.y | 0
        options.scale = options.scale | self.scale
        update = update | 0.1

        widget = Widget(options.x, options.y)
        module(widget, Data, options)
        module.render()

        self.modules.push({ interval, module })
        self.intervals = list(map(lambda x: { interval: x.interval, timer: 0 }, self.modules))

    def update(self, deltaT):
        [timer += deltaT for timer in self.timers]

        for i in self.intervals:
            if i.timer > i.interval:
                i.timer = 0
                [module.update() for module in self.modules[i.interval]]
        
    def save(self):
        pass