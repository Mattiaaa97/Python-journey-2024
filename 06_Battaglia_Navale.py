#Battaglia navale
def batt_navale(bat: list[list[str]]) -> str:
    n_righe = len(bat)
    n_colonne = len(bat[0])
    tentativi: int = 0
    colpiti: int = 0
    navi_totali: int = 0
    tentativi_max = 25
    for i in range(n_righe):
        for j in range(n_colonne):
            if bat[i][j] == '🚢':
                navi_totali += 1
    while colpiti < navi_totali:
        s = input("Inserisci un valore delle righe: ")
        v = input("Inserisci un valore delle colonne: ")
        if not (s.isnumeric() and v.isnumeric()):
            print("Input non valido! Inserisci un numero intero.")
            continue
        s: int = int(s)
        v: int = int(v)
        if 0 <= s < n_righe and 0 <= v < n_colonne:
            tentativi += 1
            if bat[s][v] == '🚢':
                bat[s][v] = "✅"
                print("Colpito")
                colpiti += 1
            elif bat[s][v] == "✅":
                print('Già colpito!!!')
            else:
                print('🌊', "Mancato")
            print(f"Hai fatto {tentativi} tentativi e ti rimangono {tentativi_max - tentativi} 🚢")
            print(f"Hai ancora {navi_totali - colpiti} navi rimanenti")

            if  tentativi >= tentativi_max:
                print("❌ Troppi tentativi, hai perso! 🦴🦴🦴")
                break
            if colpiti == navi_totali:
                print("🏆 Vittoria, complimenti campione!!!")
                break
    return f"Hai fatto {tentativi} tentativi e hai colpito {colpiti} 🚢"      
            
bat: list[list[str]] = [ 
['🌊', '🚢', '🌊'],
['🚢', '🌊', '🌊'],
['🚢', '🌊', '🚢']               
]
mat = batt_navale(bat)
print(mat)