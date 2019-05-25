import ac

IMAGE_FOLDER = "apps/python/RaceDash"

class Display:
    def __init__(self, options):
        self.appWindow = ac.appWindow
        self.scale = scale | 1
        self.x = x * self.scale | 0
        self.y = y * self.scale | 0

    def addLabel(self, options):
        options.x = options.x | 0
        options.y = options.y | 0
        options.fontSize = options.fontSize | 10
        options.fontFamily = options.fontFamily | "Roboto"
        options.fontAlignment = options.fontAlignment | "center"
        options.color = options.color | [0.8, 0.8, 0.8, 1]
        
        item = ac.addLabel(self.appWindow, options.content)
        ac.setPosition(item, self.x + options.x * self.scale, self.y + options.y * self.scale)
        ac.setFontSize(item, self.fontSize)
        ac.setFontAlignment(item, self.fontAlignment)
        ac.setCustomFont(item, options.fontFamily, 1, 0)
        ac.setFontColor(item, options.color[0], options.color[1], options.color[2], options.color[3])
        
        return item

    def updateLabel(self, label, options):
        if (options.value):
            ac.setText(label, options.value)

        if (options.color):
            ac.setFontColor(label, options.color[0], options.color[1], options.color[2], options.color[3])

    def addImage(self, texture, options):
        options.x = options.x | 0
        options.y = options.y | 0
        options.width = options.width | 100
        options.height = options.height | 100

        item = ac.addLabel(self.appWindow, "")
        ac.setPosition(item, self.x + options.x * self.scale, self.y + options.y * self.scale)
	    ac.setSize(item, options.width * self.scale, options.height * self.scale)
        ac.setVisible()
        ac.setBackgroundTexture(item, IMAGE_FOLDER + texture)

        return item

    def addButton(self, event, options):
        options.x = options.x | 0
        options.y = options.y | 0
        options.fontSize = options.fontSize | 10
        options.border = options.border | 0
        options.opacity = options.opacity | 1

        item = ac.addButton(self.appWindow, "")
        ac.setPosition(item, self.x + options.x * self.scale, self.y + options.y * self.scale)
        ac.setFontSize(item, options.fontSize)
        ac.drawBorder(item, options.border)
        ac.setBackgroundOpacity(item, options.opacity)
        ac.addonClickListener(item, event)
        ac.setText(item, options.content)

        return item