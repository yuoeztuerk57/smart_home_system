from .geraet import Geraet


class Klimaanlage(Geraet):
    def __init__(self, name: str, stromverbrauch: float, ziel_temperatur: float = 21.0):
        super().__init__(name, stromverbrauch)
        self._ziel_temperatur = ziel_temperatur
        if ziel_temperatur < 18.0:
            print("Warnung: Ziel-Temperatur unter 18 Grad eingestellt!")

    @property
    def ziel_temperatur(self) -> float:
        return self._ziel_temperatur

    @ziel_temperatur.setter
    def ziel_temperatur(self, wert: float):
        if wert < 18.0:
            print("Warnung: Ziel-Temperatur unter 18 Grad eingestellt!")
        self._ziel_temperatur = wert

    def __str__(self) -> str:
        return f"{super().__str__()} | Ziel-Temperatur: {self._ziel_temperatur}°C"