class Pet:
    """
    Клас домашніх тварин
    """ 
    def __init__(self,name="NoName",type="NoType"):
        self.name=name
        self.type=type

    def __str__(self):
        return f"Pet: {self.type}. It's name: {self.name}"
    
    


pet1=Pet()
print(pet1.name,pet1.type)
pet2=Pet()
print(pet2.name,pet2.type)

pet1.type="cat"
pet1.name="Snigok"
print(pet1.name,pet1.type)
print(pet1)
pet_of_Volodimir=Pet("Sharik","dog")
print(pet_of_Volodimir)
pet_of_Maxim=Pet("Jack","dog")
print(pet_of_Maxim)


        
