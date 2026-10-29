from smart_home import Geraet, SmartLampe, Klimaanlage

if __name__ == "__main__":
    print("SMART HOME SYSTEM LOG")
    print()

    tv = Geraet("Fernseher", 120.0)
    lampe = SmartLampe("Wohnzimmerlampe", 15.0, 80)
    klima = Klimaanlage("Klimaanlage Schlafzimmer", 1500.0, 22.0)

    print(f"Anzahl erstellter Geräte: {Geraet.anzahl_geraete}")
    print()

    print("Initialer Status:")
    print(tv)
    print(lampe)
    print(klima)
    print()

    print("Geräte einschalten:")
    tv.schalte_an()
    lampe.schalte_an()
    klima.schalte_an()
    print(tv)
    print(lampe)
    print()

    print("Lampe ausschalten:")
    lampe.schalte_aus()
    print(lampe)
    print()

    print("Klimaanlage Temperatur unter 18 Grad stellen:")
    klima.ziel_temperatur = 16.0
    print(klima)