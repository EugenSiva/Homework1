class Kniha:
    def __init__(self, nazov, autor, ISBN, rok_vydania, dostupna=True):
        self.nazov = nazov
        self.autor = autor
        self.ISBN = ISBN
        self.rok_vydania = rok_vydania
        self.dostupna = dostupna

    def vypozicat(self):
        if self.dostupna:
            self.dostupna = False
            return True
        return False

    def vratit(self):
        self.dostupna = True

    def __str__(self):
        return f"{self.nazov} - {self.autor} ({self.rok_vydania}) - {'Dostupná' if self.dostupna else 'Vypožičaná'}"


class Kniznica:
    def __init__(self):
        self.zoznam_knih = []

    def pridat_knihu(self, kniha):
        self.zoznam_knih.append(kniha)

    def vyhladat_knihu(self, nazov):
        return [kniha for kniha in self.zoznam_knih if nazov.lower() in kniha.nazov.lower()]

    def vypozicat_knihu(self, ISBN):
        for kniha in self.zoznam_knih:
            if kniha.ISBN == ISBN:
                return kniha.vypozicat()
        return False

    def vratit_knihu(self, ISBN):
        for kniha in self.zoznam_knih:
            if kniha.ISBN == ISBN:
                kniha.vratit()
                return True
        return False

    def zobraz_dostupne_knihy(self):
        return [kniha for kniha in self.zoznam_knih if kniha.dostupna]


if __name__ == "__main__":
    kniznica = Kniznica()
    kniha1 = Kniha("Začínáme programovat v jazyku Python", "Rudolf Pecinovský", "9788027154678", 2024)
    kniha2 = Kniha("Podivný regiment", "Terry Pratchett", "8071972428", 2008)
    kniha3 = Kniha("Zaklínač 1 Posledné prianie", "Andrzej Sapkowski", "9788085951653", 2011)

    kniznica.pridat_knihu(kniha1)
    kniznica.pridat_knihu(kniha2)
    kniznica.pridat_knihu(kniha3)

    print("Dostupné knihy:")
    for k in kniznica.zobraz_dostupne_knihy():
        print(k)

    print("\nVypožičanie knihy:")
    kniznica.vypozicat_knihu("9788027154678")

    print("Dostupné knihy po vypožičaní:")
    for k in kniznica.zobraz_dostupne_knihy():
        print(k)

    print("\nVrátenie knihy:")
    kniznica.vratit_knihu("9788027154678")

    print("Dostupné knihy po vrátení:")
    for k in kniznica.zobraz_dostupne_knihy():
        print(k)