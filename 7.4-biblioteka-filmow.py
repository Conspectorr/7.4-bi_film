import random
from datetime import date

class BibliotekaMedialna:
    def __init__(self):
        self.biblioteka = []

    def dodaj_media(self, media):
        self.biblioteka.append(media)

    def generuj_odtworzenia(self):
        media = random.choice(self.biblioteka)
        odtworzenia = random.randint(1, 100)
        media.odtworz(odtworzenia)

    def pobierz_filmy(self):
        return sorted([media for media in self.biblioteka if isinstance(media, Film)], key=lambda x: x.tytul)

    def pobierz_seriale(self):
        return sorted([media for media in self.biblioteka if isinstance(media, Serial)], key=lambda x: x.tytul)

    def szukaj(self, tytul):
        wyniki = [media for media in self.biblioteka if tytul.lower() in media.tytul.lower()]
        return sorted(wyniki, key=lambda x: x.tytul)

    def top_tytuly(self, n=3, typ_zawartosci=None):
        if typ_zawartosci == "filmy":
            media_lista = self.pobierz_filmy()
        elif typ_zawartosci == "seriale":
            media_lista = self.pobierz_seriale()
        else:
            media_lista = self.biblioteka

        posortowane_media = sorted(media_lista, key=lambda x: x.odtworzenia, reverse=True)
        return posortowane_media[:n]

class Media:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.odtworzenia = 0

    def odtworz(self, odtworzenia=1):
        self.odtworzenia += odtworzenia

    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"

class Film(Media):
    def __init__(self, tytul, rok_wydania, gatunek):
        super().__init__(tytul, rok_wydania, gatunek)

class Serial(Media):
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu):
        super().__init__(tytul, rok_wydania, gatunek)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def odtworz(self, odtworzenia=1):
        super().odtworz(odtworzenia)

    def __str__(self):
        numer_sezonu_str = str(self.numer_sezonu).zfill(2)
        numer_odcinka_str = str(self.numer_odcinka).zfill(2)
        return f"{self.tytul} S{numer_sezonu_str}E{numer_odcinka_str}"

if __name__ == "__main__":
    biblioteka = BibliotekaMedialna()
    print("Biblioteka filmów")
    
    # Dodanie filmów i seriali do biblioteki
    film1 = Film("Pulp Fiction", 1994, "Kryminał")
    film2 = Film("The Godfather", 1972, "Kryminał")
    serial1 = Serial("The Simpsons", 1989, "Animacja", 1, 5)
    serial2 = Serial("Breaking Bad", 2008, "Dramat", 3, 10)
    biblioteka.dodaj_media(film1)
    biblioteka.dodaj_media(film2)
    biblioteka.dodaj_media(serial1)
    biblioteka.dodaj_media(serial2)

    # Wygenerowanie odtworzeń
    for _ in range(10):
        biblioteka.generuj_odtworzenia()

    # Wyświetlenie najpopularniejszych tytułów
    current_date = date.today().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {current_date}:")
    top_tytuly = biblioteka.top_tytuly(n=3)
    for i, tytul in enumerate(top_tytuly, start=1):
        print(f"{i}. {tytul} - {tytul.odtworzenia} odtworzenia")
