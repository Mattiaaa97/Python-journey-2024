# Esercizio 1
o: str = 'Fantastico'
print(o.replace('t', 'c', 3))
print(type(o))

# Esercizio 2
cit: str = input('Dove sei nato? ')
abitanti: int = int(input('Ha : '))
fr: str =( "La citta di {} ha {} abitanti").format(cit, abitanti)
print(fr)
print(type(cit), type(abitanti), type(fr))

#Esercizio 3
f: int = int(input('Inserisci un intero : '))
c: float = float(input('Inserisci un decimale : '))
tpr: str = ("Il numero intero è {} e il numero decimale è {:.2f}").format(f, c)
print(tpr)
print(type(f), type(c), type(tpr))

 Esercizio 4
b: str = input('Inserisci una frase: ').lower()
voc : int = (b.count('a') +
    b.count('e') +
    b.count('i') +
    b.count('o') +
    b.count('u'))
print(voc)
print(type(b), type(voc))

# Esercizio 5
b: str = input('Inserisci una frase: ').lower()
tip: int = b.replace('a', ' ').replace('e', ' ').replace('i', ' ').replace('o', ' ').replace('u', ' ')
print(tip)
print(type(b), type(voc))   

 Esercizio 6
b: str = input('Inserisci una frase: ').title()
b : int = b.replace('e', '@').replace('o', '@')
print(b) 
print(type(b))

Esercizio 2.1
s: int =int(input('inserisci un numero da 1 a 7: '))
print(type(s))
match s:
    case 1: 
        print('I')
        print(type(s))
    case 2: 
        print('II')
        print(type(s))
    case 3: 
        print('III')
        print(type(s))
    case 4: 
        print('IV')
        print(type(s))
    case 5: 
        print('V')
        print(type(s))
    case 6: 
        print('VI')
        print(type(s))
    case 7: 
        print('VII')
        print(type(s))
    case _:
        print('Non valido')
       
Esercizio 1.2
from random import randint
utente: int = int(input('inserisci un numero: '))
dado1: int = randint(1,10)
print(type(utente), type(dado1))
if dado1 > 10:
    print(utente, 'Troppo alto')
    print(type(utente))
elif dado1 < 0:
    print(utente, 'Troppo basso')
    print(type(utente))
else:
    print(utente, 'Esatto')

 Esercizio 1.3
utente: str = input('inserisci un personaggio: ')
print(type(utente))
match utente: 
    case "guerriero":
        print(utente, 'Dono del fuoco')
        print(type(utente))
    case "mago":
        print(utente, 'Poteri sovraumani')
        print(type(utente))
    case "arciere":
        print(utente, 'Dono della invisibilita')
        print(type(utente))
    case _:
        print(utente, 'Personaggio non disponibile')

Esercizio 1.4/5
utente1: int = int(input('inserisci un numero: '))
utente2: int = int(input('inserisci un numero: '))
print(type(utente1), type(utente2))
if utente1 == utente2:
    print('Sono uguali')
    print(type(utente1), type(utente2))
else:
    print('Sono diversi')

 Esercizio 1.6
tente1: int = int(input('inserisci un numero: '))
tente2: int = int(input('inserisci un numero: '))
tente3: int = int(input('inserisci un numero: '))
rint(type(utente1), type(utente2), type(utente3))
f utente1 > utente2 and utente3:
   print(utente1, 'E maggiore')
   print(type(utente1), type(utente2), type(utente3))
lif utente2 > utente2 and utente3:
   print(utente2, 'E maggiore')
   print(type(utente1), type(utente2), type(utente3))
lif utente3 > utente1 and utente2:
   print(utente3, 'E maggiore')
   print(type(utente1), type(utente2), type(utente3))
lse:
   print(utente1, utente2, utente3, 'Sono uguali')

 Esercizio 1.7
utente1: int = input('inserisci un numero: ')
utente2: int = input('inserisci un numero: ')
utente3: int = input('inserisci un numero: ')
fr: int = [utente1, utente2, utente3]
fr.sort()
print(fr)
print(type(utente1), type(utente2), type(utente3))

 Esercizio 1.8
nno: int = int(input('Inserisci un anno: '))
rint(type(anno))
f (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
   print(anno, 'E bisestile')
   print(type(anno))
lse:
   print(anno, 'Non e bisestile')

 Esercizio 1.9
lato: int = 8
lato1: int = 9
lato3: int = 10
print(type(lato), type(lato1), type(lato3))
if (lato + lato1 > lato3) and (lato + lato3 > lato1) and (lato1 + lato3 > lato):
    print('Rappresenta i lati totali')
    print(type(lato), type(lato1), type(lato3))
else:
     print(' Non rappresenta i lati totali')

# Esercizio 1.10
a: int = 8
b: int = 10
c: int = 8
print(type(a), type(b), type(c))
if a != b != c:
    print('Triangolo scaleno')
    print(type(a), type(b), type(c))
elif a == b != c:
    print('triangolo isoscele')
    print(type(a), type(b), type(c))
else:
    print('triangolo equilatero')