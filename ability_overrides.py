from collections.abc import Mapping

class AbilityOverrides(Mapping):
    def __init__(self):
        self._data = {
            # Gengar should have levitate, not hidden
            92: [("Levitate", False)]
        }

    def __getitem__(self, item):
        return self._data.get(item)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data
