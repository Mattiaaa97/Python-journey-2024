##Esercizio 1
#def simmetria(u: set[str], v: set[str]) -> set[str]:
#    m: set[str] = set()
#    vocale: str = "aeiou"
#    for el in u.union(v):
#        if (el in u) != (el in v) and el[0] in vocale:
#            m.add(el)
#    return m
#u: set[str] = {"mamma", "nonno", "addio"}
#v: set[str] = {"ancona", "nonna", "mamma"}
#s: set[str] = simmetria(u, v)
#print(s)
#
##Esercizio 2
#from math import ceil
#def minima(t: list[set[int]]) -> set[int]:
#    c: set[int] = set()
#    soglia: int = ceil(len(t) / 2)
#    for n in (tutti:=set().union(*t)):
#        cont: int = 0
#        for sottoinsieme in t:
#            if n in sottoinsieme:
#                cont += 1
#        if cont >= soglia:
#            c.add(n)        
#    return c
#t: list[set[int]] = [{1, 2}, {2, 3}, {2, 4}]
#y: set[int] = minima(t)
#print(y)
#
##Esercizio 3
#def comp_stringa(shadow: set[str])-> set[str]:
#    return {el for el in shadow if len(el) % 2 != 0 and el == el[::-1]}
#shadow = {"12321", "radar", "ciao", "Python", "Ciao", "hello world"}
#s_sha: set[str] = comp_stringa(shadow)
#print(s_sha)
#
##Esercizio 4
#def parole_nvolta(l: str, f: str) -> set[str]:
#    vocali: str = "aeiou"
#    l_set: set[str] = set(l)
#    f_set: set[str] = set(f)
#    return {el for el in l_set.intersection(f_set) if el.islower() and el in vocali}
#l = "massimo"
#f = "minimo"
#c: set[str] = parole_nvolta(l, f)
#print(c)
#
##Esercizio 5
#def only_num(arg: list[set[int]]) -> set[int]:
#    c: set[int] = set()
#    for el in arg:
#        for num in el:
#            if num % 7 == 0 or str(num)[-1] == "7":
#                c.add(num)
#    return c
#arg: list[set[int]] = [{1, 7, 14}, {27, 30}, {70, 107}]
#f: set[int] = only_num(arg)
#print(f)
#
##Esercizio 6
#print(
#42 -> ✅ #Immutabile int
#
#(1, 2, 3) -> ✅ #Immutabile tuple
#
#(1, [2, 3]) -> ❌ #Mutabile tupla con all'interno list
#
#3.14 -> ✅ -> #Immutabile float
#
#[1, 2, 3] ❌ -> #Mutabile lista 
#)
#
##Esercizio 7
#def num_inter(ll: set[int]) -> set[int]:
#    t: set[int] = set()
#    neg = any(el < 0 for el in ll)
#    if neg:
#        return {abs(el) for el in ll}
#    else:
#        return {el * el for el in ll}
#ll: set[int] = { 1, 2, 3 } #{ -3, -1, 2 }
#print(num_inter(ll))
#
##Esercizio 8
#from typing import Callable
#def fu_vol(set1: set[str], set2: set[str]) -> set[str]:
#    comuni =  set1.intersection(set2)
#    return {el[0].lower() for el in comuni}
#set1: Callable[[], set[str]]= lambda: {"Cane", "Padrona", "Cinema"}
#set2: Callable[[], set[str]]= lambda: {"Topo", "Gatto", "Sedia", "Cinema"}
#c: set[int] = fu_vol(set1(), set2())
#print(c)
#
##Esercizio 9
#def parole_com(stringa: str):
#    def estrai(c: str) -> set[str]:
#        s: set[str] = set()
#        if c == "":
#            return set()
#        else:
#            prima: set[str] = {c[0]}
#            seconda: set[str] = estrai(c[1:])
#            return prima.union(seconda)
#    return estrai(stringa)
#stringa: str = "Bambola"
#print(parole_com(stringa))
#
##Esercizio 10
#def divisore(n: int) -> set[int]:
#    risu: set[int] = set()
#    i: int = 1
#    while i <= n:
#        if n % i == 0:
#            risu.add(i)
#        i += 1
#    return risu
#n: int = 5000
#print(divisore(n))
#
##Esercizio 1.1
#dizionario: dict[str, str | int] = {
#'brand': 'versace',
#'tipologia': 'maglietta',
#'quantità': 50 }
#nuovo_dizionario: dict = dict()
#for (chiave, valore) in dizionario.items():
#    nuovo_dizionario[valore] = chiave
#    print(nuovo_dizionario[valore])
#
##Esercizio 1.2
def analizza(testo: str = "Il sole splende e il cielo è azzurro. Il sole illumina tutto.".title()) -> dict[str, int]:
    i: int = 0
    new: dict[str, str | int]= dict()
    for parola in testo.split():
        parola_clean = parola.lower()
        if parola.lower() in new:
            new[parola_clean] += 1         
        else:
            new[parola_clean] = 1
    return new
v: dict[str, int] = analizza()
print(v)

#Esercizio 1.3
def somma(ll: dict[str, list[int]]) -> dict[str, int]:
    few: dict[str, int] = {}
    for chiave, valore in ll.items():
        somma: int = 0
        for c in valore:
            if not c < 0:
                somma += c
                few[chiave] = somma
    return few
ll: dict[str, list[int]] = {
  "chiave1": [1, 2, 3],
  "chiave2": [4, 5]
}
c: dict[str, int] = somma(ll)
print(c)

#Esercizio 1.4
def dizionario(di: dict[str, dict[str, int | str]]) -> dict[str, dict[str, int | str]]:
    neew: dict[str, dict[str, int | str]] = {}
    for chiave, valore in di.items():
        val_n: dict = {}
        for car in sorted(valore):
            val_n[car] = valore[car]
        neew[chiave] = val_n        
    return neew
di: dict[str, dict[str, int | str]] = {
  "utente1": {"nome": "Anna", "età": 25, "punteggio": 90},
  "utente2": {"nome": "Luca", "età": 30, "punteggio": 80}
}
st: dict[str, dict[str, int | str]] = dizionario(di)
print(st)

#Esercizio 1.5
def moltiplica():
    return lambda s: s * s
def quadrato():
    return lambda b: b * b // 2 
def triangolo():
    return lambda l: l * l * l
def chiama_funzioni(cc: dict[str, Callable], v: int) -> None:
    for chiave, funzione in cc.items():
        ris = funzione(v)
        print(f"{chiave} ({v}) = {ris}")

cc: dict[str, Callable] = {
"moltiplica": moltiplica(),
"quadrato": quadrato(),
"triangolo": triangolo()  
}
st = chiama_funzioni(cc, 4)
print(cc)

#Esercizio 1.6
def unione(f1: dict[str, str | int], f2: dict[str, str | int]) -> dict[str, str | int]:
    t: dict[str, str | int] = {}
    for chiave, valore in f1.items():
        if chiave not in f2:
            t[chiave] = f1[chiave]
        elif isinstance(valore, (int, float)):
            t[chiave] = f1[chiave] + f2[chiave]
    for chiave, valore in f2.items():
        if chiave not in t:
            t[chiave] = valore
    return t
f1 = {
    "nome": "Alice",
    "età": 30,
    "città": "Roma"
}

f2 = {
    "nome": "Alice",
    "età": 32,
    "professione": "Ingegnere"
}
tt: dict[str, str | int] = unione(f1, f2)
print(tt)

#Esercizio 1.7
from typing import Any
def key_order(dizio: dict[str, Any]) -> dict[str, Any]:
    nnew: dict[str, Any] = dict(sorted(dizio.items()))
    return nnew
dizio: dict[str, Any] = {
    "nome": "Luca",
    "età": 30,
    "iscrizione_attiva": True,
    "hobby": ["calcio", "lettura", "musica"],
    "indirizzo": {"città": "Lombardia", "CAP": 25040},
    "saldo": 153.75,
    "note": None
}
fru: dict[str, Any] = key_order(dizio)
print(fru)

#Esercizio 1.8
def classifica(teams: dict[str, int]) -> dict[str, int]:
    st: dict[str, int] = dict(sorted(teams.items(), key = lambda point: point[1], reverse = True))
    return st
teams: dict[str, int] = {
"Rubentus": 23,
"Bilan": 30, 
"Chievo": 13,
"Napoli": 45,
"FC Internazionale": 52
}
mm: dict[str, int] = classifica(teams)
print(mm)
