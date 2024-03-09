class Osoba:
    def __init__(self, imie, nazwisko, rok):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok

    def inf(self):
        print(f"Imie: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Rok: {self.rok}")


    def zmien_wyplate(self, nowa_wyplata):
            self.zarobek = nowa_wyplata

    def zmien_doswiadczenie(self, nowe_doswiadczenie):
            self.doswiadczenie = nowe_doswiadczenie



class Kasjer:
    def __init__(self, osoba, zarobek, doswiadczenie):
        self.pracownik = Pracownik(osoba, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Obsługuje klientów na kasie")


class Sprzataczka:
    def __init__(self, osoba, zarobek, doswiadczenie):
        self.pracownik = Pracownik(osoba, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Sprząta")


class Dostawca:
    def __init__(self, osoba, zarobek, doswiadczenie):
        self.pracownik = Pracownik(osoba, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Dostarcza towar")


class Informatyk:
    def __init__(self, osoba, zarobek, doswiadczenie):
        self.pracownik = Pracownik(osoba, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Zajmuje się IT")


class Menager:
    def __init__(self, osoba, zarobek, doswiadczenie):
        self.pracownik = Pracownik(osoba, zarobek, doswiadczenie)

    def czynnosc(self):
        print("Zarządza personelem")


# Przykład użycia:
osoba = Osoba("Joe", "Worker", 1980)
kasjer = Kasjer(osoba, 2000, 3)
kasjer.pracownik.inf()
kasjer.czynnosc()


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
