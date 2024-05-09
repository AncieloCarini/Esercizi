
'''
Write a function called create_playlist() that accepts a playlist name and a variable number of song titles.
The function should return a dictionary with the playlist name and a set of songs.
 Call the function with different numbers of songs to demonstrate flexibility.
 Write a function called add_like() that accepts a dictionary, the name of a playlist, 
 and a boolean value indicating whether it is liked (True or False). This function should return an updated dictionary.

Example: add_like(dictionary, “Road Trip”, liked=True)


def create_playlist(playlists: str, songs: str) -> dict:
    songs: set = set(songs)
    playlist: dict= {playlists: songs}
    return playlist


def add_like(playlist: dict, playlists: str, liked: bool) -> dict:
    playlist = {playlists:(playlist[playlists]. liked)}
    return playlist
    
print(add_like(create_playlist("simple and clean"),"Road Trip",True))



Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them.
This function should return a dictionary where the author's name is the key and the value is a list of their books. 
Demonstrate this function by adding books for different authors.

Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details.
This function should return an updated dictionary.

Example: delete_book(dictionary, “Mark Twain”)


def add_book(autore: str, libri: list) -> dict:
    dizionario: dict = {autore: libri}
    return dizionario


d = add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

def delete_book(dizionario: dict, libroeliminato: str) -> dict:
    key = next(iter(dizionario))
    dizionario[key].remove(libroeliminato)


delete_book(d, "Life on the Mississippi")
print(d)



Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
Make occupation, location, and age optional parameters. Use this function to create profiles for different people, demonstrating how it handles these optional parameters.

Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)


def build_profile(nome: str, cognome: str, occupazione: str = None, luogo: str = None, age: int = None) -> dict:
    profilo = {}
    profilo['nome'] = nome
    profilo['cognome'] = cognome
    
    if occupazione != None:
        profilo['occupazione'] = occupazione

    if luogo != None:
        profilo['luogo'] = luogo

    return profilo

nome: str = 'Angelo'
cognome: str = 'Locarini'
occupazione: str = 'studente'
luogo: str = 'sezze'
profilo = build_profile(nome, cognome, occupazione, luogo)
print(profilo)

nome = 'Pippo'
cognome: str = 'Baudo'
profilo = build_profile(nome, cognome)
print(profilo)



Write a function called plan_event() that accepts an event name, a list of participants, and an hour.
The function should return a dictionary that includes the event name and a list of the participants. 
Call this function with varying numbers of participants to plan different events.

Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.

Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)


def plan_event(event_name: str, partecipanti: str, ore: int) -> dict:
    evento = {}
    evento ['event_name'] = event_name
    evento ['partecipanti'] = partecipanti
    evento ['ore'] = ore
    
    return evento

event_name: str = 'concerto'
partecipanti: str = 'gianpaolo', 'gianpiero', 'gianluca', 'gianfranco', 'gianluigi'
ore: int = 22.30
evento1 = plan_event(event_name, partecipanti, ore)
print(evento1)

def modify_event(dizionario: dict, chiave: str, nuovo_valore: str) -> dict:
    for key in dizionario.keys():
        if key == chiave:
            dizionario[key]= nuovo_valore
            break

    return dizionario



print(modify_event(dizionario=evento1, chiave='event_name', nuovo_valore='festival'))




Write a function called create_shopping_list() that accepts a store name and any number of items as arguments.
 It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.

Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

Write a function called print_shopping_list() that accepts a dictionary and a store name, 
then prints each item from that store's shopping list.

Example: print_shopping_list(dictionary, "Grocery Store")



def create_shopping_list(negozio: str, cose: int, lista: str) -> dict:
    comprare= {}
    comprare['negozio']= negozio
    comprare['cose']= cose
    comprare['lista']= lista
    return comprare

negozio: str= 'conad'
cose: int= 2
lista: str= 'pesce', 'carne'
shopping= create_shopping_list(negozio, cose, lista)
print(shopping)
'''
