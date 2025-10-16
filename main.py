# importo la classe Crociera
from crociera import Crociera

# funzione che definisce il menu al quale l'utente può operare tramite console
def menu():
    print(f'\n--- MENU CROCIERA ---')
    print("1. Modifica nome della crociera")
    print("2. Carica dati da file")
    print("3. Assegna cabina a passeggero")
    print("4. Visualizza cabine ordinate per prezzo")
    print("5. Visualizza elenco passeggeri")
    print("6. Esci")
    return input("Scegli un'opzione >> ")

# funzione principale
def main():
    # richiamo all'oggetto tramite la sua classe e usando il nome (attributo dell'oggetto stesso)
    crociera = Crociera("MSC Futura")

    while True:
        scelta = menu()
# scelta 1 (modifica del nome della crociera)
        if scelta == "1":
            nuovo_nome = input("Inserisci il nuovo nome della crociera: ")
            crociera = Crociera(nuovo_nome)

# scelta 2 (caricare i dati dal file csv)
        elif scelta == "2":
            file_path = "dati_crociera.csv"
            try:
                # richiamo al metodo presente nella classe Crociera per leggere i dati presenti nel file csv
                listaCab, listaPas = crociera.carica_file_dati(file_path)
                print("Dati caricati correttamente.")
                print(listaCab)
                print(listaPas)
            except FileNotFoundError:
                print("File non trovato.")

# scelta 3 (assegnare la cabina a un passeggero)
        elif scelta == "3":
            # richiesta all'utente di inserire il codice della cabina e del passeggero per poter fare l'assegnazione
            codice_cabina = input("Codice cabina: ")
            codice_passeggero = input("Codice passeggero: ")
            try:
                crociera.assegna_passeggero_a_cabina(codice_cabina, codice_passeggero)
                print("Cabina assegnata con successo.")
            except Exception as e:
                print(f"Errore: {e}")

# scelta 4 (visualizzare le cabine ordinate per prezzo)
        elif scelta == "4":
            cabine_ordinate = crociera.cabine_ordinate_per_prezzo()
            print("\n--- Cabine ordinate per prezzo ---")
            # ciclo for per stampare ogni cabina ordinata precedentemente
            for c in cabine_ordinate:
                print(c)

# scelta 5 (visualizzare l'elenco dei passeggeri)
        elif scelta == "5":
            print("\n--- Elenco passeggeri ---")
            # richiamo al metodo presente nella classe Crociera per visualizzare l'elenco dei passeggeri
            crociera.elenca_passeggeri()

# scelta 6 (uscita dal programma)
        elif scelta == "6":
            print("Uscita dal programma.")
            break

# operazione non valida (input dell'utente non corretto)
        else:
            print("Scelta non valida.")
if __name__ == "__main__":
    main()