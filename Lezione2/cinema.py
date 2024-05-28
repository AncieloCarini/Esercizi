
# Sistema di Prenotazione Cinema

# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema.
#  Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
# Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

# Classi:
# - Film: Rappresenta un film con titolo e durata.
# - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
# - Cinema: Gestisce le operazioni legate alla gestione delle sale.


#     Metodi sala:
#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. 
#    Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
# 

#     Metodi cinema:
#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

# Test case:
# - Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.

# - Un cliente sceglie un film e prenota un certo numero di posti.

# - Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.










class Film:
    def __init__(self, titolo_name: str, durata_time: float) -> None:
        self.titolo_name = titolo_name
        self.durata_time = durata_time
        self.__repr__ = f"Film: {self.titolo_name}, Durata: {self.durata_time} minuti"
        self.__str__ = f"Film: {self.titolo_name}, Durata: {self.durata_time} minuti"
    




class Sala:
    def __init__(self, sala_id: int, film: Film, posti_totali: int) -> None:
        self.sala_id = sala_id
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0
        self.posti_disponibili = posti_totali
        
    
    def prenota_posti(self, posti) -> int:
        if self.posti_disponibili > 0:
            self.posti_prenotati += 1
            self.posti_disponibili -= 1
            return f"Prenotazione confermata! Posti disponibili: {self.posti_disponibili}"
        else:
            return "non ci sono più posti prenotabili per questo film."
        
        
    
    def posti_disponibili(self) -> str:
        return f"Posti disponibili: {self.posti_disponibili}"
    


    

    
                                                                        
      
          
class Cinema:
    def __init__(self, sale: list [Sala]) -> None:
    
        self.sale = sale

    
    
    def prenota_film(self, titolo_film, num_posti):
        for sala in self.sale:
            if sala.film.titolo_name == titolo_film:
                return sala.prenota_posti(num_posti)
            return "Film non disponibile"
                




        titolo_film = (len[Sala])
        if titolo_film == 'terminator':
            print(sala1.prenota_posti())
        elif titolo_film == 'matrix':
            print(sala2.prenota_posti())
        elif titolo_film == 'pirati dei caraibi':
            print(sala3.prenota_posti())
        
        num_posti = num_posti
        for _ in range(num_posti):
            print(sala.prenota_posti())
            return f"Prenotazione confermata per il film {titolo_film}!"
        else:
            return "Non ci sono più posti disponibili per questo film."




cinema= Cinema([Sala(1, Film('pirati dei caraibi', '2h32min'),50), Sala(2, Film('terminator', '1h34min'),50), Sala(3, Film('matrix', '2h'),50)]) 
print(cinema.prenota_film('terminator', 50))
print(cinema.prenota_film('matrix', 50))
print(cinema.prenota_film('pirati dei caraibi', 50))
