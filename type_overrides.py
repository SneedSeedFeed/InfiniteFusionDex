from collections.abc import Mapping

class TypeOverrides(Mapping):
    def __init__(self):
        magnemite_line = ["Steel", "Electric"]
        omanyte_line = ["Water", "Rock"]
        self._data = {
            # Magnemite line
            81: magnemite_line,
            82: magnemite_line,
            462: magnemite_line,
            # Dewgong
            87: ["Ice", "Water"],
            # Omanyte line
            138: omanyte_line,
            139: omanyte_line,
            # Scizor
            212: ["Steel", "Bug"],
            # Empoleon
            395: ["Steel", "Water"],
            # Spiritomb
            442: ["Dark", "Ghost"],
            # Ferrothorn
            598: ["Steel", "Grass"],
            # Celebi
            251: ["Grass", "Psychic"]
        }

    def __getitem__(self, item):
        return self._data.get(item)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data
