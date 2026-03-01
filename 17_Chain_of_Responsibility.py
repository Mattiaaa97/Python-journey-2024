from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class NewYearRequest:
    def __init__(
        self,
        budget_disponibile: float,
        location: str,
        location_pubblica: bool,
        fuochi_artificio: bool,
        numero_invitati: int,
        estintori_disponibili: int,
        permesso_comune: bool
    ):
        self.permesso_comune = permesso_comune
        self.budget_disponibile = budget_disponibile
        self.location = location
        self.location_pubblica = location_pubblica
        self.fuochi_artificio = fuochi_artificio
        self.numero_invitati = numero_invitati
        self.estintori_disponibili = estintori_disponibili


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        ...

    @abstractmethod
    def handle(self, request: NewYearRequest) -> str:
        ...


class BudgetHandler(Handler):
    def __init__(self, soglia_minima: int, handler_successivo: Optional[Handler] = None):
        self.soglia_minima = soglia_minima
        self.handler_successivo = handler_successivo

    def set_next(self, handler: Handler) -> Handler:
        self.handler_successivo = handler
        return handler

    def handle(self, request: NewYearRequest) -> str:
        if request.budget_disponibile < self.soglia_minima:
            return "Richiesta bocciata dal BudgetHandler: budget insufficiente"

        if self.handler_successivo is None:
            return "Richiesta approvata!"

        return self.handler_successivo.handle(request)


class LocationHandler(Handler):
    def __init__(self, handler_successivo: Optional[Handler] = None):
        self.handler_successivo = handler_successivo

    def set_next(self, handler: Handler) -> Handler:
        self.handler_successivo = handler
        return handler

    def handle(self, request: NewYearRequest) -> str:
        if request.location not in ["Casa di Marco", "Villa d’Este", "Piazza del Duomo"]:
            raise ValueError("Location non riconosciuta")

        if self.handler_successivo is None:
            return "Richiesta approvata!"

        return self.handler_successivo.handle(request)


class SecurityHandler(Handler):
    def __init__(self, handler_successivo: Optional[Handler] = None):
        self.handler_successivo = handler_successivo

    def set_next(self, handler: Handler) -> Handler:
        self.handler_successivo = handler
        return handler

    def handle(self, request: NewYearRequest) -> str:
        if request.fuochi_artificio:
            if request.budget_disponibile < 300:
                raise ValueError("Budget insufficiente per i fuochi")
            if request.estintori_disponibili < 3:
                raise ValueError("Estintori insufficienti")

        if self.handler_successivo is None:
            return "Richiesta approvata!"

        return self.handler_successivo.handle(request)


class AuthorityHandler(Handler):
    def __init__(self, handler_successivo: Optional[Handler] = None):
        self.handler_successivo = handler_successivo

    def set_next(self, handler: Handler) -> Handler:
        self.handler_successivo = handler
        return handler

    def handle(self, request: NewYearRequest) -> str:
        if request.fuochi_artificio and request.location_pubblica and not request.permesso_comune:
            raise ValueError("Serve il permesso del comune")

        if self.handler_successivo is None:
            return "Richiesta approvata yuppiiiiiiiiiiiiiiiii!"

        return self.handler_successivo.handle(request)


# COSTRUZIONE CATENA
budget_handler = BudgetHandler(soglia_minima=1000)
location_handler = LocationHandler()
security_handler = SecurityHandler()
authority_handler = AuthorityHandler()

budget_handler.set_next(location_handler)\
              .set_next(security_handler)\
              .set_next(authority_handler)

# TEST REQUEST
request = NewYearRequest(
    budget_disponibile=1500,
    location="Piazza del Duomo",
    location_pubblica=True,
    fuochi_artificio=True,
    numero_invitati=50,
    estintori_disponibili=3,
    permesso_comune=True
)

# ESECUZIONE
try:
    risultato = budget_handler.handle(request)
    print(risultato)
except ValueError as e:
    print(f"Richiesta bocciata: {e}")










