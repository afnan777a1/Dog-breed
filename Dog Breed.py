class Dog:

  animal = "Dog"

  def __init__(self, breed, anger, cuteness):
    self.breed = breed
    self.anger = anger
    self.cuteness = cuteness

Rocco = Dog("German Shepherd", 10, 4)
print(f"Dog Breed of Rocco: {Rocco.breed}")
print(f"Anger of Level Rocco: {Rocco.anger}")
print(f"Cuteness of Rocco: {Rocco.cuteness}")
print(f"species of Rocco: {Rocco.animal}")


Lulu = Dog("Poodle", 4, 8)
print(f"Dog Breed of Lulu: {Lulu.breed}")
print(f"Anger of Level Lulu: {Lulu.anger}")
print(f"Cuteness of Lulu: {Lulu.cuteness}")
print(f"species of Lulu: {Lulu.animal}")


Hachi = Dog("Shiba Inu", 6, 8)
print(f"Dog Breed of Hachi: {Hachi.breed}")
print(f"Anger Level of Hachi: {Hachi.anger}")
print(f"Cuteness of Hachi: {Hachi.cuteness}")
print(f"species of Hachi: {Hachi.animal}")


Ringo = Dog("American Bully", 10, 3)
print(f"Dog Breed of Ringo: {Ringo.breed}")
print(f"Anger Level of Ringo: {Ringo.anger}")
print(f"Cuteness of Ringo: {Ringo.cuteness}")
print(f"species of Ringo: {Ringo.animal}")


Duke = Dog("St. Bernard", 7, 10)
print(f"Dog Breed of Duke: {Duke.breed}")
print(f"Anger Level of Duke: {Duke.anger}")
print(f"Cuteness of Duke: {Duke.cuteness}")
print(f"species of Duke: {Duke.animal}")