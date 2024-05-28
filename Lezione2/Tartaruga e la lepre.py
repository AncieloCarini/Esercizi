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




from random import choices
from random import randint


def turtle_walk_speed(t_token, t_energy, weather: bool = False) -> int:
    

    
    
    walking_speed: list[int] = [3, 1, -6]
    
    weight: list[float] = [0.5, 0.3, 0.2]
    
    chosen: int = choices(walking_speed, weight)[0]
    
    index: int = walking_speed.index(chosen)

    if index == 0:
        t_energy -= 5
    elif index == 1:
        t_energy -= 3
    else:
        t_energy -= 10
    if t_energy < 0:
        t_energy = 10
    else:
        t_token += chosen - 1 if weather else chosen

    return t_token, t_energy


def hare_walk_speed(h_token, h_energy, weather: bool = False) -> int:
    
    
    walking_speed: list[int] = [0, 9, -12, 1, -2]
    
    weight: float = [0.2, 0.2, 0.1, 0.3, 0.2]
    
    chosen: int = choices(walking_speed, weight)[0]
    
    index: int = walking_speed.index(chosen)
    
    temp: int = h_energy
    if index == 0:
        h_energy += 10
        h_energy = min(h_energy, 100)
    elif index == 1:
        temp -= 15
    elif index == 2:
        temp -= 20
    elif index == 3:
        temp -= 5
    elif index == 4:
        temp -= 8
    if temp >= 0:
        h_token += chosen - 2 if weather and chosen != 0 else chosen
        h_energy = temp

    return h_token, h_energy


def bonuses_obstacles(token: int, t_name: str, obstacles: dict, bonuses: dict, max_len: int) -> int:
    
    checking: list = []
    values: list = []
    checking_len: int = 0
    start_token: int = token
    while True:
        if token in checking:
            print(f"The {t_name} got out of the loop")
            break
        if token in obstacles.keys():
            print(f"The {t_name} hit an obstacle of {obstacles[token]} on position {token}")
            checking.append(token)
            values.append(obstacles[token])
            token += obstacles[token]
        if token in checking:
            print(f"The {t_name} got out of the loop")
            break
        if token in bonuses.keys():
            print(f"The {t_name} got a bonus {bonuses[token]} on position {token}")
            checking.append(token)
            values.append(bonuses[token])
            token += bonuses[token]
        if checking_len == len(checking):
            break
        checking_len = len(checking)
    if checking:
        if len(checking) > 1:
            print(f"\nThe total amount of movement was {sum(values)} for the {t_name}:")
        print(f"started from {start_token} ended to {min(token,max_len) if token > max_len else max(token,0)}\n")
    return token


def check(t: int, h: int, length: int, **kwargs) -> bool:
  

    route = kwargs["route"]
    weather = kwargs["weather"]
    i = kwargs["i"]

    if t >= length and h >= length:
        route[-1] = "X"
        print(f"Last Round: {i}")
        print("It's raining ☂" if weather else "It's sunny ☀︎")
        show_route(route)
        print("\nIT'S A TIE.")
        print(f"\nroute length: {length}\n")
        return True
    if t >= length:
        route[h if h >= 0 else 0] = "H"
        route[-1] = "T"
        print(f"Last Round: {i}")
        show_route(route)
        print("\nTURTLE WINS! || YAY!!!")
        print(f"\nroute length: {length}\n")
        return True
    if h >= length:
        route[t if t >= 0 else 0] = "T"
        route[-1] = "H"
        print(f"Last Round: {i}")
        show_route(route)
        print("\nHARE WINS || YUCH!!!")
        print(f"\nroute length: {length}\n")
        return True
    return False


def show_route(route: list[str]) -> None:
    
    for char in route:
        print(f"{char}", end="")
    print(end="\n\n")


def start_simulation() -> None:
   
    
    route: list[str] = ["_"]*randint(25, 100)
    max_len: int = len(route) - 1
    
    interval: int = round(max_len * 0.1)
    
    obstacles: dict = {k: -v for k, v in zip(
        range(1, max_len+1),
        [randint(1, max_len//10) for _ in range(1, max_len+1)])
        if k % interval == 0}
    
    bonuses: dict = {k: v for k, v in zip(
        [randint(1, max_len-1) for _ in range(len(obstacles.values()))],
        [randint(1, max_len//10)+3 for _ in range(1, max_len+1)])
        if k not in list(obstacles.keys())}
    i: int = 1
    weather: bool = False
    t_token: int = 0
    t_energy: int = 100
    h_token: int = 0
    h_energy: int = 100
    prev_t: int = 0
    prev_h: int = 0

    
    print("\nBANG !!!!! AND THEY'RE OFF !!!!!\n")
    while True:
        route[t_token], route[h_token] = "_", "_"
        
        if (i-1) % 10 == 0:
            weather = choices([True, False], [0.5, 0.5])[0]
        
        prev_t, prev_h = t_token, h_token
        
        t_token, t_energy = turtle_walk_speed(t_token, t_energy, weather)
        h_token, h_energy = hare_walk_speed(h_token, h_energy, weather)
        
        t_token = bonuses_obstacles(t_token, "turtle", obstacles, bonuses, max_len)
        h_token = bonuses_obstacles(h_token, "hare", obstacles, bonuses, max_len)
        
        if check(t_token, h_token, max_len, route=route, weather=weather, i=i):
            break
        
        t_token = max(t_token, 0)
        h_token = max(h_token, 0)
        # changes route
        if t_token == h_token:
            route[t_token] = 'X'
        else:
            route[t_token] = 'T'
            route[h_token] = 'H'
        
        print(f"Round: {i}", end=" ")
        if i % 3 == 0 or i == 1:
            print("- It's raining ☂" if weather else "- It's sunny ☀︎")
        else:
            print()
        i += 1
        show_route(route)

        print(f"Turtle moved: {t_token-prev_t},",
              f" Turtle position: {t_token},",
              f" Turtle energy: {t_energy}")

        print(f"Hare moved: {h_token-prev_h},",
              f" Hare position: {h_token},",
              f"Hare energy: {h_energy}")

        print("\n")
        if i > 5000:
            print("The race was too long. Neither won and everyone left.\n")
            break


if __name__ == "__main__":
    start_simulation()