# Esercizio 1.1

eta: int = 60
n_preferito: int = 82
n3: int =  8

somma = eta + n_preferito
sottrazine = n3 - eta
moltiplicazione = n3 * n_preferito
divisione = eta / n_preferito
modulo = n_preferito % eta

print('somma:', somma, 'sottrazine:', sottrazine, 'moltiplicazione:', moltiplicazione, 'divisione:', divisione, 'modulo:', modulo)

print(int, type(somma))

# Esercizio 1.2

n1: int = 7
n2: int = 21
n4: int = 6

potenza = 7**n4
divisione = n2 / n1 

print('potenza:', potenza, 'divisione:', divisione)

print(int, type(potenza))

# Esercizio 3

n_pallone: int = 66

n_pallone += 4

print('n_pallone:', n_pallone)

print(int, type(n_pallone))

# Esercizio 4

n_pallone: int = 66

print('n_pallone:', n_pallone)

n_pallone -= 4

print('n_pallone:', n_pallone)

n_pallone *= 9

print('n_pallone:', n_pallone)

n_pallone /= 2

print('n_pallone:', n_pallone) 

n_pallone %= 4

print('n_pallone:', n_pallone)

print(int, type(n_pallone))

# Esercizio 5

n5: int = 90
n6: int = 34

confronto1 = n6 < n5

print('confronto1:', confronto1)

confronto2 = n5 > n6

print('confronto2:', confronto2)

confronto1 <= n6

print('confronto1:', confronto1)

confronto2 >= n5

print('confronto2:', confronto2)

confronto1 == confronto2

print('confronto1:', confronto1)

confronto1 != confronto2

print('confronto1:', confronto1)

print(int, type(n5))

# Esercizio 6

nome: str = 'mattia'
cognome: str = 'Dellanoce'

risultato1= nome == cognome
risultato2= nome != cognome

print('risultato1:', risultato1, 'risultato2:', risultato2)

print(int, type(nome))

# Esercizio 7

n8: int = 59
n9: int = 34

ris1= n8 * n9
ris= n8 + n9

aff_positiva : bool = (ris1 and ris > n8)

print('aff_positiva:', aff_positiva)

print(int, type(n9))

# Esercizio 8

eta : int = 99
eta1: int= 102

ris3 = eta > eta1
ris4 = eta1 == ris3

vera: bool = (ris3 or ris4)

print(vera)

print(int, type(eta))

# Esercizio 9

anni_nonno: int = 85
anni_nonna: int = 90

risultato = anni_nonna < anni_nonno

print(not risultato)

print(int, type(anni_nonna))

# Esercizio 10

num1: int = 5
num2: int = 45

risultato: num1 == num2
risul3= risultato > num2

print(risultato > risultato < num2)

print(int, type(num1))

# Esercizio parte 2

nome: str = input(' ')

sottostringa1: str = nome[0:len/2]
sottostringa2: str = nome[len/2:]

print(sottostringa1)

print(sottostringa2)

print(int, type(sottostringa1))












