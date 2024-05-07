'''

def blackjack_hand_total(cards: list[int]) -> int:
    x:int = sum(cards)
    if x > 21:
        if 11 in cards:           
            cards.remove(11)
            cards.append(1)
        return(sum(cards))
    else:
        return(x)
    
print(blackjack_hand_total([2, 3, 5]))
print(blackjack_hand_total([11, 5, 5]))
print(blackjack_hand_total([1, 10, 11]))
print(blackjack_hand_total([1, 10, 5]))
print(blackjack_hand_total([11, 5, 3]))

        


def construct_rectangle(area: float) -> list[float]:
    possibilities :list = []
    for length in range (1, area+1): 
        width, invalid = divmod(area, length) 
        if invalid == 0:
            possibilities.append((length, width)) 
    print(possibilities)
    lista_temp: list = []
    for a in possibilities:
        b = list(a)
        if b[0] >= b[1]:
            lista_temp.append(b)
        else:
            continue
    print(lista_temp)
    list_temp_2: list = []
    temp_1: int = 100000000000000
    best_pair: list = None
    for c in lista_temp:
        d = c[0]-c[1]
        if temp_1 > d:
            temp_1 = d
            best_pair = c

    print(best_pair)





construct_rectangle(4)
#lunghezza 4 larghezza 3




Scrivi una funzione che accetta una stringa come input,
rimuove le parole non significative comuni stop_words e restituisce un dizionario in cui le chiavi
sono parole univoche nel testo rimanente
(ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) 
e i valori sono le frequenze di quelle parole
'''

'''
stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text= "The quick brown fox jumps over the lazy dog. The dog is very lazy."

    text_lower = text.lower()
    import re
    text_clear = re.sub(r"[^\w\s]","", text_lower )
    text_clear = text_clear.split()

    stopwords_lower = [x.lower() for x in stopwords]
    text_clear_2 = []
    for word in text_clear:
        if word not in stopwords_lower:
            text_clear_2.append(word)
        
    dic: dict = {}
    for w in text_clear_2:
        if w in dic.keys():
            dic(w) = dic(w) + 1
        else:
            dic[w] = 1
    return dic



def find_disappeared_numbers(nums: list[int]) -> list[int]:

    x = min(nums)
    y = len(nums)
    missing_numbers: list = []
    for z in range(x, y + 1):
        if z not in nums:
            missing_numbers.append(z)
        else:
            continue
    return missing_numbers



numeri: list = [3, 6, 1, 8, 4, 7]
for n in numeri:
    if n % 2 == 0: print(n)
for n in numeri:
    if n % 2 == 1: print(n)

pari: list = [6, 8, 4]
dispari: list = [3, 1, 7]

print(pari + dispari)





    pari: list = []
    dispari: list = []
    for n in nums:
        if n % 2 == 0:
            pari.append(n)
        
    for n in nums:
        if n % 2 != 0 :
            dispari.append(n)
    return pari + dispari


def is_subsequence(s: str, t: str) -> bool: 
    vuota = []
    for x in t:
        if x in s:
            vuota.append(x)
        else:
            continue
    v= "".join(x for x in vuota)
    if v == s:
        return True
    else:
        return False
    
print(is_subsequence("abc", "ahbgdc"))
True

print(is_subsequence("axc", "ahbgdc"))
False
'''


def third_max(nums: list[int]) -> int:
    first_max = second_max = third_max = float('-inf')
    pass

    for num in nums:
        if num > first_max:
            third_max = second_max
            second_max = first_max
            first_max = num
        elif second_max < num < first_max:
            third_max = second_max
            second_max = num
        elif third_max < num < second_max:
            third_max = num


    if third_max != float('-inf'):
        return third_max
    else:
        return first_max

jewels = [3, 2, 1]
third_max(jewels)















print(third_max([3, 2, 1]))
1

print(third_max([1, 2]))
2

print(third_max([2, 2, 3, 1]))
1