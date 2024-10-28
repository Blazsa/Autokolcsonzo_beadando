from abc import ABC, abstractmethod

class Auto(ABC):

    @abstractmethod
    def __init__(self, rendszam, tipus, berleti_dij):
        self.__rendszam = rendszam
        self.__tipus = tipus
        self.__berleti_dij = berleti_dij

    @property
    def rendszam(self):
        return self.__rendszam

    @property
    def tipus(self):
        return self.__tipus

    @property
    def berleti_dij(self):
        return self.__berleti_dij
