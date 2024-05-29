# Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.

# La lista di interi è formata così:

# L'elemento in posizione 0 corrisponde alla radice
# Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
# Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
# Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti,
# significa che il nodo che corrisponde a quell'indice è una foglia.










# class TreeNode:
    
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    

# def symmetric(tree: list[int]) -> bool:
#     if tree[1] != tree[2]:
#         return False
#     else:
#         if tree[2*1 +1] == tree[2*(2+1)] and tree [2 * (1+1)] == tree[2*2 + 1 ]:
#             return True
#         else:
#             return False
                
                    
                    
            


# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
# in genere utilizzando tutte le lettere originali esattamente una volta.
# fai in modo che il primo print risulti True il secondo print False e il terzo print True                    

'''

def anagram(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())


        





                
    



print(anagram("rat", "car"))
print(anagram("anagram","nagaram"))
print(anagram("NeurIPS","UniReps"))
'''









# Progettare un semplice sistema bancario con i seguenti requisiti:

#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.





class Account:
    def __init__(self, account_id: str, balance: float = 0.0):
        self.account_id = account_id
        self.balance = balance
        self.transactions = []
    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")
        print(f"Deposit successful. New balance: {self.balance}")
        
        

    def get_balance(self):
        return self.balance
    def get_transactions(self):
        return self.transactions




        


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id: str):
        if account_id not in self.accounts:
            self.accounts[account_id] = Account(account_id)
        else:
            print("Account already exists")

    def deposit(self, account_id: str, amount: float):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        else:
            print("Account does not exist")

    def get_balance(self, account_id: str):
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        else:
            print("Account does not exist")



bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

	

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
















