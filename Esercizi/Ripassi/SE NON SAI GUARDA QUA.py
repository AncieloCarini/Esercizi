'''
1. School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average,
      and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.


def punteggio(nomi: str, voti: list) -> str:
    sum_voti = sum(voti)
    punteggio_minimo = sum_voti / len(voti)

    if punteggio_minimo >= 60:
        print(f"{nomi}, media_punteggio: {punteggio_minimo}. PROMOSSO\n")
    else:
        print(f"{nomi}, media_punteggio: {punteggio_minimo}. BOCCIATO\n")

studenti:list = ['angelo', 'gabriele', 'giuseppe']
punteggio_studenti:list = [[90,100,60], [80,100,7000], [10,55,60]]

for x in range(len(studenti)):
    if len(studenti) == len(punteggio_studenti):
        punteggio(studenti[x], punteggio_studenti[x])
    else:
        print(f"Someone does't have their votes recorded")
        break
        


        


2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

import random
def gioco() -> str:
    y = int(input('scegli un range con cui giocare: '))
    num = random.randrange(y + 1)

    attempts= input('hai a disposizione 10 tentativi')
    counter = 10
    while counter > 0:
        counter -= 1
        numero = int(input('scegli un numero: '))
        
        if numero > num:
            print(f"numero troppo alto, numero di tentativi {counter}")

        if numero < num:
            print(f"numero troppo basso, numero di tentativi {counter}")
        if numero == num:
            print('hai vinto')
        if counter == 0:
            print('hai perso')
            break

gioco()

persone: list = ['angelo', ' gabriele', 'giuseppe']






3. E-commerce Shopping Cart:
Create a function that defines a product with a name, price, and quantity.
Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
The function should calculate the cart total and apply any discounts or taxes.
Implement a for loop to iterate over the items in the cart and print detailed 
information about each product and the total.
'''


class Product:
    def __init__(self, name: str, price: int, quantity: int) -> None:
        self.name= name
        self.price= price
        self.quantity= quantity


prodotto_1: Product = Product(name='fanta', price= 1000, quantity= 100)

prodotto_2: Product = Product(name='coca_cola', price= 10, quantity= 4)
prodotto_3: Product = Product(name='sprite', price= 500, quantity= 1)


spesa:list = [prodotto_1, prodotto_2, prodotto_3]
carrelloOGG: list = [prodotto_3]


class Carrello:
    def __init__(self, lista_prodotti: list[Product]) -> None:         
        self.lista_prodotti: list[Product] = lista_prodotti
        

carrello1: Carrello= Carrello(lista_prodotti= spesa)
carrello2: Carrello= Carrello(lista_prodotti= carrelloOGG)
for prodotto in carrello1.lista_prodotti:
        
    
        print(prodotto.name)
    
    '''
    
    #print(prodotto.name)




# print(carrello1.lista_prodotti)
# print(carrello2.lista_prodotti)


#inizializzatore che prende in ingresso una lista di prodotti che puo essere vuota o con tante instanze della classe Product




# def product(name: str, price: int, quantity: int) -> str:
#     name: str = name
#     price: int = price
#     quantity: int = quantity









