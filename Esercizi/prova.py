


'''
def sum_above_threshold(numbers: list[int], control_number) -> int:
    lista_vuota= []
    for x in numbers:
        if x > control_number:
            lista_vuota.append(x)
        else:
            continue

    somma = sum(lista_vuota)
    return somma





def numero_magico(num: int) -> bool:
    while num != 0:
        if num % 4 == 0 and num % 6 !=0:
            return True
        if num % 6 == 0:
            return False
        break

print(numero_magico(12))



def classifica_numeri(lista: int) -> dict[str:list[int]]:
    lista_pari: list = []
    lista_dispari : list= []

    for num in lista:
        if num % 2 == 0:
            lista_pari.append(num)
        if num % 2 != 0:
            lista_dispari.append(num)


    numeri= {"pari":[], "dispari":[]}
    numeri["pari"]= lista_pari
    numeri["dispari"]= lista_dispari
    return numeri





print(classifica_numeri([]))





def countdown(n: int) -> int:
    numeri : list= []
    for num in range(n +1):
        numeri.append(num)


    numeri = numeri[::-1]
    for num in numeri:
        print(num)

countdown(5)





def convert_temperature(num: int, faranite: bool) -> float:
    
    if num > 0:
        if faranite == None:
            fara = (num*(9/5)) + 32
            return fara
        else:
            cels = (num - 32) * (5/9)
            return cels
    if num < 0:
        num = - num
        if faranite == None:
            fara = (num*(9/5)) + 32
            fara = - fara
            return fara
        else:
            cels = (num - 32) * (5/9)
            cels = - cels
            return cels
'''


'''

#def rotate_left(elements: list, k: int) -> list:
    #numeri: list =[1, 2, 3]

def rotate_left(lst, k):
   
    k = k % len(lst)
    

    rotated_list = lst[k:] + lst[:k]
    
    return rotated_list



lista = [1, 2, 3, 4, 5]
posizioni_da_ruotare = 2
nuova_lista = rotate_left(lista, posizioni_da_ruotare)
print("Lista originale:", lista)
print("Lista ruotata di", posizioni_da_ruotare, "posizioni verso sinistra:", nuova_lista)

'''








'''
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.





def transform(x: int) -> int:
    if x % 2 == 0:
        x = x / 2
    else:
        x = x * 3 - 1
    return x
        
'''

'''
Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati.
L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" 
la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.


def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        stipendio_lordo = ore_lavorate * 10
    else:
        stipendio_lordo = 40 * 10 + (ore_lavorate - 40) * 15
    return stipendio_lordo
            
'''
'''
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51


def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1, 8):
        print(i,)
    print()


    print("Sequenza b):")
    for i in range(3, 24, 5):
        print(i
    print()
    



    print("Sequenza c):")
    for i in range(20, -11, -6):
        print(i)
    print()



    print("Sequenza d):")
    for i in range(19, 52, 8):
        print(i, end=" ")
    print()
    
    return

'''
'''
Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, 
restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e che
 l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!



def integerPower(base: int, esponente: int) -> str:
    x = base
    for i in range(1, esponente):
        base *= x
    return str(base)

        


 
print(integerPower(3, 4))
    
print(integerPower(2, 5))

'''

'''
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo.
La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.

Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
senza libreria math

def hypotenuse(lato1: float, lato2: float):
    return (lato1**2 + lato2**2)**0.5
'''
'''
Scrivi una funzione che, dato un numero intero, determina se è un "numero magico".
Un numero magico è definito come un numero che contiene il numero 7.


def is_magic_number(num: int) -> bool:
    while num > 0:
        if num % 10 == 7:
            return True
        num //= 10
        return False

'''

'''
Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi
(ore, minuti e secondi) e restituisca il numero dei secondi da quando
l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, 
ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari,
entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la
funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti 
entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.
'''
'''
def seconds_since_noon (ore: int, minuti: int, secondi: int) -> int:
    return ore * 3600 + minuti * 60 + secondi

def time_difference(orario1_ore: float, orario1_minuti: float, orario1_secondi: float, orario2_ore: float, orario2_minuti: float, orario2_secondi: float) -> float:
    tempo1 = seconds_since_noon(orario1_ore, orario1_minuti, orario1_secondi)
    tempo2 = seconds_since_noon(orario2_ore, orario2_minuti, orario2_secondi)
    x = tempo1 - tempo2
    return abs(x)

    
    


print(time_difference(1, 0, 0, 3, 15, 30))
print(time_difference(11, 59, 59, 2, 0, 0))
'''



'''
Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo,
a mano a mano che il tempo passa su un orologio simulato.

Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente; 
poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, 
si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.

Ci si fermi al quinto rimbalzo.
 
Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
"Tempo: 0 Altezza: 0"
 
Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
"Tempo: 4 Rimbalzo!"
'''
'''
def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    while rimbalzi < 5:
        print(f"Tempo: {tempo} Altezza: {altezza:.2f}")
        altezza += velocita
        velocita -= 96
        if altezza < 0:
           altezza *= -0.5
           velocita *= -0.5
           rimbalzi += 1
           print(f"Tempo: {tempo} Rimbalzo!")
        tempo += 1

    
    

rimbalzo()




Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione. Prima che il file compresso venga memorizzato, deve essere diviso in blocchi da 512 byte ciascuno.
 
Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi, dove ogni valore intero della lista rappresenta la dimensione non compressa di un singolo file espressa in byte.
 
Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa, deve calcolare la dimensione compressa di tale file espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa), calcolare il numero di blocchi (arrotondato al numero intero più vicino) da 512 byte necessari per la memorizzazione, al fine di determinare se il file compresso può essere salvato nello spazio rimanente nel supporto di memorizzazione o meno.
 
In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione originale del file, la dimensione compressa, i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione. 
Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:
 
"File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
 
Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa un numero di blocchi più grande di quelli rimasti disponibili sul supporto di memorizzazione. In tal caso, la funzione deve avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è sufficiente per salvare il file. 
Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:
 
"Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."
Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000 blocchi. 




def memorizza_file(files: list[int]) -> None:
    blocchi_disponibili: int = 1000
    for file_size in files:
        compressed_size: float = file_size * 0.8
        blocchi_necessari: int = math.ceil(compressed_size / 512)
        if blocchi_necessari <= blocchi_disponibili:
            print(f"File di {file_size} byte compresso in {compressed_size:.1f} byte e memorizzato. Blocchi usati")
            {blocchi_necessari}. Blocchi rimanenti: {blocchi_disponibili - blocchi_necessari}
            blocchi_disponibili -= blocchi_necessari
        else:
            print(f"Non è possibile memorizzare il file di {file_size} byte. Spazio insufficiente.")

                        
            




memorizza_file([1100, 20000, 1048576, 512, 5000])

'''







'''
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    counter = 0
    lista_nuova = lista.copy()
    for k,v in da_rimuovere.items():
        while v > counter:
    
            if k in lista:
                lista_nuova.remove(k)
            counter += 1
        else:
            break
    
    return lista_nuova
'''

'''
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
'''
'''
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    new_dict = {}
    for x in voti:    
        nome_studente= x['nome']
        voto_studente= x["voto"]
        if nome_studente in new_dict:
            new_dict[nome_studente].append(voto_studente)
        else:
            new_dict[nome_studente] = [voto_studente]
    
    
    return new_dict

'''


'''
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    prodotti_scontati: dict = {}
    for k,v in prodotti.items():
        if v > 20:
            prodotti_scontati[k] = v
        else:
            continue
    for k,v in prodotti_scontati:
        new_v = v - ((v *10)/100).items
        prodotti_scontati[k] = new_v
    return prodotti_scontati









print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))
'''




# Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. 
# La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

# Classe Contatore
# Attributi:
# - conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

# Metodi:
# - __init__(): Inizializza l'attributo conteggio a 0.
# - setZero(): Imposta il conteggio a 0.
# - add1(): Incrementa il conteggio di 1.
# - sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. 
#    Se il conteggio è già 0, stampa un messaggio di errore.
# - get(): Restituisce il valore corrente del conteggio.
# - mostra(): Stampa a schermo il valore corrente del conteggio.

'''
class Contatore:
    def __init__(self):
        self.conteggio = 0
    
    def setZero(self):
        self.conteggio = 0
        
    
    def add1(self):
        self.conteggio += 1
        

    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print('Non è possibile eseguire la sottrazione')
        
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print("Conteggio attuale:", self.conteggio)

numero: Contatore = Contatore()
numero.setZero
numero.add1()
numero.sub1()
numero.get()
numero.mostra()
'''

    
# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare,
# modificare, e cercare ricette basate sugli ingredienti. 
# Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.

#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
# Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
# Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
# Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): 
# Sostituisce un ingrediente con un altro nella ricetta specificata. 
# Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - list_recipes(): Elenca tutte le ricette esistenti.

#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. 
# Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
# Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
        
'''

class RecipeManager:
    def __init__(self):
        self.recipes: dict[str, list[str]] = {}

    
    def create_recipe(self, name: str, ingredients: list[str]):
        if name in self.recipes:
            return "Recipe already exists"
        else:
            self.recipes[name] = ingredients
            return {name: self.recipes[name]}
        
    def add_ingredient(self, recipe_name, ingredient: str):
        if recipe_name in self.recipes:
            if ingredient not in self.recipes[recipe_name]:
                self.recipes[recipe_name].append(ingredient)
                return {recipe_name: self.recipes[recipe_name]}
    
    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name in self.recipes:
            if ingredient in self.recipes[recipe_name]:
                self.recipes[recipe_name].remove(ingredient)
                return {recipe_name: self.recipes[recipe_name]}
            
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name in self.recipes:
            if old_ingredient in self.recipes[recipe_name]:
                posizione = self.recipes[recipe_name].index(old_ingredient)
                self.recipes[recipe_name].remove(old_ingredient)
                self.recipes[recipe_name].insert(posizione, new_ingredient)
                return {recipe_name: self.recipes[recipe_name]}
            
            
    def list_recipes(self,):
        return list(self.recipes.keys())
    
        
    def list_ingredients(self, recipe_name):
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        
        
    def search_recipe_by_ingredient(self, ingredient):
        found_recipes = dict()
        for recipe, ingredients in self.recipes.items():
            if ingredient in ingredients:
                found_recipes[recipe] = ingredients
        return found_recipes


result: RecipeManager = RecipeManager
result.create_recipe
result.add_ingredient
result.remove_ingredient
result.update_ingredient
result.list_recipes
result.list_ingredients
result.search_recipe_by_ingredient



manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
'''







# In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
# Attributi:

#     marca (stringa)
#     modello (stringa)
#     anno (intero)

# Metodi:

#     __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
#     descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:

#     numero_porte (intero)

# Metodi:

#     __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
#     descrivi_veicolo(self): metodo che sovrascrive quello della classe base per 
# includere anche il numero di porte nella descrizione, 
# nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:

#     tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

# Metodi:

#     __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
#     descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, 
# nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".


'''
class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def descrivi_veicolo(self):
        print("" f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
    
        
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")    

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
    



veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo() 
auto.descrivi_veicolo()
moto.descrivi_veicolo()
'''




# Obiettivo
# L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita
#  delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

# Descrizione del problema
# Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale.
# Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
# - In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
# - in quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
# Specifiche tecniche

# 1. Classe Specie
# - Attributi:

#     nome (str): Nome della specie.
#     popolazione (int): Popolazione iniziale.
#     tasso_crescita (float): Tasso di crescita annuo percentuale.

# - Metodi:

#     __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): 
# Costruttore per inizializzare gli attributi della classe.
#     cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
#     anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni 
# la popolazione di questa specie supererà quella di un'altra specie.
#     getDensita(self, area_kmq: float) -> int: Metodo per calcolare 
# in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².

 

# 2. Sottoclassi BufaloKlingon e Elefante
# Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie 
# e devono inizializzare il nome della specie rispettiva.
 
# Formule Matematiche:

#     Aggiornamento della popolazione per l'anno successivo:
#         Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
#     Calcolo della densità di popolazione:
#         Formula: popolazione / area_kmq
#         Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
#     Calcolo degli anni necessari per superare la popolazione di un'altra specie:
#         Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie
# finché la popolazione di questa specie non supera quella dell'altra.
# Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000. 

'''

class Specie:
    def __init__(self, nome: str, popolazione: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita
        
        

        

    
    def cresci(self):
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita / 100))


    def anni_per_superare(self, altra_specie: 'Specie')-> int:
        anni = 0
        while self.popolazione <= altra_specie.popolazione:
            self.cresci()
            altra_specie.cresci()
            anni += 1
        return anni
        
        
        
        
            
    def getDensita(self, area_kmq: float)-> int:
        anni = 0
        while self.popolazione / area_kmq < 1:
            self.cresci()
            anni += 1
        return anni
    
    


class BufaloKlingon(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("BufaloKlingon", popolazione, tasso_crescita)

    
class Elefante(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione, tasso_crescita)






# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")


'''



# In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
# Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
# ### Classe Room:
# La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), 
#un numero di posti (seats) e un'area (area). L'area è calcolata come il doppio dei posti.
# - Metodi:
#     - get_id(): Restituisce l'ID dell'aula.
#     - get_floor(): Restituisce il piano dell'aula.
#     - get_seats(): Restituisce il numero di posti dell'aula.
#     - get_area(): Restituisce l'area dell'aula.

# ### Classe Building:
# La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address),
# un intervallo di piani (floors), e una lista di aule (rooms).
# - Metodi:
#     - get_floors(): Restituisce l'intervallo di piani dell'edificio.
#     - get_rooms(): Restituisce la lista delle aule nell'edificio.
#     - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
#     - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.

'''
class Room:
    def __init__(self, id: int, floor: int, seats: int):
        self.id = id
        self.floor = floor
        self.seats = seats
        
        

    def get_id(self):
        return self.id
    def get_floor(self):
        return self.floor
    def get_seats(self):
        return self.seats
    def get_area(self):
        return self.seats * 2
    

class Building:
    def __init__(self, name: str, address: str, floors: int):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []
    
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    
    def add_room(self, room: Room):
        ground_floor, last_floor = self.floors
        if room not in self.rooms:
            if room.floor in range(ground_floor, last_floor +1):
                self.rooms.append(room)
        

    def area(self):
        total_area = 0
        for room in self.rooms:
            total_area += room.get_area()
        return total_area
        
    
    


# Creazione di stanze
room1 = Room(id="Room1", floor=1, seats=15)
room2 = Room(id="Room2", floor=5, seats=20)
room3 = Room(id="Room3", floor=11, seats=10)  # Questo piano è fuori dal range

# Test classe Room
print("Test classe Room:")
print(f"ID: {room1.get_id()}, Atteso: Room1")
print(f"Piano: {room1.get_floor()}, Atteso: 1")
print(f"Posti: {room1.get_seats()}, Atteso: 15")
print(f"Area: {room1.get_area()}, Atteso: 30.0")

# Creazione di un edificio
building = Building(name="Test Building", address="123 Test St", floors=(1, 10))

# Test di inizializzazione Building
print("\nTest di inizializzazione Building:")
print(f"Nome: {building.name}, Atteso: Test Building")
print(f"Indirizzo: {building.address}, Atteso: 123 Test St")
print(f"Piani: {building.floors}, Atteso: (1, 10)")
print(f"Stanze iniziali: {building.get_rooms()}, Atteso: []")

# Test aggiunta stanza valida
building.add_room(room1)
print("\nDopo aggiunta Room1:")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test aggiunta stanza su piano non valido
building.add_room(room3)
print("\nDopo tentativo di aggiunta Room3 (piano non valido):")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test aggiunta stanza duplicata
building.add_room(room1)
print("\nDopo tentativo di aggiunta duplicato Room1:")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test calcolo area
building.add_room(room2)
print("\nDopo aggiunta Room2:")
print(f"Area totale: {building.area()}, Atteso: 70.0")

# Test rappresentazione in stringa Building
print("\nRappresentazione in stringa dell'edificio:")
print(f"Nome Edificio: {building.name}")
print(f"Indirizzo Edificio: {building.address}")
print(f"Piani Edificio: {building.get_floors()}")
print("Stanze nell'edificio:")
for room in building.get_rooms():
    print(f"ID Stanza: {room.get_id()}, Piano: {room.get_floor()}, Posti: {room.get_seats()}, Area: {room.get_area()}")
print(f"Area totale dell'edificio: {building.area()}m2")

# Verifica valori attesi
atteso_stanze = ["Room1", "Room2"]
atteso_area = 70.0
print(f"\nVerifica finale: Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: {atteso_stanze}")
print(f"Verifica finale: Area totale: {building.area()}, Atteso: {atteso_area}")
'''
	

# ### Classi Person, Student e Lecturer:
# La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
# Le classi Student e Lecturer ereditano da Person.
# Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
#     - set_group(group): Associa un gruppo di studio allo studente

# ### Classe Group:
# La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti
# (students) e una lista di docenti (lecturers).
# - Metodi:
#     - get_name(): Restituisce il nome del gruppo
#     - get_limit(): Restituisce il limite di studenti nel gruppo
#     - get_students(): Resituisce la lista di studenti nel gruppo
#     - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti.
# Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
#     - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
#     - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.

'''
class Person:
    def __init__(self, cf, name, surname, age):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
        





class Student(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group):
        self.group = group
        group.add_student(self)




class Lecturer(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)


class Group:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
        self.lecturers_limit = limit // 10 + 1
    def get_name(self):
        return self.name
    def get_limit(self):
        return self.limit
    def get_students(self):
        return self.students
    def get_limit_lecturers(self):
        return max(1, len(self.students) // 10)
    def add_student(self, student):
        if len(self.students) < self.limit and student not in self.students:
            self.students.append(student)
            student.set_group(self)
    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
    



# Creazione delle persone
person1 = Person(cf="CF123", name="John", surname="Doe", age=30)
student1 = Student(cf="CF456", name="Jane", surname="Smith", age=20)
lecturer1 = Lecturer(cf="CF789", name="Dr. Emily", surname="Brown", age=45)

# Test della classe Person
print("Test della classe Person:")
print(f"CF: {person1.cf}, Atteso: CF123")
print(f"Nome: {person1.name}, Atteso: John")
print(f"Cognome: {person1.surname}, Atteso: Doe")
print(f"Età: {person1.age}, Atteso: 30")

# Test della classe Student
print("\nTest della classe Student:")
print(f"CF: {student1.cf}, Atteso: CF456")
print(f"Nome: {student1.name}, Atteso: Jane")
print(f"Cognome: {student1.surname}, Atteso: Smith")
print(f"Età: {student1.age}, Atteso: 20")
print(f"Gruppo iniziale: {student1.group}, Atteso: None")

# Test metodo set_group della classe Student
group1 = Group(name="Group A", limit=10)
student1.set_group(group1)
print("\nDopo set_group di student1:")
print(f"Gruppo di student1: {student1.group.get_name()}, Atteso: Group A")

# Test della classe Lecturer
print("\nTest della classe Lecturer:")
print(f"CF: {lecturer1.cf}, Atteso: CF789")
print(f"Nome: {lecturer1.name}, Atteso: Dr. Emily")
print(f"Cognome: {lecturer1.surname}, Atteso: Brown")
print(f"Età: {lecturer1.age}, Atteso: 45")

# Creazione di un gruppo e aggiunta di studenti e docenti
group2 = Group(name="Group B", limit=2)
group2.add_student(student1)
group2.add_lecturer(lecturer1)

print("\nDopo aggiunta di student1 e lecturer1 a group2:")
print(f"Studenti in group2: {[student.cf for student in group2.get_students()]}, Atteso: [CF456]")
print(f"Docenti in group2: {[lecturer.cf for lecturer in group2.lecturers]}, Atteso: [CF789]")

'''






# class Room:
#     def __init__(self, id: int, floor: int, seats: int):
#         self.id = id
#         self.floor = floor
#         self.seats = seats
        
        

#     def get_id(self):
#         return self.id
#     def get_floor(self):
#         return self.floor
#     def get_seats(self):
#         return self.seats
#     def get_area(self):
#         return self.seats * 2
    

# class Building:
#     def __init__(self, name: str, address: str, floors: int):
#         self.name = name
#         self.address = address
#         self.floors = floors
#         self.rooms = []
    
#     def get_floors(self):
#         return self.floors
    
#     def get_rooms(self):
#         return self.rooms
    
    
#     def add_room(self, room: Room):
#         ground_floor, last_floor = self.floors
#         if room not in self.rooms:
#             if room.floor in range(ground_floor, last_floor +1):
#                 self.rooms.append(room)
        

#     def area(self):
#         total_area = 0
#         for room in self.rooms:
#             total_area += room.get_area()
#         return total_area

# class Person:
#     def __init__(self, cf, name, surname, age):
#         self.cf = cf
#         self.name = name
#         self.surname = surname
#         self.age = age

# class Student(Person):
#     def __init__(self, cf, name, surname, age):
#         super().__init__(cf, name, surname, age)
#         self.group = None

#     def set_group(self, group):
#         self.group = group
#         group.add_student(self)

# class Lecturer(Person):
#     def __init__(self, cf, name, surname, age):
#         super().__init__(cf, name, surname, age)

# class Group:
#     def __init__(self, name, limit):
#         self.name = name
#         self.limit = limit
#         self.students = []
#         self.lecturers = []
#         self.lecturers_limit = limit // 10 + 1
#     def get_name(self):
#         return self.name
#     def get_limit(self):
#         return self.limit
#     def get_students(self):
#         return self.students
#     def get_limit_lecturers(self):
#         return max(1, len(self.students) // 10)
#     def add_student(self, student):
#         if len(self.students) < self.limit and student not in self.students:
#             self.students.append(student)
#             student.set_group(self)
#     def add_lecturer(self, lecturer):
#         if len(self.lecturers) < self.get_limit_lecturers():
#             self.lecturers.append(lecturer)


# # ### Classe Course:
# # La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
# # - Metodi:
# #     - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
# #     - get_groups(): Restituisce la lista dei gruppi nel corso.
# #     - add_group(group): Aggiunge un gruppo al corso.
# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.groups = []

#     def register(self, student):
#         for group in self.groups :
#             if len(group.get_students()) < group.get_limit():
#                 group.add_student(student)
#                 break
            
                
            
            
            
    
#     def get_groups(self):
#         return self.groups
    
#     def add_group(self, group):
#         self.groups.append(group)





# # Creazione degli edifici
# smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
# armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

# # Aggiunta delle stanze all'edificio smi
# smi.add_room(Room(id="123", floor=3, seats=32))
# smi.add_room(Room(id="333", floor=0, seats=42))
# smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
# smi.add_room(Room(id="111", floor=-1, seats=32))

# # Aggiunta delle stanze all'edificio smi
# armellini.add_room(Room(id="567", floor=3, seats=22))
# armellini.add_room(Room(id="888", floor=0, seats=32))
# armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
# armellini.add_room(Room(id="999", floor=2, seats=22))

# # Output dei risultati
# print("### SMI ###")
# print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
# print(f"Area totale dell'edificio SMI: {smi.area()} m²")
# print("### ARMELLINI ###")
# print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
# print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


# # Creazione dei gruppi
# fullstack = Group(name="Fullstack", limit=1)
# cloud = Group(name="Cloud", limit=10)
# cyber = Group(name="Cyber", limit=10)

# # Creazione di un corso e aggiunta dei gruppi al corso
# course = Course(name="Python")
# course.add_group(fullstack)
# course.add_group(cloud)
# course.add_group(cyber)

# # Registrazione degli studenti al corso
# course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
# course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
# course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
# course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
# course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
# course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
# course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
# course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
# course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
# course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
# course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
# course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
# course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

# print("### COURSE DETAILS ###")
# print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
# print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
# print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")








# Obiettivo:
# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) 
# e una classe derivata Film che rappresenti specificamente un film. 
# Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

# Specifiche della Classe Media:
 
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, 
# il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%

# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film,
# aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().



class Media:
    def __init__(self, title, reviews):
        self.title = title
        self.reviews = reviews

    def set_title(self, title):
        self.title = title
        return self
    def get_title(self):
        return self.title
    def aggiungiValutazione(self, voto):
        if 1 <= voto <= 5:
            self.reviews.append(voto)
    def getMedia(self):
        return sum(self.reviews) / len(self.reviews)
    def getRate(self):
        media = self.getMedia()
        if media < 2:
            return "Terribile"
        elif media < 3:
            return "Brutto"
        elif media < 4:
            return "Normale"
        elif media < 5:
            return "Bello"
        elif media < 6:
            return "Grandioso"
    # def ratePercentage(self, voto):
    #     return (self.reviews.count(voto) / len(self.reviews)) * 100
    # def recensione(self):
    #     print(f"Titolo del Film: {self.title}")
    #     print(f"Voto Medio: {self.getMedia():.2f}")
    #     print(f"Giudizio: {self.getRate()}")
    #     print(f"Terribile: {self.ratePercentage(1):.2f}%")
    #     print(f"Brutto: {self.ratePercentage(2):.2f}%")
    #     print(f"Normale: {self.ratePercentage(3):.2f}%")
    #     print(f"Bello: {self.ratePercentage(4):.2f}%")
    #     print(f"Grandioso: {self.ratePercentage(5):.2f}%")


class Film(Media):
    def __init__(self, title):
        super().__init__(title)
        self.reviews = []
    def ratePercentage(self, voto):
        return (self.reviews.count(voto) / len(self.reviews)) * 100
    def recensione(self):
        print(f"Titolo del Film: {self.title}")
        print(f"Voto Medio: {self.getMedia():.2f}")
        print(f"Giudizio: {self.getRate()}")
        print(f"Terribile: {self.ratePercentage(1):.2f}%")
        print(f"Brutto: {self.ratePercentage(2):.2f}%")
        print(f"Normale: {self.ratePercentage(3):.2f}%")
        print(f"Bello: {self.ratePercentage(4):.2f}%")
        print(f"Grandioso: {self.ratePercentage(5):.2f}%")




titolo = Film('Eragon')
titolo.aggiungiValutazione(5)
titolo.aggiungiValutazione(4)
titolo.aggiungiValutazione(3)
titolo.aggiungiValutazione(2)
titolo.aggiungiValutazione(1)
titolo.recensione()
print(titolo.getMedia())
