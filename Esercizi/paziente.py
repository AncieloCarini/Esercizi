
# ### CLASSE: Paziente
# Creare un file chiamato "paziente.py".
# In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

# Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
# - Definire i seguenti metodi:

#     costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
#     setIdCode(idCode): consente di impostare il codice identificativo del paziente.
#     getidCode(): consente di ritornare il codice identificativo del paziente.
#     patientInfo(): stampa in output le informazioni del paziente in questo modo:

#         "Paziente: {nome} {cognome}
#          ID: {codice identificativo}"


from persona import Persona

class Paziente(Persona):
    def __init__(self, nome, cognome, eta, idCode):
        super().__init__(nome, cognome, eta)
        self.__idCode = idCode
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        
    def setIdCode(self, idCode):
        self.__idCode = idCode
        return self.__idCode
    
    def getIdCode(self):
        pass