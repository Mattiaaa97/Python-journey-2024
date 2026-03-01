#Esercizio CourierLite
from typing import TypedDict, NotRequired
from typing import NamedTuple
from math import sqrt

class Punto(NamedTuple):
    x: float
    y: float
    def distanza(self, altro: 'Punto') -> float:
        return sqrt((self.x - altro.x) ** 2 + (self.y - altro.y) ** 2)

class DatiCliente(TypedDict):
    id_client: str
    nome: str
    email: str

class Persona:
    def __init__(self, id_persona: str, nome: str):
        self._id_persona = id_persona
        self._nome = nome

    def __str__(self) -> str:
        return f"Sono {self._nome} ed sono identificato con {self._id_persona}"

    def __repr__(self) -> str:
        return f"Persona(id_persona='{self._id_persona}', nome='{self._nome}')"

class Cliente(Persona):
    def __init__(self, id_persona: str, nome: str, email: str):
        super().__init__(id_persona, nome)
        self._email = email

    def __str__(self) -> str:
        return f"Sono {self._nome},id -> {self._id_persona}"

    def __repr__(self) -> str:
        return f"Cliente(id_persona='{self._id_persona}', nome='{self._nome}', email='{self._email}')"

class Corriere(Persona):
    def __init__(self, id_persona: str, nome: str, posizione: Punto, velocita: float):
        super().__init__(id_persona, nome)
        self._velocita = velocita
        self._posizione = posizione

    def muovi_a(self, nuova: Punto) -> None:
        self._posizione = nuova

    def distanza_da(self, p: Punto) -> float:
        return self._posizione.distanza(p)

class Pacco:
    def __init__(self, codice: str, descrizione: str, peso_kg: float):
        self._codice = codice
        self._descrizione = descrizione
        self._peso_kg = peso_kg

    def __str__(self):
        return f"{self._codice}: {self._descrizione} ({self._peso_kg} kg)"

    def __repr__(self):
        return f"Pacco(codice='{self._codice}', descrizione='{self._descrizione}', peso_kg={self._peso_kg})"

class Spedizione:
    def __init__(self, ordine: 'DatiOrdine', cliente: Cliente, corriere: Corriere | None):
        self._ordine = ordine
        self._cliente = cliente
        self._corriere = corriere

    def origine(self) -> Punto:
        return self._ordine['ritiro']

    def destinazione(self) -> Punto:
        return self._ordine['consegna']

    def assegna(self, corriere: Corriere) -> None:
        if self._corriere is not None:
            raise ValueError("Spedizione già assegnata a un corriere")
        self._corriere = corriere

    def distanza_residua(self) -> float:
        if self._corriere is None:
            raise ValueError("Spedizione non ancora assegnata ad un corriere")
        return self._corriere._posizione.distanza(self.destinazione())
