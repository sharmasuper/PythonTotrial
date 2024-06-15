class Animal :
    def __init__(self,name,species) :
        self.name = name
        self.species = species
    def show_details(self):
        print(f"Name is : {self.name}")    
        print(f"special : {self.species}")

class Dog(Animal) :
    def __init__(self,name,bread) :
        Animal.__init__(self,name,species="Dog") 
        self.bread = bread

    def show_details(self):
        Animal.show_details(self) 
        print(f" Breed : {self.bread}")

class GoldenRetriever(Dog) :
    def __init__(self,name,color) :
        Dog.__init__(self,name,bread='Golden Retriever') 
        self.color = color

    def show_details(self) :
        Dog.show_details(self) 
        print(f"color : {self.color}")       


o = GoldenRetriever("tonny","Black")
o.show_details() 
print(GoldenRetriever.mro())