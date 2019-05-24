import RaceDash.lib.Module

class Position(RaceDash.lib.Module):
    def __init__(self, data, display, options):
        super().__init__(data, display)

        x = options.x | 0
        y = options.y | 0

        self.l = self.display.label("Pos: -/-", x, y, 14, "left")

    def update(self):
        pos = self.data.getPosition()
        ac.setText(self.l, "Pos: {}/{}".format(pos.actual, pos.total)
