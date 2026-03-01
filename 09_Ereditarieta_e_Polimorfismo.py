#Esercizio 1
class Animale:
    def verso(self):
        return "..."

class Cane(Animale):
    def verso(self):
        return "bau"

class Gatto(Animale):
    def verso(self):
        return "miao"

ca = Animale()
ca1 = Cane()
ga = Gatto()

print(ca.verso(), ca1.verso(), ga.verso())

#Esercizio 2-3
class Persona:
    def __init__(self, nome: str, eta: int):
        self.__nome = nome
        self.__eta = eta
    def getNome(self):
        return self.__nome
    def getEta(self):
        return self.__eta
class Studente(Persona):
    def __init__(self, nome: str, eta: int, corso: str):
        super(). __init__(nome, eta)
        self.__corso = corso
    def getCorso(self):
        return self.__corso
    def getScheda(self) -> str:
            return f"{self.getNome()} ha {self.getEta()} anni e frequenta il corso di {self.__corso}"
            
    
c: Persona = Studente("anna", 20)
print(c.getNome(), c.getEta())
c1: Studente = Studente("marco", 36, "Informatica")
print(c1.getScheda())

#Esercizio 4
class Veicolo:
    def __init__(self, ruote: int):
        self.__ruote = ruote
    def setNome(self):
        self.__ruote = 4
    def getNome(self):
        return self.__ruote
class Moto(Veicolo):
    def __init__(self):
        super().__init__(6)
    def getRuote(self):
        return self.getNome()
v: Veicolo = Veicolo(2)
print(v.getNome())
m1: Moto = Moto()
print(m1.getRuote())

#Esercizio 5 
class Volante:
    def vola(self):
        return "Sto volando"
class Nuotante:
    def nuota(self):
        return "Sto nuotando"
class Anatra(Nuotante, Volante):
    pass
m1: Anatra = Anatra()
print(m1.nuota())
print(m1.vola())

#Esercizio 6
class Animale:
    def verso(self):
        return "Generale"   
class Cane(Animale):
    def verso(self):
        return "bauuu"
class Gatto(Animale):
    def verso(self):
        return "Miaooooo"
class Pecora(Animale):
    def verso(self):
        return "Beeeeee"
def fai_agire(animale):
        return animale.verso()
pr: Animale = Animale()
print(fai_agire(pr))
g: Gatto = Gatto()
print(fai_agire(g))
p: Cane = Cane()
print(fai_agire(p))
c: Pecora = Pecora()
print(fai_agire(c))

#Esercizio 7
class Veicolo:
    conteggio: int = 0
    def __init__(self):
        Veicolo.conteggio += 1
class Auto(Veicolo):
    def __init__(self):
        super().__init__()

class Moto(Veicolo):
    def __init__(self):
        super().__init__()
        
t1: Veicolo = Veicolo()
c1: Auto = Auto()
c2: Moto  = Moto()
print(Veicolo.conteggio)
    