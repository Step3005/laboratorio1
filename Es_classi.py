from hashlib import algorithms_guaranteed


class ContoBancario:
    def __init__(self, nome, cognome, saldo):
        self.nome = nome
        self.cognome = cognome
        self.saldo = float(saldo)

    def stampa_dati(self):
        print("Nome:", self.nome)
        print("Cognome:", self.cognome)
        print("--------------")

    def deposito(self, importo):

        if importo > 0:
            self.saldo += importo
        else:
            print("Importo deve essere positivo!")


    def prelievo(self, importo):
        if  importo > self.saldo:
            print("Attenzione, saldo insufficiente!")

        else:
            self.saldo -= importo

    def restituisco_saldo(self):
        return self.saldo



conto = ContoBancario("Stefano","Alemanno", 5000)
conto.stampa_dati()

conto.deposito(50000)
print(f"Saldo dopo il deposito: {conto.restituisco_saldo()}")

conto.prelievo(3000)
print(f"Saldo dopo il prelievo: {conto.restituisco_saldo()}")

conto.prelievo(100000)
print(f"Saldo dopo il prelievo: {conto.restituisco_saldo()}")