
class Statystyki:
    def __init__(self):
        self.oceny_produktow = {}
        self.zakupione_produkty = {}
        self.zarobki = 0
        self.licznik_klientow = 0

    def dodaj_zakup(self, produkt, cena):
        if produkt in self.zakupione_produkty:
            self.zakupione_produkty[produkt] += 1
        else:
            self.zakupione_produkty[produkt] = 1

        self.zarobki += cena

        self.licznik_klientow += 1

    def dodaj_ocene_produktu(self, produkt, ocena):
        if produkt in self.oceny_produktow:
            self.oceny_produktow[produkt].append(ocena)
        else:
            self.oceny_produktow[produkt] = [ocena]

    def dodaj_klienta(self):
        self.licznik_klientow += 1

    def srednie_oceny_i_ilosci_zakupionych(self):
        for produkt, oceny in self.oceny_produktow.items():
            srednia_ocena = sum(oceny) / len(oceny) if oceny else 0
            ilosc_zakupow = self.zakupione_produkty.get(produkt, 0)
            print(f"Produkt: {produkt}, Średnia ocena: {srednia_ocena}, Ilość zakupów: {ilosc_zakupow}")

statystyki = Statystyki()

statystyki.dodaj_ocene_produktu("Manga", 4)
statystyki.dodaj_ocene_produktu("Figurki", 5)
statystyki.dodaj_ocene_produktu("X", 3)

statystyki.srednie_oceny_i_ilosci_zakupionych()

