#Warehouse Manage
class Prodotto:
    
    def __init__(self, nome: str, quantita: int, prezzo_unitario: float):
        self._nome = nome
        self._quantita = quantita
        self._prezzo_unitario = prezzo_unitario
    
    def __add__(self, other) -> "Prodotto":
        if self._nome == other._nome and self._prezzo_unitario == other._prezzo_unitario:
            new_quantita = self._quantita + other._quantita
        else:
            raise ValueError("Non si possono sommare i prodotti")
        return Prodotto(self._nome, new_quantita, self._prezzo_unitario)
    
    def __mul__(self, other):
        if not isinstance(other, int) or other <= 0:
            raise ValueError("Il fattore di moltiplicazione deve essere un intero positivo")
        else:
            new_quantita = self._quantita * other
        return Prodotto(self._nome, new_quantita, self._prezzo_unitario)
    
    def __eq__(self, other):
      if not isinstance(other, Prodotto):
          return False
      if self._nome == other._nome and self._quantita == other._quantita and self._prezzo_unitario == other._prezzo_unitario:
          return True
      else:
          return False
          
    def __lt__(self, other):
        self_valore = self._quantita * self._prezzo_unitario
        other_valore = other._quantita * other._prezzo_unitario
        if self_valore <= other_valore:
            return True
        return False
        
    def __gt__(self, other):
        if not isinstance(other, Prodotto):
            raise ValueError("Non è all'interno di prodotto")
        self_valore = self._quantita * self._prezzo_unitario
        other_valore = other._quantita * other._prezzo_unitario
        if self_valore > other_valore:
            return True
        return False
    
    def __str__(self) -> str:
        return f"Prodotto: {self._nome} ({self._quantita} pezzi al prezzo di {self._prezzo_unitario}$)"
   
class Ordine:
    def __init__(self, prodotti: list[Prodotto]):
        self._prodotti = prodotti
    
    def __len__(self) -> int:
        return len(self._prodotti)
        
    def __add__(self, other):
        if not isinstance(other, Ordine):
            raise ValueError("Il presente non è all' interno di ordine")
        prodotti_combianti: dict[str, Prodotto] = {}
        for p in self._prodotti:
            if not p._nome in prodotti_combianti:
                prodotti_combianti[p._nome] = p
            else:
                prodotti_combianti[p._nome] = prodotti_combianti[p._nome] + p

        for p in other._prodotti:
            if not p._nome in prodotti_combianti:
                prodotti_combianti[p._nome] = p
            else:
                prodotti_combianti[p._nome] = prodotti_combianti[p._nome] + p

        lista_combinata = list(prodotti_combianti.values())
        return Ordine(lista_combinata)
                
    def __contains__(self, other):
        for prodotto in self._prodotti:
            if prodotto._nome == other:
                return True
        return False
        
    def totale(self):
        tot: int = 0
        for prodotto in self._prodotti:
            valore_singolo = prodotto._quantita * prodotto._prezzo_unitario
            tot += valore_singolo
        return tot

