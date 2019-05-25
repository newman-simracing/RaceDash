import RaceDash.lib.RaceDash as RaceDash
import RaceDash.modules as modules

raceDash = RaceDash({ scale: 1, opacity: 0.6 })

def acMain(ac_version):
    raceDash.add(modules.RPM, { x: 0, y: 0 })
    raceDash.add(modules.RPMBar, { x: 0, y: 0 })
    
    raceDash.add(modules.Gear, { x: 10, y: 10 })
    raceDash.add(modules.Speed, { x: 0, y: 0 })

    raceDash.add(modules.Position, { x: 0, y: 10 })

    raceDash.add(modules.BestTime, { x: 100, y: 30 })
    raceDash.add(modules.LastTime, { x: 100, y: 40 })

def acUpdate(deltaT):
    raceDash.update(deltaT)

def acShutdown():
    raceDash.save()