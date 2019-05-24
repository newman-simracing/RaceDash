import RaceDash.lib
import RaceDash.modules

lib = RaceDash.lib
modules = RaceDash.modules

data = lib.Data()
display = lib.Display(1)

modules.RPM(data, display, { x: 0, y: 0 })
modules.Position(data, display, { x: 0, y: 14 })
