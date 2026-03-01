#print("Esercitazione")
#import random
#
#def tombola() -> None:
#    sacco = list(range(1,91))
#    estratto: set[int] = set()
#    sacco2 = list(sacco)
#    
#    def genera_riga(sacco: list[int]) -> list[int]:
#        riga: list[int] = [0] * 9
#        for i in range(len(unica)): 
#            for j in range(len(riga[0])):
#                if riga[j]
#        
#                
#        
#        
#    def cartella(sacco: list[int]) -> list[list[int]]:
#        giocatore: list[list[int]] = []
#        while len(giocatore) < 3:
#            riga = genera_riga(sacco.copy())
#            giocatore.append(riga)
#        return giocatore
#    
#    def giocatori(sacco: list) -> list[list[list[int]]]:
#        giocatore1:  list[list[int]] = []
#        sacco3 = list(sacco)
#        while len(giocatore1) < 6:
#            new_cart = cartella(sacco3)
#            if new_cart not in giocatore1:
#                giocatore1.append(new_cart)
#        return giocatore1
#    
#    all_the_fold = giocatori(sacco)
#    
#    while sacco2:
#        indice: int = random.randint(0, len(sacco2) - 1)
#        numero: int = sacco2[indice]
#        estratto.add(numero)
#        sacco2.remove(numero)
#    
#        for giocatore in all_the_fold:
#            for cartella in giocatore:
#                for riga in cartella:
#                    if all(numero in estratto for numero in riga):
#                        print("Hai fatto cinquina complimenti")
#                        return
#    print("Nessuna cinquina trovata")
#
#tombola()

print("Esercitazione")
import random

def tombola() -> None:
    sacco = list(range(1,91))
    random.shuffle(sacco)
    while sacco:
        n = sacco.pop(0)
        print(n)
        
def genera_riga(sacco: list[int]):
    numeri: list = list()
    riga: list[int] = [0] * 9
    
    while len(numeri) < 5:
        n = random.choice(sacco)
        if n not in numeri:
            numeri.append(n)
            sacco.remove(n)
    numeri.sort()
    
    posizioni = list(range(9))
    random.shuffle(posizioni)
    posizioni = posizioni[:5]
    
    for i in range(5):
        riga[posizioni[i]] = numeri[i]
    
    return riga
    
def genera_cartella(sacco: list[int]):
    new_cartella: list[int] = list()
    for i in range(3):
        new_cartella.append(genera_riga(sacco))
    return new_cartella
        
def estrai_numeri(sacco: list[int]) -> int:
    n = sacco.pop()
    print(f"Il numero estratto è: {n}") 
    return n
def segna_numero(cartella: list[list[int]], n: int) -> None:
    for riga in cartella:
        for i in range(len(riga)):
            if riga[i] == n:
                riga[i] = "✅"
            
def controlla_cinquina(cartella: list[list[int]]) -> bool:
    for riga in cartella:
        if riga.count("✅") == 5 :
            print("Cinquina fatta, complimenti!!!!")
            return True
    return False

def gioca():
    lista_cartelle: list[list[list[int]]] = list()
    sacco_cartelle = list(range(1,91))
    random.shuffle(sacco_cartelle)
    numero_giocatori : int = 3
    for _ in range(numero_giocatori):
        lista_cartelle.append(genera_cartella(sacco_cartelle.copy()))

    sacco_estrazioni: list[int] = list(range(1,91))
    random.shuffle(sacco_estrazioni)
    
    while sacco_estrazioni:
        n = estrai_numeri(sacco_estrazioni)
        for cartella in lista_cartelle:
            segna_numero(cartella, n)
            print("Cartella aggiornata:")
            for riga in cartella:
                print(riga)
            if controlla_cinquina(cartella):
                 print("🎉 Grandissimo, hai fatto cinquina!")
                 return
gioca()