#Menager applicativo
from esCourierLite import Cliente, Corriere, Spedizione, Punto, DatiCliente

class CourierManager:
    def __init__(self):
        self._contatore_spedizioni: int = 0
        self._clienti = {}
        self._corrieri = {}
        self._spedizioni = {}

    def registra_Cliente(self, dc: DatiCliente) -> Cliente:
        if dc["id_client"] in self._clienti:
            return self._clienti[dc["id_client"]]
    
        cliente = Cliente(dc["id_client"], dc["nome"], dc["email"])
        self._clienti[dc["id_client"]] = cliente
        return cliente


    def registra_corriere(self, id_persona: str, nome: str, posizione: 'Punto', velocita_kmh: float) -> 'Corriere':
        if id_persona in self._corrieri:
            return self._corrieri[id_persona]
        corriere = Corriere(id_persona, nome, posizione, velocita_kmh)
        self._corrieri[id_persona] = corriere
        return corriere

    def crea_spedizione(self, ordine: 'DatiOrdine', cliente_id: str) -> 'Spedizione':
        if cliente_id not in self._clienti:
            raise ValueError("Il cliente non è presente")

        cliente = self._clienti[cliente_id]
        self._contatore_spedizioni += 1

        codice_spedizione = f"SPED{self._contatore_spedizioni}"

        spedizione = Spedizione(ordine, cliente, corriere=None)

        self._spedizioni[codice_spedizione] = spedizione

        return spedizione

    def assegna_spedizione(self, codice_spedizione: str, id_corriere: str) -> None:
        if codice_spedizione not in self._spedizioni:
            raise ValueError("Il seguente codice non è presente!!")
        if id_corriere not in self._corrieri:
            raise ValueError("Il seguente corriere non è presente!!")
            
        spedizione = self._spedizioni[codice_spedizione]
        
        corriere = self._corrieri[id_corriere]
        
        spedizione.assegna(corriere)

    def move_corriere(self, id_corriere: str, nuova: Punto) -> None:
        if id_corriere not in self._corrieri:
            raise ValueError("Il seguente corriere non è presente!!")
        corriere = self._corrieri[id_corriere]
        corriere.posizione = nuova
        
    
    def stima_tempo(self, codice: str) -> float:
        if codice not in self._spedizioni:
            raise ValueError("La seguente spedizione non è presente!!")
        spedizione = self._spedizioni[codice]
        if spedizione._corriere is None:
            raise ValueError("A seguente spedizione non è stao assegnato il corriere!!")
        distanza: float = spedizione.distanza_residua()
        
        velocita: float = spedizione._corriere._velocita
        
        if velocita <= 0:
            raise ValueError("La velocita deve essere maggiore di 0")
        
        tempo = distanza / velocita
        
        return tempo
        
    
    def __repr__(self):
        return f"Cliente: {len(self._clienti)}, corriere = {len(self._corrieri)}, spedizione = {len(self._spedizioni)}"
    
    def __str__(self):
        clienti_str = ",".join(str(cliente) for cliente in self._clienti)
        corrieri_str = ",".join(str(corriere) for corriere in self._corrieri)
        spedizioni_str = ",".join(str(spedizione) for spedizione in self._spedizioni)
        
        result: str = (
            f"Clienti: {clienti_str}\t"
            f"Corrieri: {corrieri_str}\t"
            f"Spedizioni: {spedizioni_str}\t"
        )
        
        return result    