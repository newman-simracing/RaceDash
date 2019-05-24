import platform
import os
import sys
import configparser
import ac
import acsys

class RaceDashData:
    def __init__(self):
        if platform.architecture()[0] == "64bit":
           sysdir = os.path.dirname(__file__) + "/stdlib64"
        else:
           sysdir = os.path.dirname(__file__) + "/stdlib" 

        sys.path.insert(0, sysdir)
        os.environ["PATH"] = os.environ["PATH"] + ";."

        self.loadConfig()

    def loadConfig(self):
        configPath = "apps/python/RaceDash/config.ini"
        config = configparser.ConfigParser()
        config.read(configPath)

    def getGear(self):
        value = ac.getCarState(0, acsys.CS.Gear)

        if (value) == 0:
           return "R"

        if value == "N":
           return "N"

        value - 1

    def getSpeed(self, mph):
        if mph:
            ac.getCarState(0, acsys.CS.SpeedMPH)
        else:
            ac.getCarState(0, acsys.CS.SpeedKMH)

    def getRPM(self):
        ac.getCarState(0, acsys.CS.RPM)

    def getTurbo(self):
        ac.getCarState(0, acsys.CS.TurboBoost)

    def getPosition(self):
        return {
            actual: 1,
            total: 200
        }

class RaceDashDisplay:
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

class RaceDashModule:
    def __init__(self, data, display, options):
        self.data = data
        self.display = display
        self.options = options

class RPMModule(RaceDashModule):
    def __init__(self, data, display, options):
        super().__init__(data, display)

        x = options.x | 0
        y = options.y | 0

        self.display.label("---- rpm", x, y, 14, "left")

class PositionModule(RaceDashModule):
    def __init__(self, data, display, options):
        super().__init__(data, display)

        x = options.x | 0
        y = options.y | 0

        self.l = self.display.label("Pos: -/-", x, y, 14, "left")

    def update(self):
        pos = self.data.getPosition()
        ac.setText(self.l, "Pos: {}/{}".format(pos.actual, pos.total)


data = RaceDashData()
display = RaceDashDisplay(1)

RPMModule(data, display, { x: 0, y: 0 })
PositionModule(data, display, { x: 0, y: 14 })
