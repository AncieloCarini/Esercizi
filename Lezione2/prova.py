


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

'''



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