class Personne:
    def __init__(self,nom,prenom,age,moyenne): #constructor
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne
    def Say(self): #methode
        return "Hello "+self.nom+"  "+self.prenom
    
    def Age(self):
        if(self.age>40):
            return "Vielle"
        else:
            return "Jeune"

Personne1=Personne("Jack","yo",50,14)
print(Personne1.Say())
print(Personne1.Age())

Personne2=Personne("Jacques","yyyy",30,13)
print(Personne2.Age())


class Per(Personne):
    def Moy(self):
        if(self.moyenne>10):
            return "success"
        else:
            return "defeat"

Personne3=Per("aaa","bbb",10,14)
print(Personne3.Say())
print(Personne3.Moy())











