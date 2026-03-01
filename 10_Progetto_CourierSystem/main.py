from manager import CourierManager
from esCourierLite import Punto

def main():
    gestore = CourierManager()
    
    gestore.registra_Cliente({'id_client': 'C1', 'nome': 'Cliente1', 'email': 'cliente1@email.com'})
    gestore.registra_Cliente({'id_client': 'C2', 'nome': 'Cliente2', 'email': 'cliente2@email.com'})
    
    gestore.registra_corriere('CR1', 'Corriere1', Punto(0, 0), 50)
    gestore.registra_corriere('CR2', 'Corriere2', Punto(0, 0), 60)
    
    ordine1 = {'ritiro': Punto(0, 0), 'consegna': Punto(100, 0)}
    ordine2 = {'ritiro': Punto(0, 0), 'consegna': Punto(200, 0)}
    
    sped1 = gestore.crea_spedizione(ordine1, 'C1')
    sped2 = gestore.crea_spedizione(ordine2, 'C2')
    
    codice_sped1 = 'SPED1'
    
    gestore.assegna_spedizione(codice_sped1, 'CR1')
    
    tempo_stimato = gestore.stima_tempo(codice_sped1)
    print(f"Tempo stimato spedizione1: {tempo_stimato:.2f} ore")
    
if __name__== "__main__":
    main()
    
