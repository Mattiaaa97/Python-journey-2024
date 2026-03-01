from typing import Callable
from functools import partial
#Esercizio 1
def inverti_segnale(numero: int, operazione: Callable[[int], int]):
    ris = operazione(numero)
    if numero < 0:
        return -ris
    else:
        return ris
ris: Callable[[int], int] = lambda c: c * 5
ris1: Callable[[int], int] = lambda c: c * 9


#Esercizio 2
def crea_ricorda_stringa():
    segreta = ""
    def salva(s):
        nonlocal segreta
        segreta = s
    def inverti():
        return segreta[::-1]
    return salva, inverti
salva, inverti = crea_ricorda_stringa()

#Esercizio 3
def  inquadra_testo(testo: str, bordo_sinistro: str, bordo_destro: str) -> str:
    return f"{bordo_sinistro * 2}{testo}{bordo_destro * 2}"
m1: Callable[[str], str] = partial(inquadra_testo, bordo_sinistro='"', bordo_destro='"')

#Esercizio 4
def  operatore_magico() -> Callable[[int, int, int], int]:
    return lambda a,b,c : (a if a > b or b else b) + c ** 2
r: int = operatore_magico()  
    
#Esercizio 5
def Timer_verbale(prefisso: str, m: str)-> str:
        return f"{prefisso} {m}"
m1: Callable[[str], str] = partial(Timer_verbale, "Tra")
m2: Callable[[str], str] = partial(Timer_verbale, "Fra")
p: str = input("Inserisci qualche parola: ")
p1: str = input("Inserisci qualche parola: ")

#Parte 2
#Esercizio 1
def Access_List_Items(l: list, i: int) -> list:
    if i < 0 or i > len(l):
        return "ERRORE"
    return l[i]
l = ['marmellata', 'mela', 'carne bianca', 'formaggi']

#Esercizio 2
def Change_List_Items(l: list, i: int, n: int) -> list:
    if i < 0 or i > len(l):
        return "ERRORE"
    else:
        l[i] = n
    return l
l = [2, 5, 6, 9, 3, 4]

#Esercizio 3
def Add_List_Items(l: list, s: str) -> list:
    l.append(s)
    return l
l = [" "]

#Esercizio 4
def Remove_List_Items(l: list, i: int) -> list:
    if i < 0 or i > len(l):
        return "ERRORE"
    else:
        del l[i]
        return l
l = [3, 6, 7, 9]

#Parte 3
def Somma_di_una_lista(t: list) -> int:
    if not t:
        return 0
    else:
        return t[0] + Somma_di_una_lista(t[1:])
t = [3, 6, 7, 9, 7, 8, 11]


print("Esercizio 1")
print(inverti_segnale(3, ris))
print(inverti_segnale(-6, ris1))
print('*'*100)

print("Esercizio 2")
salva("Mamma mia")
print(inverti())
print('*'*100)

print("Esercizio 3")
print(m1("Mondoooooo"))
print(m1("Casaaaaaaaa"))
print('*'*100)

print("Esercizio 4")
print(r(4,6,7)) 
print(r(2,6,5))
print('*'*100)

print("Esercizio 5")
print(m1(p))
print(m2(p1))
print('*'*100)

print("Parte 2_Esercizio 1")
print(Access_List_Items(l, 2))
print(Access_List_Items(l, 6))
print('*'*100)

print("Parte 2_Esercizio 2")
print(Change_List_Items(l, 2, 33))
print(Change_List_Items(l, 3, 11))
print('*'*100)

print("Parte 2_Esercizio 3")
print(Add_List_Items(l, "mango"))
print(Add_List_Items(l, "papaia"))
print('*'*100)

print("Parte 2_Esercizio 4")
print(Remove_List_Items(l, 2))
print(Remove_List_Items(l, 3))
print('*'*100)

print("Parte 3")
print(Somma_di_una_lista(t))
print('*'*100)
