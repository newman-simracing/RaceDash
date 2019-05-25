import RaceDash.lib.Module

class Subline(RaceDash.lib.Module):
    def __init__(self, display, data, options):
        super().__init__(display, data, options)
        self.options.fontSize = 10

        self.valueOptions = self.options.join({
            color: [0.9, 0.9, 0.9, 1]
        })

        self.descriptionOptions = self.options.join({
            color: [0.2, 0.2, 0.2, 1]
        })

    def render(self, valueContent, descriptionContent):
        self.value = self.display.addLabel(self.options.join({
            content: valueContent,
            x: 0,
            fontAlignment: "left"
        }))

        self.label = self.display.addLabel(self.options.join({
            content: descriptionContent,
            x: 100,
            fontAlignment: "right"
        })

    def update(self):
        pass