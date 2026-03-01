from abc import ABC, abstractmethod

class Visitatore:
    def __init__(self, ID: int, nome: str, dati_personali: str, storico: list[str], biglietto: 'Biglietto'):
        self.ID = ID
        self.nome = nome
        self.dati_personali = dati_personali
        self.storico = storico
        self.biglietto = biglietto

    def get_ID(self) -> int:
        return self.ID

    def get_nome(self) -> str:
        return self.nome

    def get_dati_personali(self) -> str:
        return self.dati_personali

    def get_storico(self) -> list[str]:
        return self.storico

    def get_biglietto(self) -> 'Biglietto':
        return self.biglietto

class Biglietto(ABC):
    @abstractmethod
    def get_privilegi(self) -> list[str]:
        pass

class BigliettoGiornaliero(Biglietto):
    def get_privilegi(self) -> list[str]:
        return ["Giostra", "Cavallo pazzo", "Gira che vomiti"]

class BigliettoStagionale(Biglietto):
    def get_privilegi(self) -> list[str]:
        return ["Giostra", "Cavallo pazzo", "Gira che vomiti", "Plagliaccio crime", "Il domino"]

class BigliettoPremium(Biglietto):
    def get_privilegi(self) -> list[str]:
        return ["Giostra", "Cavallo pazzo", "Gira che vomiti", "Plagliaccio crime", "Il domino", "La casa delle streghe", "Il labirinto"]

class Attrazione(ABC):
    def __init__(self, ID: int, capacita_massima: int, nome_attrazione: str):
        self.ID = ID
        self.capacita_massima = capacita_massima
        self.nome_attrazione = nome_attrazione
        self.prenotazioni: list['Visitatore'] = []
        self.visitatori_attuali: list['Visitatore'] = []


    @abstractmethod
    def entra(self, visitatore: 'Visitatore') -> None:
        pass

    @abstractmethod
    def get_dettagli(self) -> str:
        pass


class Giostra(Attrazione):
    def __init__(self, ID: int, capacita_massima: int, nome_attrazione: str):
        super().__init__(ID, capacita_massima, nome_attrazione)

    def entra(self, visitatore: 'Visitatore') -> None:
        if self.nome_attrazione in visitatore.biglietto.get_privilegi():
            visitatore.storico.append(self.nome_attrazione)
            if len(self.visitatori_attuali) < self.capacita_massima:
                self.visitatori_attuali.append(visitatore)
            else:
                raise ValueError("Posti attualmente pieni")
        else:
            raise ValueError("Il biglietto non risiede nei privilegi")
        if visitatore in self.prenotazioni:
            self.prenotazioni.remove(visitatore)

    def get_dettagli(self) -> str:
        return f"ID -> {self.ID}, Nome -> {self.nome_attrazione}, Capacità massima -> {self.capacita_massima}, Numero prenotazioini attuali -> {len(self.visitatori_attuali)}"


class GestionieAttrazioni:
    def __init__(self, attrazioni: list[Attrazione], nome_attrazione: str):
        self.attrazioni = attrazioni
        self.nome_attrazione = nome_attrazione

    def entra(self, visitatore: 'Visitatore') -> None:
        for att in self.attrazioni:
            if att.nome_attrazione == self.nome_attrazione:
                if visitatore in att.visitatori_attuali:
                    print(f"E' già all'interno, all'ettrazione della {self.nome_attrazione}")
                else:
                    att.entra(visitatore)

    def get_dettagli(self) -> str:
        return f"Nome attrazione -> {self.nome_attrazione}"

class Prenotazione:
    def __init__(self, ID: str, visitatore: Visitatore, attrazione: Attrazione, stato: str):
        self.ID = ID
        self.visitatore = visitatore
        self.attrazione = attrazione
        self.stato = stato


    def attiva(self) -> str:
        self.stato = "Prenotazione attiva"
        return self.stato

    def cancellata(self) -> str:
        self.stato = "Prenotazione cancellata"
        return self.stato

class GestorePrenotazioni:
    def __init__(self, prenotazioni: list['Prenotazione'], attrazioni: list['Attrazione']):
        self.prenotazioni = prenotazioni
        self.attrazioni = attrazioni

    def prenota(self, visitatore: 'Visitatore', attrazione: 'Attrazione') -> str:
        if attrazione is None or attrazione not in self.attrazioni:
            raise ValueError("Attrazione non presente")

        if visitatore in attrazione.prenotazioni:
            raise ValueError("Visitatore già presente")

        nuovo_ID = f"{visitatore.ID}_{attrazione.ID}"
        nuova_prenotazione = Prenotazione(nuovo_ID, visitatore, attrazione, "Prenotazione attiva")
        self.prenotazioni.append(nuova_prenotazione)

        attrazione.prenotazioni.append(visitatore)

        return f"La prenotazione {nuova_prenotazione.ID} è confermata"

    def cancella_prenotazione(self, prenotazione: 'Prenotazione', visitatore: 'Visitatore') -> str:
        if prenotazione not in self.prenotazioni:
            raise ValueError("Prenotazione non presente")

        self.prenotazioni.remove(prenotazione)
        prenotazione.attrazione.prenotazioni.remove(prenotazione.visitatore)

        prenotazione.cancellata()
        return f"La prenotazione di {prenotazione.visitatore} per {prenotazione.attrazione} è stata cancellata"

# Visitatori
v1 = Visitatore(1, "Mario Rossi", "Dati personali Mario", [], BigliettoGiornaliero())
v2 = Visitatore(2, "Luca Bianchi", "Dati personali Luca", [], BigliettoStagionale())

# Attrazioni
g1 = Giostra(101, 2, "Giostra")
g2 = Giostra(102, 3, "Cavallo pazzo")

# Gestore prenotazioni
gestore = GestorePrenotazioni(prenotazioni=[], attrazioni=[g1, g2])

# Prenotazioni
gestore.prenota(v1, g1)
gestore.prenota(v2, g2)

# ------------------ STAMPE ------------------

print("Prenotazioni attuali:")
for p in gestore.prenotazioni:
    print(f"{p.visitatore.nome} -> {p.attrazione.nome_attrazione}, Stato: {p.stato}")

print("\nDettagli attrazioni:")
for attr in gestore.attrazioni:
    print(attr.get_dettagli())

print("\nStorico visitatori:")
for v in [v1, v2]:
    print(f"{v.nome}: {v.storico}")







