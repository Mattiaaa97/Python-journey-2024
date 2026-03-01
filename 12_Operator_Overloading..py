#Esercizio 1
class Vettore2d:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vettore2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vettore2d(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vettore2d({self.x}, {self.y})"

dou = Vettore2d(3.4, 6.8)
dou1 = Vettore2d(2.3, 4.3)

print("dou:", dou)
print("dou1:", dou1)

print("Somma:", dou + dou1)
print("Differenza:", dou - dou1)

#Esercizio 2
class NumeroComplesso:
    def __init__(self, re: float, im: float):
        self._re = re
        self._im = im
    
    def __eq__(self, other):
        diff_re: float = abs(self._re - other._re)
        diff_im: float = abs(self._im - other._im)
        tolleranza = 1e-6
        if diff_re < tolleranza and diff_im < tolleranza:
            return True
        else:
            return False

e1: NumeroComplesso = NumeroComplesso(4.2, 4.1)
e2: NumeroComplesso = NumeroComplesso(4.2000002, 4.1000001)
print(e1 == e2)

#Esercizio 3
class Durata:
    def __init__(self, minuti: int):
        self._minuti = minuti
    
    def __lt__(self, other):
        if self._minuti < other._minuti:
            return True
        return False
    
    def __le__(self, other):
        if self._minuti <= other._minuti:
            return True
        return False
        
    def __gt__(self, other):
        if self._minuti > other._minuti:
            return True
        return False
    
    def __ge__(self, other):
        if self._minuti >= other._minuti:
            return True
        return False
    
    def __eq__(self, other):
        if self._minuti == other._minuti:
            return True
        return False

n: Durata= Durata(65)
n1: Durata = Durata(120)
print(n.__lt__(n1))
print(n.__le__(n1))
print(n.__gt__(n1))
print(n.__ge__(n1))
print(n.__eq__(n1))

#Esercizio 4
class Testo:
    def __init__(self, contenuto: str):
        self._contenuto = contenuto
        
    def __mul__(self, other):
        if isinstance(other._contenuto, int):
            return self._contenuto * other._contenuto
    
    def __rmul__(self, other):
        if isinstance(other, Testo) and isinstance(other._contenuto, int):
            return other._contenuto * self._contenuto
        return NotImplementedError

t: Testo = Testo("amio")
t1: Testo = Testo(5)
print(t.__mul__(t1))
print(t.__rmul__(t1))

#Esercizio 5
class Moneta:
    def __init__(self, valore: float, valuta: str):
        self._valore = valore
        self._valuta = valuta
    
    def __add__(self, other):
        if self._valuta == other._valuta:
            return Moneta(self._valore + other._valore, self._valuta)
        raise ValueError("Non ha la stessa valuta!!!")
    
    def __eq__(self, other) -> bool:
        return self._valore == other._valore and self._valuta == self._valuta 
    
    def __str__(self):
        return f"{self._valore} {self._valuta}"

m = Moneta(87.32, "euro")
m1 = Moneta(23.55, "dollaro")
m2 = Moneta(87.32, "euro")

print(m == m2)
print(m == m1)

#Esercizio 6
class Rettangolo:
    def __init__(self, base: float, altezza):
        self._base = base
        self._altezza = altezza
        
    def __eq__(self, other):
        return self._base * self._altezza == other._base * other._altezza
        
    def __lt__(self, other):
        return self._base * self._altezza < other._base * other._altezza
    
    def __str__(self):
        return self._base, self._altezza
    
r: Rettangolo = Rettangolo(2.2, 6.2)
r1: Rettangolo = Rettangolo(3.2, 4.2)

r2: Rettangolo = Rettangolo(2.0, 6.0)
r3: Rettangolo = Rettangolo(3.0, 4.0)

print(r == r1)
print(r2 == r3)

#Esercizio 7
class Registro:
    def __init__(self, studenti: list[str]):
        self._studenti = studenti
    
    def __contains__(self, other):
        if other in self._studenti :
            return True
        return False
    
    def __len__(self):
        return len(self._studenti)
    
    def __repr__(self):
        return f"Registro({self._studenti})"

s: Registro = Registro(["Mattia", "Luca", "Andrea"])

print(repr(s))
print("Luca" in s)
print("Marco" in s)
print(len(s))

#Esercizio 8
class Intervallo:
    def __init__(self, inizio: int, fine: int):
        self._inizio = inizio
        self._fine = fine
        
    def __add__(self, other):
        return Intervallo(self._inizio + other, self._fine + other)
        
    def __radd__ (self, other):
      return Intervallo(other + self._inizio, other + self._fine)
    
    def __eq__ (self, other):
        return self._inizio == other._inizio and self._fine == other._fine
        
    def __repr__(self):
        return f"Intervallo ({self._inizio}, {self._fine})"

print(Intervallo(1, 5) + 3)
print(3 + Intervallo(1, 5))