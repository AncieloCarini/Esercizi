
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


from ospedale.persona import Persona

class Paziente(Persona):
    def __init__(self, nome, cognome, id_Code):
        super().__init__(nome, cognome)
        #self.__nome = nome
        #self.__cognome = cognome
        #self.età = età

        if isinstance(id_Code, str):
            self.__id_Code = id_Code
        else:
            self.__id_Code = None
        
    def setIdCode(self, id_Code):
        #self.__idCode = idCode
        #return self.__idCode

        if isinstance(id_Code, str):
            self.__id_Code = id_Code
        else:
            self.__id_Code = None

    def getIdCode(self):
        return self.__id_Code
    
    def patientInfo(self):
        print(f"Paziente: {self.getName} {self.getLastname}\n ID: {self.getIdCode}")
