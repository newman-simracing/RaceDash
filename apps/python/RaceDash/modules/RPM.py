import RaceDash.lib.Module

class RPM(RaceDash.lib.Module):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)
        label = "---- rpm"
        self.display.label(label)

    def update(self):
        label = "{} rpm".format(self.data.getRPM())
        self.display.label(label)
