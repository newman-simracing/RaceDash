import RaceDash.lib.Module

class RPM(RaceDash.lib.Module):
    def __init__(self, data, display, options):
        super().__init__(data, display)

        x = options.x | 0
        y = options.y | 0

        self.display.label("--- rpm", x, y, 14, "left")
