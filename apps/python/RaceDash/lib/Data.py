import platform
import os
import sys
import configparser
import ac
import acsys

class Data:
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
