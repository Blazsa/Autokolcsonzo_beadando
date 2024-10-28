from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)

    def __str__(self):
        return f"A {self.rendszam} rendszámú {self.tipus} típusú autó bérleti díja {self.berleti_dij} Ft/nap."
        