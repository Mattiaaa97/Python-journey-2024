#Esercitazione_sabato 28_06
#Esercizio 1
def genera_codice(frase: str) -> str:
    i: int = 0
    new: str = ""

    while i < len(frase):
        c = frase[i].lower()
        if c in "aeiou":
            match c:
                case "a":
                    new += "1"
                case "e":
                    new += "2"
                case "i":
                    new += "3"
                case "o":
                    new += "4"
                case "u":
                   new += "5"
        else:
            new += frase[i]
        i += 1

    return new

frase: str = input("Inserisci una frase: ")
print(genera_codice(frase))
print("*" * 100)

#Esercizio 2
def prima_occorrenza(frase: str, lettera: str) -> int:
    i: int = 0
    while i < len(frase):
        if lettera == frase[i]:
            return i
        i += 1
    return -1

# Input utente
frase: str = input("Inserisci una frase: ")
lettera: str = input("Inserisci una lettera da cercare: ")

print(prima_occorrenza(frase, lettera))
print("*" * 100)

f
#Esercizio 3
def conta_maiuscole_minuscole(frase: str)-> int:
    mai: int = 0
    minu: int = 0
    for lettera in frase:
        if lettera.islower():
            minu += 1   
        elif lettera.isupper():
            mai += 1
    return minu, mai

frase: str = input("Inserisci una frase: ")
lettera: str = input("Inserisci una lettera da cercare: ")
print(conta_maiuscole_minuscole(frase))

#Esercizio 4
def codice_morse(msg: str) -> str:
    vocali: str = "aeiouAEIOU"
    new: str = ""
    for c in msg:
        if c in vocali:
            new += "*"
        elif c.isalpha():
            new += "_"
        else:
            new += c
    return new
msg: str = input("Inserisci una frase: ")
print(codice_morse(msg))

#Esercizio 5
def rimuovi_parole(frase: str, lettera: str):
    i: int = 0
    new: str = ""
    parola: str = ""
    while i < len(frase):
        if frase[i] != " ":
            parola += frase[i]
        else:
            if lettera.lower() not in parola.lower():
                new += parola + " "
            parola: str = ""
        i += 1
    if parola != "" and lettera.lower() not in parola.lower():
        new += parola
    return new.strip()
frase: str = input("Inserisci una frase: ")
lettera: str = input("Inserisci una lettera da cercare: ")
print(rimuovi_parole(frase, lettera))

#Esercizio 6
def conta_sillabe(parola: str) -> int:
    vocali: str = "aeiouAEIOU"
    cont: int = 0
    i: int = 0
    i_sillaba: bool = False
    while i < len(parola):
        if parola[i] in vocali:
            if not i_sillaba:
                cont += 1
                i_sillaba= True
        else:
            i_sillaba = False
        i += 1
    return cont
parola: str = input("Inserisci una parola da cercare: ")
print(conta_sillabe(parola))

#Esercizio 7
def numeri_in_parole(n: int) -> str:
    match n:
        case 1:
            return "s"
        case 2:
            return "c"
        case 3:
            return "i"
        case 4:
            return "v"
        case 5:
            return "o"
        case 6:
            return "l"
        case 7:
            return "a"
        case 8:
            return "r"
        case 9:
            return "e"
        case _:
            return "Errore"

n = int(input("Inserisci un numero da 1 a 9: "))
print(numeri_in_parole(n))

#Esercizio 8
from random import randint
def genera_password_consonanti(lun: int) -> str:
    cons: str = "bcdfghjklmnpqrstvwxyz"
    passworld: str = ""
    i: int = 0
    while i < lun:
        pos: int = randint(0, len(cons) - 1)
        passworld += cons[pos]
        i += 1
    return passworld
lun: int = int(input("Inserisci la lunghezza della password: "))
print(genera_password_consonanti(lun))

#Esercizio 9
def somma_numeri(s: str) -> int:
    i: int = 0
    somma: int = 0
    t: str = ""

    while i < len(s):
        if s[i].isdigit():
            t += s[i]
        else:
            if t != "":
                somma += int(t)
                t = ""
        i += 1
    if t != "":
        somma += int(t)

    return somma

# Esecuzione
s: str = input("Inserisci una stringa: ")
print(somma_numeri(s))

#Esercizio 10
def normalizza_spazi(s: str) -> str:
    r: str = ""
    i: int = 0
    spazio: bool = False
    while i < len(s):
        if s[i] != " ":
           r += s[i]
           spazio = False
        else:
            if not spazio:
                r += " "
                spazio = True
        i += 1
    return r.strip()
s: str = input("Inserisci una stringa: ")
print(normalizza_spazi(s))
