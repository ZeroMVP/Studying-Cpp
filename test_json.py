class Pet:
    def __init__(self, name = None):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0} - suka".format(self.name)


dog = Dog("Anton", "Lihtarev")
print(dog.name)
print(dog.say())
print("Giii")
