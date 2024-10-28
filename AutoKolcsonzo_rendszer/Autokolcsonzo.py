from datetime import datetime

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_hozzaadasa(self, auto):
        self.autok.append(auto)

    
    def autok_listazasa(self):
        print("Elérhető autók:")
        for auto in self.autok:
            print(auto)

    
    def berles_hozzaadasa(self, berles):
        self.berlesek.append(berles)


    def berlesek_listazasa(self):
        if not self.berlesek:
            print("Nincs aktív bérlés.")
        else:
            print("Aktív bérlések:")
            for berles in self.berlesek:
                print(f"Rendszám: {berles['rendszam']}, Dátum: {berles['datum']}")

    def berles_lefoglalasa(self, rendszam):
        if rendszam not in [auto.rendszam for auto in self.autok]:
            print(f"Nincs ilyen rendszámú autó: {rendszam}")
            return
        
        datum_str = input("Adja meg a foglalni kívánt dátumot (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        except ValueError:
            print("Hibás dátum formátum!")

        if  datum < datetime.today().date():
            print("A megadott dátum múltbeli dátum!")
            return

        for berles in self.berlesek:
            if berles['rendszam'] == rendszam and berles['datum'] == datum:
                print(f"A {rendszam} rendszámú autó már foglalt {datum} napjára.")
                return
        
        uj_berles = {'rendszam': rendszam, 'datum': datum}
        self.berlesek.append(uj_berles)
        print(f"A {rendszam} rendszámú autó sikeresen lefoglalva {datum} napjára.")

    def berles_lemondasa(self, rendszam):
        if rendszam not in [auto.rendszam for auto in self.autok]:
            print(f"Nincs ilyen rendszámú autó: {rendszam}")
            return

        datum_str = input("Adja meg a törölni kívánt dátumot (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        except ValueError:
            print("Hibás dátum formátum!")
            return
        
        for berles in self.berlesek:
            if berles['rendszam'] == rendszam and berles['datum'] == datum:
                self.berlesek.remove(berles)
                print(f"A {rendszam} rendszámú autó bérlése sikeresen lemondva.")
                return
        print(f"Nincs bérlés a(z) {rendszam} rendszámú autóhoz.")