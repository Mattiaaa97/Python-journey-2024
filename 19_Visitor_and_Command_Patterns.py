from abc import ABC, abstractmethod

from mypy.dmypy_util import receive

print("###################################Esercizio 1#####################################")
class Forma(ABC):
    @abstractmethod
    def accept(self, visitor: 'AreaVisitor') -> None:
        pass

class Cerchio(Forma):
    def __init__(self, raggio: float) -> None:
        self.raggio = raggio

    def accept(self, visitor: 'AreaVisitor') -> None:
        visitor.visitCerchio(self)

class Rettangolo(Forma):
    def __init__(self, base: float, altezza: float):
        self.base = base
        self.altezza = altezza

    def accept(self, visitor: 'AreaVisitor') -> None:
        visitor.visitRettangolo(self)

    def get_base(self) -> float:
        return self.base

    def get_altezza(self) -> float:
        return self.altezza

class Triangolo(Forma):
    def __init__(self, base: float, altezza: float):
        self.base = base
        self.altezza = altezza

    def accept(self, visitor: 'AreaVisitor') -> None:
        visitor.visitTriangolo(self)

    def get_base(self) -> float:
        return self.base

    def get_altezza(self) -> float:
        return self.altezza

class AreaVisitor(ABC):
    @abstractmethod
    def visitCerchio(self, cerchio: Cerchio) -> float:
        pass
    @abstractmethod
    def visitRettangolo(self, rettangolo: Rettangolo) -> float:
        pass
    @abstractmethod
    def visitTriangolo(self, triangolo: Triangolo) -> float:
        pass

class Area(AreaVisitor):
    def visitCerchio(self, cerchio: Cerchio) -> float:
        area = 3.14 * cerchio.raggio ** 2
        print(f"L'area del cerchio è {area}")
        return area

    def visitRettangolo(self, rettangolo: Rettangolo) -> float:
        area = rettangolo.base * rettangolo.altezza
        print(f"L'area del rettangolo è {area}")
        return area

    def visitTriangolo(self, triangolo: Triangolo) -> float:
        area = triangolo.base * triangolo.altezza / 2
        print(f"L'area del triangolo è {area}")
        return area

cerchio = Cerchio(5)
rettangolo = Rettangolo(4, 3)
triangolo = Triangolo(6, 2)

visitor = Area()

cerchio.accept(visitor)
rettangolo.accept(visitor)
triangolo.accept(visitor)

print("################################Esercizio 2########################################")
from abc import ABC, abstractmethod

class Editor(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

class EditorConcreto:
    def __init__(self):
        self.testo: str = ""

    def aggiungitesto(self, posizione: int, testo: str) -> None:
        prima = self.testo[:posizione]
        dopo = self.testo[posizione:]
        self.testo = prima + testo + dopo

    def rimuovitesto(self, posizione: int, lunghezza: int) -> str:
        testo_rimosso = self.testo[posizione:posizione + lunghezza]
        self.testo = self.testo[:posizione] + self.testo[posizione + lunghezza:]
        return testo_rimosso

class AggiungiTesto(Editor):
    def __init__(self, testo: str, editor: 'EditorConcreto', posizione: int):
        self.testo = testo
        self.editor = editor
        self.posizione = posizione

    def execute(self) -> None:
        self.editor.aggiungitesto(self.posizione, self.testo)

    def undo(self) -> None:
        self.editor.rimuovitesto(self.posizione, len(self.testo))

class RimuoviTesto(Editor):
    def __init__(self, editor: 'EditorConcreto', posizione: int, lunghezza: int):
        self.editor = editor
        self.posizione = posizione
        self.lunghezza = lunghezza
        self.testo_rimosso: str = ""

    def execute(self) -> None:
        self.testo_rimosso = self.editor.rimuovitesto(self.posizione, self.lunghezza)

    def undo(self) -> None:
        self.editor.aggiungitesto(self.posizione, self.testo_rimosso)

class ModificaTesto(Editor):
    def __init__(self, editor: 'EditorConcreto', posizione: int, lunghezza: int, nuovo_testo: str):
        self.editor = editor
        self.posizione = posizione
        self.lunghezza = lunghezza
        self.nuovo_testo = nuovo_testo
        self.vecchio_testo: str = ""

    def execute(self) -> None:
        self.vecchio_testo = self.editor.rimuovitesto(self.posizione, self.lunghezza)
        self.editor.aggiungitesto(self.posizione, self.nuovo_testo)

    def undo(self) -> None:
        self.editor.rimuovitesto(self.posizione, len(self.nuovo_testo))
        self.editor.aggiungitesto(self.posizione, self.vecchio_testo)


editor = EditorConcreto()

cmd1 = AggiungiTesto("Ciao ", editor, posizione=0)
cmd2 = ModificaTesto(editor, posizione=0, lunghezza=5, nuovo_testo="Ciao mondo")
cmd3 = AggiungiTesto("!", editor, posizione=11)

# Esecuzione comandi
cmd1.execute()
print(editor.testo)

cmd2.execute()
print(editor.testo)

cmd3.execute()
print(editor.testo)

# Undo
cmd3.undo()
print(editor.testo)

cmd2.undo()
print(editor.testo)

# Redo
cmd2.execute()
print(editor.testo)

cmd3.execute()
print(editor.testo)

print("################################Esercizio 3########################################")
class PerimetroVisitor(ABC):
    @abstractmethod
    def visitCerchio(self,cerchio: Cerchio) -> float:
        pass
    @abstractmethod
    def visitRettangolo(self, rettangolo: Rettangolo) -> float:
        pass
    @abstractmethod
    def visitTriangolo(self, triangolo: Triangolo) -> float:
        pass

class PerimetroConcreto(PerimetroVisitor):

    def visitCerchio(self, cerchio: Cerchio) -> float:
        return 2 * 3.14 * cerchio.raggio

    def visitRettangolo(self, rettangolo: Rettangolo) -> float:
        return 2 * (rettangolo.altezza + rettangolo.base)

    def visitTriangolo(self, triangolo: Triangolo) -> float:
        return triangolo.l1 + triangolo.l2 + triangolo.l3

class Cerchio:
    def __init__(self, raggio: float):
        self.raggio = raggio

    def accept(self, visitor: PerimetroVisitor) -> float:
        return visitor.visitCerchio(self)


class Rettangolo:
    def __init__(self, base: float, altezza: float):
        self.base = base
        self.altezza = altezza

    def accept(self, visitor: PerimetroVisitor) -> float:
        return visitor.visitRettangolo(self)


class Triangolo:
    def __init__(self, l1: float, l2: float, l3: float):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def accept(self, visitor: PerimetroVisitor) -> float:
        return visitor.visitTriangolo(self)


#Stampe
perimetro_concreto: PerimetroConcreto = PerimetroConcreto()

cerchio = Cerchio(raggio=10)
rettangolo = Rettangolo(base=4, altezza=8)
triangolo = Triangolo(l1=3, l2=4, l3=5)

print("[Il perimetro del CERCHIO] -> ", cerchio.accept(perimetro_concreto))
print("[Il perimetro del RETTANGOLO] -> ", rettangolo.accept(perimetro_concreto))
print("[Il perimetro del TRIANGOLO] -> ", triangolo.accept(perimetro_concreto))

print("################################Esercizio 4########################################")
from abc import ABC, abstractmethod
from typing import Optional, Protocol


# --- Command Pattern ---
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class ApriFileCommand(Command):
    def __init__(self, editor: "Editor") -> None:
        self._editor = editor

    def execute(self) -> None:
        self._editor.apri_file()


class ScriviTestoCommand(Command):
    def __init__(self, editor: "Editor", testo: str) -> None:
        self._editor = editor
        self.testo = testo

    def execute(self) -> None:
        self._editor.scrivi_testo(self.testo)


class SalvaFileCommand(Command):
    def __init__(self, editor: "Editor") -> None:
        self._editor = editor

    def execute(self) -> None:
        self._editor.salva_testo()


class MacroCommand:
    def __init__(self, lista_comandi: Optional[list[Command]] = None) -> None:
        self.lista_comandi = lista_comandi or []

    def add_command(self, command: Command) -> None:
        if command not in self.lista_comandi:
            self.lista_comandi.append(command)
        else:
            print("Comando già presente nella lista!!!")

    def execute(self) -> None:
        for comando in self.lista_comandi:
            comando.execute()


# --- Editor astratto e concreto ---
class Editor(ABC):
    @abstractmethod
    def apri_file(self) -> None:
        pass

    @abstractmethod
    def scrivi_testo(self, testo: str) -> None:
        pass

    @abstractmethod
    def salva_testo(self) -> None:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class EditorConcreto(Editor):
    def apri_file(self) -> None:
        print("File aperto")

    def scrivi_testo(self, testo: str) -> None:
        print(f"Testo scritto: {testo}")

    def salva_testo(self) -> None:
        print("File salvato")

    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


# --- Classi geometriche corrette ---
class Triangolo:
    def __init__(self, l1: float, l2: float, l3: float) -> None:
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def accept(self, visitor: "AreaVisitor") -> float:
        return visitor.visit_triangolo(self)


class Rettangolo:
    def __init__(self, base: float, altezza: float) -> None:
        self.base = base
        self.altezza = altezza

    def accept(self, visitor: "AreaVisitor") -> float:
        return visitor.visit_rettangolo(self)


class Cerchio:
    def __init__(self, raggio: float) -> None:
        self.raggio = raggio

    def accept(self, visitor: "AreaVisitor") -> float:
        return visitor.visit_cerchio(self)


# --- Visitor tipizzato ---
class AreaVisitor(Protocol):
    def visit_triangolo(self, triangolo: Triangolo) -> float:
        ...

    def visit_rettangolo(self, rettangolo: Rettangolo) -> float:
        ...

    def visit_cerchio(self, cerchio: Cerchio) -> float:
        ...


# --- Esempio utilizzo editor e macro ---
editor = EditorConcreto()
macro = MacroCommand()
macro.add_command(ApriFileCommand(editor))
macro.add_command(ScriviTestoCommand(editor, "Ciao mondo"))
macro.add_command(SalvaFileCommand(editor))
macro.execute()











