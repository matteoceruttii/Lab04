# importo le classi Cabina (con anche le sottoclasi) e Passeggero
from cabina import *
from passeggero import Passeggero

# classe Crociera
class Crociera:
# funzione che inizializza gli attributi e le strutture dati (stampa e setter/getter)
    def __init__(self, nome):
        self._nome = nome
        self.listaPasseggeri = []
        self.listaCabine = []

        # ATTRIBUTO NOME
        # getter
        @property
        def nome(self):
            return self._nome
        # setter
        @nome.setter
        def nome(self, nome):
            self._nome = nome

# definizione delle proprietà di stampa degli attributi relativi alla classe
    def __str__(self):
        return f"Nome crociera: {self._nome}"

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(Nome crociera={self._nome}')

# funzione per confrontare oggetti o per ordinarli
    def __eq__(self, other):
        return (self._nome == other._nome)

# funzione per caricare i dati contenuti nel file csv in un'apposita struttura dati
    def carica_file_dati(self, file_path):
        # apertura del file
        infile = open(file_path, "r", encoding="utf-8")
        # lettura delle singole righe e aggiunta dei vari campi alla lista corrispondente
        for riga in infile:
            campi = riga.split(",")
            # CABINA
            if 'CAB' in campi[0]:
                # cabina standard
                if len(campi) == 4:
                    cabina = Cabina(campi[0], campi[1], campi[2], campi[3])
                # cabina per animali
                elif campi[4].isdigit():
                    cabina = CabinaAnimali(campi[0], campi[1], campi[2], campi[3], campi[4])
                # cabina deluxe
                else:
                    cabina = CabinaDeluxe(campi[0], campi[1], campi[2], campi[3], campi[4])
                self.listaCabine.append(cabina)
            # PASSEGGERO
            elif 'P' in campi[0]:
                passeggero = Passeggero(campi[0], campi[1], campi[2])
                self.listaPasseggeri.append(passeggero)
            else:
                print("Campo non valido")
        # chiusura del file
        infile.close()
        return self.listaCabine, self.listaPasseggeri

# funzione che assegna una cabina a un passeggero
    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

# funzione che ordina le cabine per prezzo (metodi dunder)
    def cabine_ordinate_per_prezzo(self):
        return

# funzione che elenca i passeggeri mostrando, per ognuno, la cabina a cui è associata (quando applicabile)
    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO