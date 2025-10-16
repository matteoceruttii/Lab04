class Passeggero():
    # inizializzazione degli attributi della classe Passeggero
    def __init__(self, codice, nome, cognome):
        self._codice = codice
        self._nome = nome
        self._cognome = cognome

    # definizione dei metodi getter e setter
        # ATTRIBUTO CODICE
        # getter
        @property
        def codice(self):
            return self.codice
        # setter
        @codice.setter
        def codice(self, nome):
            self._codice = codice

        # ATTRIBUTO NOME
        # getter
        @property
        def nome(self):
            return self._nome
        # setter
        @nome.setter
        def nome(self, nome):
            self._nome = nome

        # ATTRIBUTO COGNOME
        # getter
        @property
        def cognome(self):
            return self._cognome
        # setter
        @cognome.setter
        def cognome(self, nome):
            self._cognome = cognome

    # definizione delle funzioni per la formattazione di stampa
    def __str__(self):
        return f"{self._codice} - {self._nome} - {self._cognome}"
    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"Codice={self._codice} - Nome={self._nome} - Cognome:{self._cognome}")