#Esercizio 1
dado: str = input('Inserisci la stringa: ')
i: int = 0
cont: int = 0
dado1: str = ""
alpha: str = ""
while i < len(dado):
    if i + 1 < len(dado) and dado[i] == dado[i + 1]:
        if alpha == "":
            alpha = dado[i]
        cont += 1
    else:
        if alpha == "":
            alpha = dado[i]
        cont += 1
        dado1 += alpha + str(cont)
        alpha = ""
        cont = 0
    i += 1
print("Stringa compressa:", dado1)
print(type(dado), type(i), type(cont), type(dado1), type(alpha))
print('*'*100)

#Esercizio 2
stringone: str = input('Inserisci lo strinone: ')
i : int = 0
dec: str = ""
while i < len(stringone):
    lettera = stringone[i]
    if i + 3 < len(stringone) and stringone[i+1:i+4].isdigit():
        numero: int = int(stringone[i+1:i+4])
        i += 4
    elif i + 2 < len(stringone) and stringone[i+1:i+3].isdigit():
        numero: int = int(stringone[i+1:i+3])
        i += 3
    else:
        print('Errato')
        break
    if 0 <= numero <= 127:
        dec += chr(numero)
    else:
        dec += '?'
print(dec)
print(type(stringone), type(i), type(dec), type(numero))
print('*'*100)

#Esercizio 3
s: str = input('Inserisci una stringa palindroma: ')
start: int = 0
palindrona: str = ""
while start < len(s) - 1:
    end: int = start + 1
    while end <= len(s):
        sott: str = s[start:end]
        if sott == sott[::-1] and len(sott) > len(palindrona):
            palindrona = sott
        end += 1
    start += 1
print("Palindroma più lunga trovata:", palindrona)
print(type(s), type(start), type(palindroma), type(end), type(sott))
print('*'*100)

#Esercizio 4
p: str = input('Inserisci una stringa: ')
i: int = 0
k: int = int(input('Il moltiplicatore: '))
vocale: str = 'aeiouAEIOU'
spr: str = ""
while i < len(p):
    if p[i] in vocale:
        spr += p[i] * k   
    else:
        spr += p[i]
    i += 1
print(spr)
print(type(p),type(i), type(k), type(vocale), type(spr))
print('*'*100)

#Esercizio 5
frase: str = input('Inserisci una frase: ')
pattern: str = input('Inserisci un pattern: ')
i: int = 0
cont: int = 0
while i <= len(frase) - len(pattern):
    if frase[i:i+len(pattern)] == pattern:
        i += len(pattern)
        cont += 1
    else:
        i += 1
print(f'Hai trovato {pattern}, {cont} volte')
print(type(frase),type(pattern), type(i), type(cont) )
print('*'*100)
