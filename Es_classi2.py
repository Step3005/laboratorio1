class Prodotto:
    def __init__(self, id, nome, prezzo, quantità, categoria):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
        self.quantità = quantità
        self.categoria = categoria

    def stampa(self):
        print("Id:", self.id)
        print("Nome:", self.nome)
        print("Prezzo:", self.prezzo)
        print("Quantità:", self.quantità)
        print("Categoria:", self.categoria)

    def nome_prodotto(self):
        nome = self.nome
        return nome



prodotto1 = Prodotto(101, "Maglietta", 15.90, 20, "Abbigliamento")
prodotto2 = Prodotto(202, "Smartphone", 499.00, 15, "Elettronica")
prodotto3 = Prodotto(303, "Scarpe da ginnastica", 59.90, 32, "Abbigliamento")






class Magazzino:
    def __init__(self):
        self.inventario = []


    def aggiungi_prodotto_magazzino(self, prod):
        self.inventario.append(prod)

    def stampa_magazzino(self):
        for prod in self.inventario:
            prod.stampa()
            print("-------------")

    def rimuovi_prodotto_magazzino(self,x):
        for prod in self.inventario:
            if prod == x:
                self.inventario.remove(prod)


    def cerca_prodotto(self, nome):
        for prod in self.inventario:
            if prod.nome_prodotto() == nome:
                print("prodotto presente")










# prodotto1 = Prodotto(101, "Maglietta", 15.90, 20, "Abbigliamento")
# prodotto2 = Prodotto(202, "Smartphone", 499.00, 15, "Elettronica")
# prodotto3 = Prodotto(303, "Scarpe da ginnastica", 59.90, 32, "Abbigliamento")

m = Magazzino
m.aggiungi_prodotto_magazzino(prodotto1)
m.aggiungi_prodotto_magazzino(prodotto2)
m.aggiungi_prodotto_magazzino(prodotto3)
m.stampa_magazzino()
m.rimuovi_prodotto_magazzino(prodotto1)
m.stampa_magazzino()
m.cerca_prodotto("maglietta")









# prodotto1.stampa_magazzino()
# prodotto2.visulaizza_catalogo()
# prodotto3.visulaizza_catalogo()