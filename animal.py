#1. Animal → Dog & Cat
#Base class: Animal
class Animal:
#Attributes: name, species
   def __init__(self,name,species):
       self.name=name
       self.species=species
#Method: make_sound() → print("Generic sound")
   def make_sound(self):
       return "Generic Sound"
#Derived classes:
#Dog: override make_sound() → "Woof!"
class Dog(Animal):
   def __init__(self,name,species):
       super().__init__(name,species)
       self.name=name
   def make_sound(self):
        return "Woof!"
#Cat: override make_sound() → "Meow!"
class Cat(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
        self.name=name
    def make_sound(self):
        return "Meaow"
#📝 Practice: Create objects and call make_sound().
def main():
    dog=Dog("Puppy","Dog")
    print(f"{dog.species} name is {dog.name} make sound {dog.make_sound} ")
    cat=Cat("Kitten","cat")
    print(f"{cat.species} make sound {cat.make_sound} ")

if __name__=="__main__":
    main()