#Main
from warehouse import Prodotto, Ordine

class SessioneMagazzino:
    
    def __init__(self):
        pass
 
    def __enter__(self):
        print("Inizio sessione magazzino")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fine sessione magazzino")
        if exc_type:
            print(f"Eccezione {exc_val}")           
        return False
        
with SessioneMagazzino():
    p1: Prodotto = Prodotto("Schiuma da barba", 56, 178.00)
    p2: Prodotto = Prodotto("Schiuma da barba", 56, 178.00)
    p3: Prodotto = Prodotto("Arance", 70, 84.00)
    
    p4 = p1 + p2
    p5 = p3 * 2
    
    print(f"Prodotto sommato: {p4}")
    print(f"Prodotto scalato {p5}")
    
    print(f"Prodotto eguale? {p1 == p2}")
    print(f"Prodotto maggiore? {p4 > p3}")
    
    o1: Ordine = Ordine([p1, p3])
    o2: Ordine = Ordine([p2])
    o3: Ordine = o1 + o2
    
    print(f"Ordine totale ${o3.totale()}")
    print(f"'Pane' è all'interno? {'Pane' in o3}")
    print("Fine test")
    
    print("Fine test!!! ✅")