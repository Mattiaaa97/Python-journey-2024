print("Esercitazione")

#Esercizio 1 - 2
class RangeStart:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.cont = self.a
    
    def __iter__(self):
        return RangeStart(self.a, self.b)
    
    def __next__(self) -> int:
        if self.cont >= self.b:
            raise StopIteration
        c: int = self.cont
        self.cont += 1
        return c

#Esercizio 3
class SequenceView:
    def __init__(self, seq: str):
        self.seq = seq
        
    def __iter__(self):
        return Forward(self.seq)
    
    def __reversed__(self):
        return Backward(self.seq)

class Forward:
    def __init__(self, seq: str):
        self.seq = seq
        self.contt = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> str:
        if self.contt >= len(self.seq):
            raise StopIteration
        todo: int = self.seq[self.contt]
        self.contt += 1
        return todo

class Backward:
    def __init__(self, seq: str):
        self.seq = seq
        self.co = len(self.seq) - 1
    
    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        if self.co < 0:
            raise StopIteration
        todo1: int = self.seq[self.co]
        self.co -= 1
        return todo1

#Esercizio 4
class Bag:
    def __init__(self, s: list[str]):
        self.s = s
        self.modcount: int = 0
    
    def add(self, stri: str):
        self.s.append(stri)
        self.modcount += 1
    
    def remove_one(self, stri: str):
        if stri in self.s:
            self.s.remove(stri)
            self.modcount += 1
    
    def __iter__(self):
        return BagIterator(self)

class BagIterator:
    def __init__(self, bag: Bag):
        self.bag = bag
        self.modcount2 = bag.modcount
        self.contatore: int = 0
        
 
    def __iter__(self):
        return self
        
    def __next__(self) -> str:
       if self.modcount2 != self.bag.modcount:
           raise RuntimeError("La collezione è stata modificata durante l'iterazione")
       if self.contatore >= len(self.bag.s):
           raise StopIteration
       risultato = self.bag.s[self.contatore]
       self.contatore += 1 
       return risultato

#Esercizio 5
from collections.abc import Iterable

class RoundRobin:
    def __init__(self, *iterable: Iterable):
        self.iterators = [iter(it) for it in iterable]
        self.tot: int = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.iterators:
            raise StopIteration

        tent: int = 0
        if self.tot >= len(self.iterators):
            self.tot = 0
        
        while tent < len(self.iterators):            
            try:
                val = next(self.iterators[self.tot])
                self.tot += 1
                if self.tot == len(self.iterators):
                    self.tot = 0
                return val
            except StopIteration as e:
                print("Non è presente")
                self.iterators.pop(self.tot)
                if self.tot == len(self.iterators):
                    self.tot = 0
                tent += 1
        raise StopIteration

#Esercizio 6
class Windowe:
    def __init__(self, seq: str, k: int):
        self.seq = seq
        self.k = k
        self.conta: int = 0
    
    def __iter__(self):
        return self
        
    def __next__(self) -> str:
        if self.conta + self.k <= len(self.seq):
            riss: str = self.seq[self.conta: self.conta + self.k]
            self.conta += 1
            return riss         
        raise StopIteration 

print("Esercizio 1")
m: RangeStart = RangeStart(1, 3)
for numero in m:
    print(numero)

i: RangeStart = RangeStart(1, 3)
for num in i:
    print(num)

print("Esercizio 2")
u: RangeStart = RangeStart(1, 4)
it1 = iter(u)
it2 = iter(u)

print(next(it1))
print(next(it2))
print(next(it1))
print(next(it2))
print(next(it1))
print(next(it2))

print("Esercizio 3")
st: SequenceView = SequenceView("Bassamarea")
for numer in st:
    print(numer)

for numer in reversed(st):
    print(numer)
#
print("Esercizio 4")           
b: Bag = Bag(["mela", "banana", "arancia"])
b.add("kiwi")
print(b.s)
for frutto in b:
    print(frutto)

print("Esercizio 5")
r = RoundRobin([1, 2, 3], ['a', 'b'], (10, 20, 30, 40))
for el in r:
    print(el)

print("Esercizio 6")
tt: Windowe = Windowe("Francesco", 2)
for i in tt:
    print(i)