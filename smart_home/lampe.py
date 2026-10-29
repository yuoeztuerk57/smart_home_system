from .geraet import Geraet


class SmartLampe(Geraet):
    def __init__(self, name: str, stromverbrauch: float, helligkeit: int = 100):
        super().__init__(name, stromverbrauch)
        self.helligkeit = helligkeit

    def schalte_aus(self):
        super().schalte_aus()
        self.helligkeit = 0

    def __str__(self) -> str:
        return f"{super().__str__()} | Helligkeit: {self.helligkeit}%"