import RaceDash.modules.Subline

class LastTime(RaceDash.modules.Subline):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)

    def render(self):
        super().render(self.data.getLastTime(), "last:")

    def update(self):
        super().update(self.data.getLastTime())