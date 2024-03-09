class Osoba:
    def __init__(self, imie, nazwisko, rok):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok

    def inf(self):
        print(f"Imie: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Rok: {self.rok}")


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, rok, zarobek, doswiadczenie):
        super().__init__(imie, nazwisko, rok)
        self.zarobek = zarobek
        self.doswiadczenie = doswiadczenie

    def inf(self):
        super().inf()
        print(f"Zarobek: {self.zarobek}")
        print(f"Doświadczenie: {self.doswiadczenie}")

    def zmien_wyplate(self, nowa_wyplata):
        self.zarobek = nowa_wyplata

    def zmien_doswiadczenie(self, nowe_doswiadczenie):
        self.doswiadczenie = nowe_doswiadczenie


class Kasjer(Pracownik):
    def __init__(self, imie, nazwisko, rok, zarobek, doswiadczenie):
        super().__init__(imie, nazwisko, rok, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Obsługa przy kasie ")


class Sprzataczka(Pracownik):
    def __init__(self, imie, nazwisko, rok, zarobek, doswiadczenie):
        super().__init__(imie, nazwisko, rok, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Sprząta")


class Dostawca(Pracownik):
    def __init__(self, imie, nazwisko, rok, zarobek, doswiadczenie):
        super().__init__(imie, nazwisko, rok, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Dostarcza towar")


class Informatyk(Pracownik):
    def __init__(self, imie, nazwisko, rok, zarobek, doswiadczenie):
        super().__init__(imie, nazwisko, rok, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Zajmuje się IT")


class Menager(Pracownik):
    def __init__(self, imie, nazwisko, rok, zarobek, doswiadczenie):
        super().__init__(imie, nazwisko, rok, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Zarządza personelem")


# class Osoba:
#     def __init__(self, imie, nazwisko, rok):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.rok = rok

#     def inf(self):
#         print(f"Imie: {self.imie}")
#         print(f"Nazwisko: {self.nazwisko}")
#         print(f"Rok: {self.rok}")


# class Klijent(Osoba):
#     def __init__(self, imie, nazwisko, rok, kasa):
#         super().__init__(imie, nazwisko, rok)
#         self.kasa = kasa

#     def pokaz_kase(self):
#         print(f"kas: {self.kasa}")


# class Pracownik(Osoba):
#     licznik = 0
#     def __init__(self, imie, nazwisko, rok, zarobek):
#         super().__init__(imie, nazwisko, rok)
#         Pracownik.licznik += 1
#         self.numer = Pracownik.licznik
#         self.zarobek = zarobek


# class Sprzedawca(Pracownik):
#     def __init__(self, imie, nazwisko, rok, numer_kasy, zarobek):
#         super().__init__(imie, nazwisko, rok, zarobek)
#         self.numer_kasy = numer_kasy

#     def inf(self):
#         super(Sprzedawca, self).inf()
#         print(self.numer_kasy)
#         print(f"Zarobek: {self.zarobek}")


# class Sprzataczka(Pracownik):
#     def __init__(self, imie, nazwisko, rok, zarobek):
#         super().__init__(imie, nazwisko, rok, zarobek)

#     @staticmethod
#     def strantnij():
#         print("spranta")
