import produkty
import statystiki

class Magazyn:
    def __init__(self, cena) -> None:
        self.magazyn = []
        self.sprzedarz = []
        self.cena = cena
        self.statystyki = statystiki.Statystyki()


    def dodaj_mange(self):
        self.magazyn.append(produkty.Manga)

    def dodaj_figurka(self):
        self.magazyn.append(produkty.Figurki)
    
    def dodaj_poduszka(self):
        self.magazyn.append(produkty.Poduszka)
    
    def dodaj_Filmy(self):
        self.magazyn.append(produkty.Filmy_anime_DVD)

    def dodaj_Fanarty(self):
        self.magazyn.append(produkty.Fan_arty)
        

    
    
    def usun_zecz_z_magazynu(self, a):
        self.magazyn.remove(self.magazyn[a])
    
    def usun_zecz_sprzedarz(self, a):
        self.magazyn.remove(self.cena[a])

    def przenies_z_magazynu_na_sprzedaz(self, a):
        self.sprzedarz.append(self.magazyn[a])
        self.magazyn.remove(self.magazyn[a])

    def ocena(self, l):
        self.statystyki.dodaj_zakup()
        
