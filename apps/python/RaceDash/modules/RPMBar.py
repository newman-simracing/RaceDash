import RaceDash.lib.Module

class RPMBar(RaceDash.lib.Module):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)

    def render(self):
        pass

    def update(self):
        rpm = self.data.RPM()
        maxRpm = self.data.MaxRPM()
        perc = rpm / maxRpm * 100
        options = {}

        options.background = "normal"
        
        if perc > 60
            options.background = "yellow"

        if perc > 90
            options.background = "red"

        pass