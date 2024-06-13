
# In questo problema ricreerete la classica gara tra la tartaruga e la lepre.
# Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento.
# I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. 
# ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 
# e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa,
# i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio,
# il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

# - Tartaruga:
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato.

# - Lepre:
#     - Riposo (20% di probabilità): non si muove.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
#     -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

# Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali
# (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). 
# Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

# Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10.
# Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento"
# quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.

# Iniziate la gara stampando:
# 'BANG !!!!! AND THEY'RE OFF !!!!!'

# Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo),
# stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga,
# la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente,
# i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre 
# e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione.
# Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

# Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70.
# Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga,
# stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". 
# Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"),
# oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.


# Requisiti del Codice:
# - Utilizzare il modulo random per la generazione dei numeri casuali.
# - Definire e utilizzare:
#     - una funzione per visualizzare le posizioni sulla corsia di gara,
#     - una funzione per calcolare la mossa della tartaruga,
#     - una funzione per calcolare la mossa della lepre.
# - Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse,
# mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.



'''
import random  
T = "T"
H = "H"


lunghezza = 70
#pista: list = ['_'] * lunghezza


pista = [('_', '_')] *lunghezza
pista[0] = ('T', 'H')



def print_pista(tartaruga_mosse, lepre_mosse):
    for i in range(70):
        if i == tartaruga_mosse:
            print('T', end='')
        elif i == lepre_mosse:
            print('H', end='')
        elif i == tartaruga_mosse and lepre_mosse:
            print('OUCH!', end='')
        
        

def tartaruga_move():
    posizioneT= pista.index('T')
    x = random.randrange(1, 11)
    if x <= 5:
        pista[posizioneT + 3] = 'T'
        posizioneT = pista.index('T')
    elif x <= 7:
        pista[posizioneT - 6] = 'T'
        posizioneT = pista.index('T')
    elif x <= 10:
        pista[posizioneT + 1] = 'T'
        posizioneT = pista.index('T')


def lepre_move():
    posizioneH = pista.index('H')
    x = random.randrange(1, 11)
    if x <= 2:
        pista[posizioneH + 0] = 'H'
        posizioneH = pista.index('H')
    elif x <= 4:
        pista[posizioneH + 9] = 'H'
        posizioneH = pista.index('H')
    elif x <= 5:
        pista[posizioneH - 12] = 'H'
        posizioneH = pista.index('H')
    elif x <= 8:
        pista[posizioneH + 1] = 'H'
        posizioneH = pista.index('H')
    elif x <= 10:
        pista[posizioneH - 2] = 'H'
        posizioneH = pista.index('H')


print(" BANG !!!!! AND THEY'RE OFF !!!!!")


#print(print_pista(tartaruga_move(), lepre_move()))
lepre_move()
tartaruga_move()

print(pista)

'''







# Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers should be stored in a list and returned as output.

'''
def find_numbers():
    result = []
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5!= 0:
            result.append(num)
    return result

print(find_numbers())

'''


#Write a function to calculate the factorial of a number given as input. The number should be returned as output. For example:

    #Input: 8
    #Output: 40320

'''
def fattoriale(num):
    if num == 0:
        return 1
    else:
        return num * fattoriale(num - 1)

n = int(input('enter a number:'))
print('fattoriale di', n, 'è', fattoriale(n))
'''
    



# se the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers.
# The list is given as input to the function. All factorials should be returned as output. For example:

#     Input: [2, 5, 8, 10]
#     Output: [2, 120, 40320, 3628800]
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def compute_factorials(numbers):
    return [factorial(num) for num in numbers]

numbers = [7, 18, 27, 150]
print("Factorials of", numbers, "are", compute_factorials(numbers))
'''




# Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value)
# pairs such that i is an integer between 1 and n (both included). The function should return the dictionary as output. For example:

#     Input: 8
#     Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def generate_dict(n):
    return {i: i*i for i in range(1, n+1)}      # esempio n = 4  ovvero 1x1 2x2 3x3 4x4 

n = 12
print(generate_dict(n))
