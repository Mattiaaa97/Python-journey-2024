#Esercizio 1
class Saluto:
    def __init__(self, saluto: str):
        self._saluto = saluto
        

    def __enter__(self):
        print("Ciaooo")
        return self._saluto
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Arrivederci")
        if exc_type:
            print(f"Eccezione {exc_val}")           
        return False
    
with Saluto("Ciaooo") as messaggio:
    print(messaggio)

print(("*" * 50))

#Esercizio 2
from time import time 

class Timer:
    def __init__(self):
        pass
    
    def __enter__(self):
        self.inizio = time()
        return self.inizio
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fine = time()
        difference: float = self.fine - self.inizio
        print(difference)
        if exc_type:
            print(f"Eccezione {exc_val}")           
        return False
with Timer() as temp:
    print(temp)
    
print(("*" * 50))

#Esercizio 3
class  SafeRun:
    def __init__(self, correre: float):
        self._correre = correre
    
    def __enter__(self):
        return self._correre
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Eccezione {exc_type.__name__}: {exc_val}")
            return True
        return False

with SafeRun(0) as corri:  
    print(4 / corri)
    
print(("*" * 50))

#Esercizio 4
class SommaNumeri:
    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b
        
    def __enter__(self) -> float:
        somma: float = self._a + self._b
        return somma
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fine somma")
        if exc_type:
           print(f"Eccezione {exc_val}")
        return False
        
with SommaNumeri(3.2, 4.1) as risultato:
    print(risultato)

print(("*" * 50))

#Esercizio 5
class A:
    def __init__(self, start: str):
        self._start = start
        
    def __enter__(self):
        return self._start
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self._start)
        if exc_type:
            print(f"Eccezione {exc_val}")
        return False

class B:
    def __init__(self, b_start: str):
        self._b_start = b_start
    
    def __enter__(self):
        return self._b_start
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self._b_start)
        if exc_type:
            print(f"Eccezione {exc_val}")
        return False

with A("olaaaa"), B("fineeeee"):
    print("Dentro il blocco")

with A("muaahhaah"):
    with B("tieeeeee"):
        print("Dentro il blocco")