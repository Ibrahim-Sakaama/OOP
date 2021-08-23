class CompteBancaire:
    def __init__(self,nom="Dupont",solde=1000):
        self.nom=nom
        self.solde=solde
    
    def depot(self,somme):
        self.solde+=somme
        

    def retrait(self,somme):
        self.solde -= somme
         
    
    def affiche(self):
        print("le titulaire "+self.nom+" qui a "+str(self.solde)+"dt dans son compte")
        print("le titulaire {} et le solde est {}".format(self.nom,str(self.solde)))

compte1=CompteBancaire("sam",1000)
compte1.depot(1000)
compte1.affiche()


