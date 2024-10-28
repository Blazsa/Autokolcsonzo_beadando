from datetime import datetime
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Autokolcsonzo import Autokolcsonzo


def inicializalas():
    # Autókölcsönző létrehozása:
    kolcsonzo = Autokolcsonzo("Balázs autókölcsönzője")

    # Autók létrehozása
    auto1 = Szemelyauto("ABC-123", "Mercedes", 10000)
    auto2 = Szemelyauto("DEF-456", "BMW", 12000)
    auto3 = Teherauto("GHI-789", "Porsche", 14000)

    # Autók hozzáadása az autók listájához:
    kolcsonzo.autok_hozzaadasa(auto1)
    kolcsonzo.autok_hozzaadasa(auto2)
    kolcsonzo.autok_hozzaadasa(auto3)

    # Bérlések hozzáadása:
    kolcsonzo.berles_hozzaadasa({'rendszam': auto1.rendszam, 'datum': datetime.strptime("2025-01-01", "%Y-%m-%d").date()})
    kolcsonzo.berles_hozzaadasa({'rendszam': auto2.rendszam, 'datum': datetime.strptime("2025-02-01", "%Y-%m-%d").date()})
    kolcsonzo.berles_hozzaadasa({'rendszam': auto3.rendszam, 'datum': datetime.strptime("2025-03-01", "%Y-%m-%d").date()})
    kolcsonzo.berles_hozzaadasa({'rendszam': auto1.rendszam, 'datum': datetime.strptime("2025-04-01", "%Y-%m-%d").date()})

    return kolcsonzo

    

def felhasznaloi_felulet(kolcsonzo):
    while True:
        print("\n1. Autók bérlése")
        print("2. Autók bérlésének lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Válasszon egyet: ")
        print("\n")

        if valasztas == "1":
            # Autók  bérlése:
            kolcsonzo.autok_listazasa()
            rendszam = input("Melyik autót szeretné bérelni (rendszám)? ")
            kolcsonzo.berles_lefoglalasa(rendszam)

        elif valasztas == "2":
            # Bérlés lemondása:
            kolcsonzo.berlesek_listazasa()
            rendszam = input("Melyik autó bérlését szeretné lemondani (rendszám)? ")
            kolcsonzo.berles_lemondasa(rendszam)

        elif valasztas == "3":
            # Aktív bérlések listázása:
            print("Aktív bérlések:\n")
            kolcsonzo.berlesek_listazasa()

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen választás, próbálja újra.")

kolcsonzo = inicializalas()
felhasznaloi_felulet(kolcsonzo)
