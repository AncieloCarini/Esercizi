'''
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.

Classi:
- Libro: Rappresenta un libro con titolo, autore, stao del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.

- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.

- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.

- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
'''




class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = True
        


class Biblioteca:
    def __init__(self):
        self.catalogo: list[Libro] = []
    
    def aggiungi_libro(self, libro):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        libro = Libro(titolo, autore)
        self.catalogo.append(libro)
        return f"Libro '{titolo}' di {autore} aggiunto con successo"
    
    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo and libro.disponibile:
                libro.disponibile = False
                return f"Libro '{titolo}' prestato con successo"
            elif libro.titolo == titolo and not libro.disponibile:
                return f"Libro '{titolo}' non disponibile"
            return f"Libro '{titolo}' non trovato"
        
    def restituisci_libro(self, titolo): 
        for libro in self.catalogo:
            if libro.titolo == titolo and not libro.disponibile:
                libro.disponibile = True
                return f"Libro '{titolo}' restituito con successo"
            elif libro.titolo == titolo and libro.disponibile:
                return f"Libro '{titolo}' già disponibile"

    def mostra_libri_disponibili(self):
        libri_disponibili = [libro.titolo for libro in self.catalogo 
                             if libro.disponibile]
        return f"Libri disponibili: {', '.join(libri_disponibili)}"
    

    
libro1: Libro = Libro(titolo='Batman', autore='Dc Comics')
libro2: Libro = Libro(titolo='Spiderman', autore='Marvel')


def prova(libro, titolo):
    biblioteca = Biblioteca()
    biblioteca.aggiungi_libro(libro)
    print(biblioteca.presta_libro(titolo))
    print(biblioteca.restituisci_libro(titolo))
    print(biblioteca.mostra_libri_disponibili())


(prova(libro1, 'Batman'))
(prova(libro2, 'Spiderman'))