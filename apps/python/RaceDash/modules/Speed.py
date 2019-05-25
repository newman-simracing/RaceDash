import RaceDash.lib.Module

class Speed(RaceDash.lib.Module):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)
        options.unit = options.unit | "kph"

    def render(self):
        self.value = self.display.addLabel({
            content: self.data.getRPM()
        })
        
        self.label = self.display.addLabel({
            content: self.options.unit,
            fontSize: 10,
            y: 10,
            color: [0.2, 0.2, 0.2, 1]
        })

    def update(self):
        self.display.updateLabel(self.value, self.data.getRPM())