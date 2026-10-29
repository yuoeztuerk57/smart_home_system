class Geraet:
    anzahl_geraete = 0

    def __init__(self, name: str, stromverbrauch: float):
        self.name = name
        self.__status = False
        self._stromverbrauch = stromverbrauch
        Geraet.anzahl_geraete += 1

    def schalte_an(self):
        self.__status = True

    def schalte_aus(self):
        self.__status = False

    def ist_an(self) -> bool:
        return self.__status

    def __str__(self) -> str:
        status_str = "AN" if self.__status else "AUS"
        return f"Gerät: {self.name} | Status: {status_str} | Verbrauch: {self._stromverbrauch}W"