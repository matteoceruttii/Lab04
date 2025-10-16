# classe Cabina
class Cabina:
    def __init__(self, codice, numLetti, ponte, prezzoBaseNotte):
        self._codice = codice
        self._numLetti = numLetti
        self._ponte = ponte
        self._prezzoBaseNotte = prezzoBaseNotte

        # ATTRIBUTO CODICE
        # getter
        @property
        def codice(self):
            return self.codice
        # setter
        @codice.setter
        def codice(self, nome):
            self._codice = codice

        # ATTRIBUTO NUMERO DEI LETTI
        # getter
        @property
        def num_letti(self):
            return self._numLetti
        # setter
        @num_letti.setter
        def num_letti(self, numLetti):
            self._numLetti = numLetti

        # ATTRIBUTO PONTE
        # getter
        @property
        def ponte(self):
            return self._ponte
        # setter
        @ponte.setter
        def ponte(self, nome):
            self._ponte = ponte

        # ATTRIBUTO COSTO BASE PER NOTTE
        # getter
        @property
        def prezzo_base_notte(self):
            return self._prezzoBaseNotte
        # setter
        @prezzo_base_notte.setter
        def prezzo_base_notte(self, prezzoBaseNotte):
            self._prezzoBaseNotte = prezzoBaseNotte

    def __str__(self):
        return (f"Codice: {self._codice}, "
                f"Numero di letti: {self._numLetti}, "
                f"Ponte: {self._ponte}, "
                f"Prezzo Base: {self._prezzoBaseNotte}")
    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"Codice={self._codice}, "
                f"NumeroLetti={self._numLetti}, "
                f"Ponte={self._ponte}, "
                f"PrezzoBaseNotte={self._prezzoBaseNotte}")


# sottoclasse cabina per animali
class CabinaAnimali(Cabina):
    def __init__(self, codice, numLetti, ponte, prezzoBaseNotte, numeroAnimali):
        # importo tutti gli attributi della classe parent
        super().__init__(codice, numLetti, ponte, prezzoBaseNotte)
        self.numeroAnimali = numeroAnimali


# sottoclasse cabina deluxe
class CabinaDeluxe(Cabina):
    def __init__(self, codice, numLetti, ponte, prezzoBaseNotte, tipologia):
        # importo tutti gli attributi della classe parent
        super().__init__(codice, numLetti, ponte, prezzoBaseNotte)
        self.tipologia = tipologia