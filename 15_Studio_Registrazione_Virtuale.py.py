from abc import ABC, abstractmethod
from random import random
from typing import Protocol, List, Any, Optional

class Audioeffect(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def process(self, samples: List[float]) -> List[float]:
        pass

    def set_params(self, **kwargs: Any) -> None:
        pass

class Gain(Audioeffect):
    def __init__(self, gain: float) -> None:
        self.gain: float = gain

    def name(self) -> str:
        return "Gain"

    def process(self, samples: List[float]) -> List[float]:
        return [s * self.gain for s in samples]

    def set_params(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if key == "gain" and isinstance(value, (int, float)):
                self.gain = float(value)
                return
        raise TypeError(f"{key} is not a valid parameter")

class Limiter(Audioeffect):
    def __init__(self, limit: float) -> None:
        self.limit: float = limit

    def name(self) -> str:
        return "Limite"

    def process(self, samples: List[float]) -> List[float]:
        result: List[float] = []
        for val in samples:
            if val < -self.limit:
                result.append(-self.limit)
            elif val > self.limit:
                result.append(self.limit)
            else:
                result.append(val)
        return result

    def set_params(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if key == "limit" and isinstance(value, (int, float)):
                self.limit = float(value)
                return
        raise ValueError("Valore non valido")

class Delay(Audioeffect):
    def __init__(self, delay: int) -> None:
        self.delay: int = delay

    def name(self) -> str:
        return "Delay"

    def process(self, samples: List[float]) -> List[float]:
        return [0.0] * self.delay + samples

    def set_params(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if key == "delay" and isinstance(value, int):
                self.delay = value
                return
        raise ValueError("Valore non valido")

class Chainable(Protocol):
    def name(self) -> str:
        ...
    def process(self, samples: List[float]) -> List[float]:
        ...
    def set_params(self, **kwargs: Any) -> None:
        ...

class Normalizer(Audioeffect):
    def __init__(self, normalizer: Optional[Chainable], n_lista: List[Chainable]) -> None:
        self.normalizer: Optional[Chainable] = normalizer
        self.n_list: List[Chainable] = n_lista

    def name(self) -> str:
        return "Normalizer"

    def process(self, samples: List[float]) -> List[float]:
        max_val: float = max(abs(s) for s in samples) if samples else 0.0
        if max_val == 0.0:
            return samples.copy()
        factor: float = 1.0 / max_val
        return [s * factor for s in samples]

    def set_params(self, **kwargs: Any) -> None:
        raise NotImplementedError("set_params non implementato per Normalizer")

    def describe(self) -> str:
        return "\n".join(effect.name() for effect in self.n_list)

# Definizione degli effetti
gain: Audioeffect = Gain(2.0)
limiter: Audioeffect = Limiter(0.8)
delay: Audioeffect = Delay(3)
some_normalizer: Chainable = Gain(1.0)  # o qualsiasi altro effetto che implementa Chainable
normalizer: Audioeffect = Normalizer(normalizer=some_normalizer, n_lista=[gain, limiter, delay])

# Lista di campioni casuali
lista_numeri: List[float] = [random() for _ in range(100)]

# Applicazione della catena di effetti
processed: List[float] = lista_numeri[:10]
for effetto in [gain, limiter, delay, normalizer]:
    processed = effetto.process(processed)

# Stampa delle statistiche
print(f"Min: {min(processed)}, Max: {max(processed)}, Media: {sum(processed)/len(processed)}")

# Modifica dei parametri a runtime
limiter.set_params(limit=0.5)
processed = lista_numeri[:10]
for effetto in [gain, limiter, delay, normalizer]:
    processed = effetto.process(processed)

# Stampa delle statistiche dopo la modifica
print(f"Min: {min(processed)}, Max: {max(processed)}, Media: {sum(processed)/len(processed)}")
