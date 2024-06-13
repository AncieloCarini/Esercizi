#Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti 
#al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

#Definisci una classe Prodotto con i seguenti attributi:
#- nome (stringa)
#- quantità (intero)
 
#Definisci una classe Magazzino con i seguenti metodi:
#- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
#- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
#- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
#Test case:
#Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
#Il sistema cerca un prodotto per verificare se esiste nell'inventario.
#Il sistema verifica la disponibilità dei prodotti in inventario.




class Prodotto:
    def __init__(self, nome, quantita):
        self.nome = nome
        self.quantita = quantita

class Magazzino:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, nome):
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return prodotto
        return None

magazzino = Magazzino()


magazzino.aggiungi_prodotto(Prodotto("Penna", 100))
magazzino.aggiungi_prodotto(Prodotto("Quaderno", 50))
magazzino.aggiungi_prodotto(Prodotto("Matita", 75))




nome_prodotto = "Matita"
prodotto_cercato = magazzino.cerca_prodotto(nome_prodotto)

if prodotto_cercato:
    print(f"Il prodotto '{nome_prodotto}' è presente nel magazzino X{prodotto_cercato.quantita}.")
else:
    print(f"Il prodotto '{nome_prodotto}' non è presente nel magazzino.")

nome_prodotto = "Compasso"
prodotto_cercato = magazzino.cerca_prodotto(nome_prodotto)

if prodotto_cercato:
    if prodotto_cercato.quantita > 0:
        print(f"Il prodotto '{nome_prodotto}' è disponibile nel magazzino.")
    else:
        print(f"Il prodotto '{nome_prodotto}' non è disponibile nel magazzino.")
else:
    print(f"Il prodotto '{nome_prodotto}' è esaurito.")
    