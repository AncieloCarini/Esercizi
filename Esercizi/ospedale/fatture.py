# ### CLASSE: Fattura
# Creare un file chiamato "fatture.py".
# In tale file, creare una classe chiamata Fattura.

# - Definire i seguenti metodi:

#     init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. 
# Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor().
# In caso affermativo assegnare all'attributo fatture (di tipo intero) 
# il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int). 
# In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, 
# come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
#     getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
#     getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
#     addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario,
# richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
#     removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo
# in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture()
# e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".

class Fattura:
    def __init__(self, patient, doctor):
        if self.isAValidDoctor(doctor):
            self.doctor = doctor
            self.patient = patient
            self.fatture = len(patient)
            self.salary = 0
        else:
            self.doctor = None
            self.patient = None
            self.fatture = None
            self.salary = None
        print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        return self.salary
    def getFatture(self):
        self.fatture = len(self.patient)
        return self.fatture
    def addPatient(self, newPatient):
        self.patient.append(newPatient)
        self.getFatture()
        self.salary = self.doctor.parcella * self.fatture
        print(f"Alla lista del Dottor {self.doctor.cognome} è stato aggiunto il paziente {newPatient.codice_identificativo}")
    def removePatient(self, idCode):
        for p in self.patient:
            if p.codice_identificativo == idCode:
                self.patient.remove(p)
                self.getFatture()
                self.salary = self.doctor.parcella * self.fatture
                print(f"Alla lista del Dottor {self.doctor.cognome} è stato rimosso il paziente {idCode}")
