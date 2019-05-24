import RaceDash.lib.RaceDash as RaceDash
import RaceDash.modules as modules

raceDash = RaceDash({ scale: 1 })
raceDash.add(modules.RPM, { x: 0, y: 0 })
raceDash.add(modules.Position, { x: 0, y: 10 })
