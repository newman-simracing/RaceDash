import RaceDash.lib.Module

class Position(RaceDash.lib.Module):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)
        self.l = self.display.label("Pos: -/-", options.x, options.y, 14, "left")

    def update(self):
        pos = self.data.getPosition()
        ac.setText(self.l, "Pos: {}/{}".format(pos.actual, pos.total)
