from typing import Any, Optional

class Game:
    def __init__(self, location: str, health: int, inventory: list[str], quest_progress: dict[str, str]):
        self.location = location
        self.health = health
        self.inventory = inventory
        self.quest_progress = quest_progress

    def create_memento(self, full: bool) -> 'GameMemento':
        if full:
            state_full: dict[str, Any] = {
                'location': self.location,
                'health': self.health,
                'inventory': self.inventory,
                'quest_progress': self.quest_progress
            }
            return GameMemento(state_full)
        else:
            state_partial: dict[str, Any] = {
                'inventory': self.inventory,
                'quest_progress': self.quest_progress
            }
            return GameMemento(state_partial)

    def restore(self, memento: 'GameMemento') -> None:
        if memento is None:
            return
        state = memento.get_state()
        for key, value in state.items():
            setattr(self, key, value)


class GameMemento:
    def __init__(self, state: dict[str, Any]):
        self._state = state

    def get_state(self) -> dict[str, Any]:
        return self._state


class GameCaretaker:
    def __init__(self, branches: dict[str, list['GameMemento']]):
        self._branches: dict[str, list['GameMemento']] = {}

    def save_memento(self, branch_name: str, memento: 'GameMemento') -> None:
        if branch_name not in self._branches:
            self._branches[branch_name] = []
        self._branches[branch_name].append(memento)

    def get_memento(self, branch_name: str, index: int = -1) -> Optional['GameMemento']:
        if branch_name not in self._branches:
            return None
        return self._branches[branch_name][index]

    def pop_memento(self, branch_name: str) -> Optional['GameMemento']:
        if branch_name not in self._branches:
            return None
        self._branches[branch_name].pop()
        return self.get_memento(branch_name, -1)


# --- Creazione del gioco ---
game = Game(
    location="StanzaIniziale",
    health=100,
    inventory=["Spada"],
    quest_progress={"Tutorial": "in_corso"}
)

# --- Creazione del caretaker ---
caretaker = GameCaretaker({})

# --- 1️⃣ Primo salvataggio completo in "PercorsoBuono" ---
caretaker.save_memento("PercorsoBuono", game.create_memento(full=True))

# --- 2️⃣ Cambiamenti nel gioco ---
game.location = "Foresta"
game.health = 80
game.inventory.append("Pozione")
game.quest_progress["Tutorial"] = "completato"

# --- 3️⃣ Salvataggio parziale in "PercorsoBuono" ---
caretaker.save_memento("PercorsoBuono", game.create_memento(full=False))

# --- 4️⃣ Branch alternativo "PercorsoMalvagio" ---
game.location = "Caverna"
game.health = 50
game.inventory = ["Ascia"]
game.quest_progress = {"Tutorial": "fallito"}

caretaker.save_memento("PercorsoMalvagio", game.create_memento(full=True))

# --- 5️⃣ Restore da branch "PercorsoBuono" (ultimo memento parziale) ---
memento_buono = caretaker.get_memento("PercorsoBuono")
if memento_buono is not None:
    game.restore(memento_buono)

# --- 6️⃣ Restore da branch "PercorsoMalvagio" (memento completo) ---
memento_malvagio = caretaker.get_memento("PercorsoMalvagio")
if memento_malvagio is not None:
    game.restore(memento_malvagio)

# --- 7️⃣ Test undo sul branch "PercorsoBuono" ---
caretaker.pop_memento("PercorsoBuono")
undo_memento = caretaker.get_memento("PercorsoBuono")
if undo_memento is not None:
    game.restore(undo_memento)
