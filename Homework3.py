class Prvok:
    def __init__(self, data):
        self.data = data
        self.dalsi_prvok = None


class LinkedList:
    def __init__(self):
        self.head = None

    def vloz_prvok(self, data):
        novy_prvok = Prvok(data)
        if self.head is None:
            self.head = novy_prvok
        else:
            aktualny = self.head
            while aktualny.dalsi_prvok:
                aktualny = aktualny.dalsi_prvok
            aktualny.dalsi_prvok = novy_prvok

    def vymaz_prvok(self, data):
        if self.head is None:
            print("Zoznam je prázdny.")
            return

        if self.head.data == data:
            self.head = self.head.dalsi_prvok
            return

        aktualny = self.head
        while aktualny.dalsi_prvok and aktualny.dalsi_prvok.data != data:
            aktualny = aktualny.dalsi_prvok

        if aktualny.dalsi_prvok:
            aktualny.dalsi_prvok = aktualny.dalsi_prvok.dalsi_prvok
        else:
            print("Hodnota sa v zozname nenachádza.")

    def vypis_vsetky(self):
        if self.head is None:
            print("Zoznam je prázdny.")
            return

        aktualny = self.head
        while aktualny:
            print(aktualny.data, end=' -> ' if aktualny.dalsi_prvok else '\n')
            aktualny = aktualny.dalsi_prvok

    def obsahuje(self, data):
        aktualny = self.head
        while aktualny:
            if aktualny.data == data:
                print("Hodnota sa v zozname nachádza.")
                return True
            aktualny = aktualny.dalsi_prvok
        print("Hodnota sa v zozname nenachádza.")
        return False

    def nahrad_hodnotu(self, stara_hodnota, nova_hodnota):
        aktualny = self.head
        while aktualny:
            if aktualny.data == stara_hodnota:
                aktualny.data = nova_hodnota
                return
            aktualny = aktualny.dalsi_prvok
        print("Hodnota sa v zozname nenachádza.")


moj_zoznam = LinkedList()

while True:
    print("Menu:")
    print("1. Pridať prvok")
    print("2. Vymazať prvok")
    print("3. Zobraziť zoznam")
    print("4. Skontrolovať existenciu hodnoty")
    print("5. Nahradiť hodnotu")
    print("6. Ukončiť program")

    volba = input("Vyberte možnosť: ")

    if volba == "1":
        data = input("Zadajte hodnotu: ")
        moj_zoznam.vloz_prvok(data)
    elif volba == "2":
        data = input("Zadajte hodnotu na vymazanie: ")
        moj_zoznam.vymaz_prvok(data)
    elif volba == "3":
        moj_zoznam.vypis_vsetky()
    elif volba == "4":
        data = input("Zadajte hodnotu na kontrolu: ")
        moj_zoznam.obsahuje(data)
    elif volba == "5":
        stara_hodnota = input("Zadajte hodnotu na nahradenie: ")
        nova_hodnota = input("Zadajte novú hodnotu: ")
        moj_zoznam.nahrad_hodnotu(stara_hodnota, nova_hodnota)
    elif volba == "6":
        break
    else:
        print("Neplatná voľba, skúste znova.")