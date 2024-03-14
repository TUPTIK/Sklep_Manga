class Produkt:
    def __int__(self, rozmiar, waga):
        self.rozmiar = rozmiar
        self.waga = waga

    def inf(self):
        print(f"Rozmiar: {self.rozmiar}")
        print(f"Waga: {self.waga}")


class Manga(Produkt):
    def __init__(self, rozmiar, waga, nazwa, numer_wydania, fabula):
        super.__init__(rozmiar, waga)
        self.nazwa = nazwa
        self.numer = numer_wydania
        self.fabula = fabula

    def inf(self):
        super(Manga, self).inf()
        print(f"Nazwa: {self.nazwa}")
        print(f"Numer wydania: {self.numer}")
        print(f"Fabula: {self.fabula}")


class Figurki(Produkt):
    def __init__(self, rozmiar, waga, wyglad):
        super.__init__(rozmiar, waga)
        self.wyglad = wyglad

    def inf(self):
        super(Figurki, self).inf()
        print(f"Wyglad: {self.wyglad}")


class Poduszka(Produkt):
    def __init__(self, rozmiar ,waga:int ,wyglad:str ,material:str, cena:int) -> None:
        super.__init__(rozmiar, waga)
        self.wyglad = wyglad
        self.material = material
        self.cena = cena


    def nowa_cena(self, nowa_cena):
        self.cena = nowa_cena


    def inf(self):
        super(Poduszka, self).inf()
        print(f'Wyglad : {self.wyglad}')
        print(f'Material : {self.material}')
        print(f'Cena : {self.cena}')




class Filmy_anime_DVD(Produkt):
    def __init__(self, rodzaj:str, dlugosc:int, cean:int, ilosc_rekalm:int, ilosc_GB:int) -> None:
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.cena = cean
        self.ilosc_rekalm = ilosc_rekalm
        self.ilosc_GB = ilosc_GB

    def nowa_cena(self, nowa_cena):
        self.cena = nowa_cena


    def inf(self):
        super(Filmy_anime_DVD, self).inf()
        print(f'Rodzaj filmu: {self.rodzaj}')
        print(f'Dlugosc filmu: {self.dlugosc}')
        print(f'Cena filmu: {self.cena}')
        print(f'Ilosc reklam: {self.ilosc_rekalm}')
        print(f'Waga wyrazona w GB: {self.ilosc_GB}')



class Fan_arty(Produkt):
    def __init__(self, rozmiar, waga:int, jakie_kolory:str, ilosc_uzytych_rzeczy:int, czas:int, temat:str, cena:int) -> None:
        super.__init__(rozmiar, waga)
        self.kolory = jakie_kolory
        self.ilosc_uzytych_rzeczy = ilosc_uzytych_rzeczy
        self.czas = czas
        self.temat = temat
        self.cena = cena

    def nowa_cena(self, nowa_cena):
        self.cena = nowa_cena

    def inf(self):
        super(Fan_arty, self).inf()
        print(f'Kolory wkonania: {self.kolory}')
        print(f'Ilosc urzytych zeczy do wytworzenia dziela: {self.ilosc_uzytych_rzeczy}')
        print(f'Czas potrzebny do wykonania: {self.czas}')
        print(f'Konkrettny temat wykonania: {self.temat}')
        print(f'Cena: {self.cena}')



