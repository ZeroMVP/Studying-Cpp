class Planet:
    
    def __init__(self, name):
        self.name = name
    
class Eartj(Planet):
    
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number



earth = Eartj("Earth", '5')
print(earth.name)
print(earth.number)
