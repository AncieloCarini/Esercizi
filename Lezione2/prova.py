


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