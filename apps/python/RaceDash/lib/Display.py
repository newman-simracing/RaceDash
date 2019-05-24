import ac

class Display:
    appWindow = ac.newApp("RaceDash")
    scale = 1

    def __init__(self, scale):
        self.scale = scale

    def label(self, title, x, y, size, alignment):
        l = ac.addLabel(self.appWindow, title)
        ac.setPosition(l, x * self.scale, y * self.scale)
        ac.setFontSize(l, size * self.scale)
        ac.setFrontAlignment(l, alignment)
        return l

    def button(self, title, x, y, width, height, size, event):
        b = ac.addButton(self.appWindow, "")
        ac.setPosition(b, x * self.scale, y * self.scale)
        ac.setSize(b, width * self.scale, height * self.scale)
        ac.setFontSize(b, size * self.scale)
        ac.drawBorder(b, 0)
        ac.setBackgroundOpacity(b, 0)
        ac.addonClickListener(b, event)
        ac.setText(b, title)
        return b
