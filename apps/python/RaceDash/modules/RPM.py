import RaceDash.lib.Module

class RPM(RaceDash.lib.Module):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)

    def render(self):
        self.value = self.display.addLabel({
            content: self.data.getRPM()
        })

    def update(self):
        rpm = self.data.RPM()
        maxRpm = self.data.MaxRPM()
        perc = rpm / maxRpm * 100
        options = {}

        options.color = [0.1, 0.1, 0.1, 1]
        
        if perc > 60
            options.color = [0.5, 0.5, 0.5, 1]

        if perc > 90
            options.color = [0.9, 0.9, 0.9, 1]

        self.display.updateLabel(self.value, rpm, options)