







class Persona:
    def __init__(self, nome:str, cognome:str):
        self.nome = nome
        self.cognome = cognome
        
        if not isinstance(self.nome, str):
            print("Il nome inserito non è una stringa!")
            self.nome = None
        else:
            self.nome = self.nome
            if not isinstance(self.cognome, str):
                print("Il cognome inserito non è una stringa!")
                self.cognome = None
            else:
                self.cognome = self.cognome
                self.età = 0
                
    def setName(self, first_name):
        if not isinstance(first_name, str):
            print("Il nome inserito non è una stringa!")
        else:
            self.nome = first_name
    
    def setLastname(self, last_name):
        if not isinstance(last_name, str):
            print("Il cognome inserito non è una stringa!")
        else:
            self.cognome = last_name
    
    def setAge(self, age):
        if not isinstance(age, int):
            print("L'età deve essere un numero intero!")
        else:
            self.età = age

    def getName(self):
        return self.nome
    def getLastname(self):
        return self.cognome
    def getAge(self):
        return self.età
    def __str__(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}, Età: {self.età}"   
    
    




   

