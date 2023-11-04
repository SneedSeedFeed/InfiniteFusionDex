from collections.abc import Mapping

class AbilityOverrides(Mapping):
    def __init__(self):
        pidgey_line = [("Tangled Feet", False),("Keen Eye", False),("Big Pecks", True)]
        ekans_line = [("Shed Skin", False), ("Intimidate", False), ("Unnerve", True)]
        diglett_line = [("Arena Trap", False), ("Sand Veil", False), ("Sand Force", True)]
        growlithe_line = [("Flash Fire", False), ("Intimidate", False), ("Justified", True)]
        machop_line = [("No Guard", False), ("Guts", False), ("Steadfast", True)]
        geodude_line = [("Sturdy", False), ("Rock Head", False), ("Sand Veil", True)]
        krabby_line = [("Shell Armor", False), ("Hyper Cutter", False), ("Sheer Force", True)]
        voltorb_line = [("Static", False),("Soundproof", False),("Aftermath",True)]
        cubone_line = [("Lightning Rod", False), ("Rock Head", False), ("Battle Armor", True)]
        chinchou_line = [("Illuminate", False), ("Volt Absorb", False), ("Water Absorb", True)]
        marill_line = [("Huge Power", False), ("Thick Fat", False), ("Sap Sipper", True)]
        snubbull_line = [("Run Away", False), ("Intimidate", False), ("Rattled", True)]

        self._data = {
            # Gengar
            92: [("Levitate", False)],
            # Pidgey line
            16: pidgey_line,
            17: pidgey_line,
            18: pidgey_line,
            # Ekans line
            23: ekans_line,
            24: ekans_line,
            # Diglett line
            50: diglett_line,
            51: diglett_line,
            # Growlithe line
            58: growlithe_line,
            59: growlithe_line,
            # Machop line
            66: machop_line,
            67: machop_line,
            68: machop_line,
            # Geodude line
            74: geodude_line,
            75: geodude_line,
            76: geodude_line,
            # Farfetch'd
            83: [("Inner Focus", False), ("Keen Eye", False), ("Defiant", True)],
            # Onix
            95: [("Sturdy", False), ("Rock Head", False), ("Weak Armor", True)],
            # Steelix
            208: [("Sturdy", False), ("Rock Head", False), ("Sheer Force", True)],
            # Krabby line
            98: krabby_line,
            99: krabby_line,
            # Voltorb line
            100: voltorb_line,
            101: voltorb_line,
            # Cubone line
            104: cubone_line,
            105: cubone_line,
            # Hitmonchan
            107: [("Iron Fist", False), ("Keen Eye", False), ("Inner Focus", True)],
            # Lapras
            131: [("Shell Armor", False), ("Water Absorb", False), ("Hydration", True)],
            # Snorlax
            143: [("Thick Fat", False), ("Immunity", False), ("Gluttony", True)],
            # Aerodactyl
            142: [("Pressure", False),("Rock Head", False), ("Unnerve", True)],
            # Chinchou Line
            170: chinchou_line,
            171: chinchou_line,
            # Marill line
            183: marill_line,
            184: marill_line,
            # Dunsparce
            206: [("Run Away", False), ("Serene Grace", False), ("Rattled", True)],
            # Murkrow
            198: [("Super Luck", False), ("Insomnia", False), ("Prankster", True)],
            # Honchkrow
            430: [("Super Luck", False), ("Insomnia", False), ("Moxie", True)],
            # Snubbull line
            209: [("Run Away", False), ("Intimidate", False), ("Rattled", True)],
            210: [("Quick Feet", False), ("Intimidate", False), ("Rattled", True)],
            # Teddiursa
            216: [("Quick Feet", False), ("Pickup", False), ("Honey Gather", True)],
            # Ursaring
            217: [("Quick Feet", False), ("Guts", False), ("Unnerve", True)],
            # Absol
            359: [("Super Luck", False), ("Pressure", False), ("Justified", True)],
            # Clefairy
            35: [("Magic Guard", False), ("Cute Charm", False), ("Friend Guard", True)],
            # Clefable
            36: [("Magic Guard", False), ("Cute Charm", False), ("Unaware", True)]
        }

    def __getitem__(self, item):
        return self._data.get(item)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data
