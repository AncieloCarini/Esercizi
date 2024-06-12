
# 1. GESTIONALE PAGAMENTO
# Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza 
# l'importo del pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro 
# da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno.
# Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, ad esempio: 
# "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo.
# Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti.
# Si definisca inoltre il metodo inPezziDa() 
# che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o 
# in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo.
# Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza,
# e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() 
# per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito
# con valori differenti e si invochi dettagliPagamento() per ognuno di essi.

# Esempio di output:
# Pagamento in contanti di: €150.00
# 150.00 euro da pagare in contanti con:
# 1 banconota da 100 euro
# 1 banconota da 50 euro

# Pagamento in contanti di: €95.25
# 95.25 euro da pagare in contanti con:
# 1 banconota da 50 euro
# 2 banconote da 20 euro
# 1 banconota da 5 euro
# 1 moneta da 0.2 euro
# 1 moneta da 0.05 euro

# Pagamento di: €200.00 effettuato con la carta di credito
# Nome sulla carta: Mario Rossi
# Data di scadenza: 12/24
# Numero della carta: 1234567890123456

# Pagamento di: €500.00 effettuato con la carta di credito
# Nome sulla carta: Luigi Bianchi
# Data di scadenza: 01/25
# Numero della carta: 6543210987654321




class Pagamento:
    def __init__(self):
        self.__importo = 0.0
        
    def set_importo(self, importo):
        self.__importo = importo

    def get_importo(self):
        return self.__importo
    def dettagliPagamento(self):
        return f'Pagamento in contanti: {self.__importo}'    

class PagamentoContanti(Pagamento):
    def __init__(self, importo: float):
        super().__init__()
        self.set_importo(importo)
       
        
    
    def dettagliPagamento(self):
        return f'Pagamento in contanti: {self.get_importo():.2f}'            
    
    def inPezziDa(self):
        pezzi = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]
        pezzoni = []
        total = self.get_importo()
        for x in pezzi:
            if total >= x:
                numero_pezzi = round(total / x)
                total -= x * numero_pezzi
                total = round(total, 2)
                pezzoni.append((x, numero_pezzi))
        return pezzoni
    
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome, dataScadenza, numeroCarta):
        super().__init__()
        self.__nome = nome
        self.__dataScadenza = dataScadenza
        self.__numeroCarta = numeroCarta
    def dettagliPagamento(self):
        return f'Pagamento di: {self.get_importo():.2f} effettuato con la carta di credito\nNome sulla carta: {self.__nome}\n Data di scadenza: {self.__dataScadenza}\nNumero della carta: {self.__numeroCarta}'
    
        
    
    
pagamento1 = PagamentoContanti(2001.30)
print(pagamento1.dettagliPagamento())
print(pagamento1.inPezziDa())

pagamento2 = PagamentoContanti(100)
print(pagamento2.dettagliPagamento())
print(pagamento2.inPezziDa())


pagamento3 = PagamentoCartaDiCredito("Angelo Locarini","11/69", 123432103)
pagamento3.set_importo(50000890890.99)
print(pagamento3.dettagliPagamento())






# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito
# con valori differenti e si invochi dettagliPagamento() per ognuno di essi.



