import RaceDash.modules.SubLine

class BestTime(RaceDash.modules.SubLine):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)

    def render(self):
        super().render(self.data.getBestTime(), "best:")

    def update(self):
        super().update(self.data.getBestTime())