import RaceDash.lib.Module

class Position(RaceDash.lib.Module):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)

    def render(self):
        pos = self.data.getPosition()

        self.value = self.display.addLabel({
            content: pos.actual
        })

        self.description = self.display.addLabel({
            content: "pos"
        })

        self.total = self.display.addLabel({
            content: pos.total
        })

    def update(self):
        pos = self.data.getPosition()
        self.display.updateLabel(self.value, pos.actual)
        self.display.updateLabel(self.total, pos.total)