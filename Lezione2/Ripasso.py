
#creazione variabile
nome_variabile: int = 10   
nome_variabile: float = 10.0
nome_variabile: bool = False
nome_variabile: str = 'ciao'


#nome_variabile vieni sostituito da 10 e si somma al +5
nome_variabile: int = 10
nome_variabile = nome_variabile + 5
'oppure'
nome_variabile += 5








#si può fare solo su python ma non va fatto in quanto un int e un float non vanno sommati in altri linguaggi
variabile_float: float = 0.0
variabile_float = 5.0 + 10









#divisione = /    divisione con floor division ovvero risultato solo con il numero intero (3.5 diventa 3) = //
lunghezza_lista: int = 7
punto_di_mezzo: int = 7 / 2
#punto_di_mezzo: int = 7 // 2  #il risutato in questo caso è 3 

import math #utile per aggiungere funzioni matematiche
math.ceil(punto_di_mezzo) #in questo caso invece di 3 prende il 4 ovvero l'intero più vicino
print(math.ceil(punto_di_mezzo))








#operazioni con i booleani
var_1: bool = True
var_2: bool = False

print(var_1 and var_2) # (and) ritorna True solo se entrambe sono True
print(var_1 or var_2)  # (or) basta che almeno uno sia True per avere True
print(not var_1)       # (not) restituisce il contrario True=False 






# (if) ha bisogno di condizioni per entrare in funzione e che siano vere

if var_1 and var_2:     #in questo caso è False quindi non entra nell' if
#if var_1 or var_2:     #in questo caso è True e quindi entra
    
    print(f'{var_1 and var_2}')


# essendo corretta l'operazione si entra  / nel caso ci fosse stato (or) al posto di (and) 
#la seconda operazione poteva essere anche sbagliata

x: int = 10
if x > 0 and x < 20:
    print(f'{var_1 and var_2}')

if x in range(10):
    print(f'x:  {x}')



#bubblesort     [i]= alla posizione nella lista che parte da 0 e prosegue fino all'erorre

lista: list = [1, 2, 5, 3]

for i in range(len(lista)-1):

    if lista[i] > lista[i+1]:

        temp : int = lista[i]

        lista[i] = lista[i + 1]

        lista[i+1] = temp
print(lista)



#condizioni con if elif e else   (printa solo quella corretta ovvero quella True)

a: bool = True
b: bool = False


if a and b:
    print(f'sono nel primo if')
elif a or b:
    print(f'sono nel primo elif')
else:
    print(f'sono nell else')





              #0  1  2  3
lista: list = [1, 2, 3, 5]

lista[0]                                #cosi prendo direttamente la prima posizione in lista senza usare for o altre cose

for numero in lista:                    #per ogni elemento in lista   ('numero' sta per gli elementi in lista)
    
    print(f'x^2: {numero**2}')          #sto portando alla seconda i numeri nella lista



numero: int = 0                            #ho riscritto numero perchè nella fase precedente ha assunto un altro valore

for numero in range(len(lista)):           #in questo caso si sta prendendo la posizione non il numero

    print(f'x^2: {lista[numero]**2}')      #sto portando alla seconda LE POSIZIONI della lista




contatore: int = 0                          # while necessita di un contatore
while contatore < len(lista):               #il ciclo while serve per ripetere più volte la stessa istruzione finche non viene interrotta

    print(f'x^2: {lista[contatore]**2}')
    contatore += 1
    




anagrafe: dict = {                                 #struttura dizionario
    'persona_1': 'Angelo',                         #persona = chiave
    'persona_2': 'Gabriele',                       #il nome = valore
    'persona_3': 'Giuseppe'}



anagrafe['persona_1']                                     #cosi accedi al valore della chiave
print(anagrafe['persona_1']) 


anagrafe['persona_4'] = 'gabbo'                           #cosi aggiungo al dizionario una nuova chiave
anagrafe['persona_2'] = 'gabbo'                           #cosi viene sovrascritta la chiave 2 sostituendo il nome






anagrafe: dict = {                                 
    'persona_1': 'Angelo',                         
    'persona_2': 'Gabriele',                       
    'persona_3': 'Giuseppe'}

key: str = 'persona_100'                              



#devo estrarre da questa lista nome dello studente e il voto a lui associato e metterle come key e value nel dizionario vuoto
voti: list = [{'nome': 'Angelo', 'voto': 20}, {'nome': 'Gabriele', 'voto': 30}, {'nome': 'Angelo', 'voto': 10}]

aggr: dict = {}                               #creo un dizionario vuoto

for dizionario in voti:                       #creo un ciclo for che mi va a prendere tutti gli elementi della lista ovvero i dizionari
                                              #e li chiamo dizionario

    studente: str = dizionario['nome']            #prendiamo una nuova variabile (studente) e la associamo al valore della key nome presente nel dizionario
    voto: int = dizionario['voto']
    print(studente , voto)

    if studente in aggr:                         # primo if: controlliamo se studente è presente nel dizionario vuoto (aggr)
        aggr[studente].append(voto)              # se la condizione è vera andiamo ad aggiungere al suo valore associato il nuovo voto

    else:                                        # se il primo if è falso ovvero studente non è nel dizionario
        aggr[studente] = [voto]                  #aggiungo al dizionario il nome dello studente e il voto sotto forma di lista           

    print(aggr)

#nel caso in cui ci fosse un altra chiave con lo stesso nome ovvero: angelo è ripetuto piu di una volta non si aggiungerà al dizionario vuoto
#ma se il nome è lo stesso e il voto è diverso, all'interno della lista dove viene stampato il voto verrà aggiunto anche l'altro voto



a: list = [1,2]           #lista modificabile
b: tuple = (1,2)          #la tupla no
 
a[0] = 3
b[0] = 3
