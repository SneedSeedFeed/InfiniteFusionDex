from collections.abc import Mapping

class FusionTypeOverrides(Mapping):
    def __init__(self):
        bulbasaur_line = "Grass"
        geodude_line = "Rock"
        gastly_line = "Ghost"
        self._data = {
            # Bulbasaur line
            1: bulbasaur_line,
            2: bulbasaur_line,
            3: bulbasaur_line,
            # Charizard
            6: "Fire",
            # Geodude line
            74: geodude_line,
            75: geodude_line,
            76: geodude_line,
            # Gastly line
            92: gastly_line,
            93: gastly_line,
            94: gastly_line,
            # Onix
            95: "Rock",
            # Scyther
            123: "Bug",
            # Gyarados
            130: "Water",
            # Articuno
            144: "Ice",
            # Zapdos
            145: "Electric",
            # Moltres
            146: "Fire",
            # Dragonite
            149: "Dragon",
            # Steelix
            208: "Steel",
        }

    def __getitem__(self, item):
        return self._data.get(item)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data
