import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self. carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(self, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count

class Truck(CarBase):
    def __init__(self,brand, photo_file_name, carrying, body_whl):
        pass

class SpecMachine(CarBase):
    def __init__(self,brand, photo_file_name, carrying, extra):
        pass

def get_car_list(csv_filename):
    car_list = []
    return car_list


def readop(csv_filename):
    s = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter = ';')
        next(reader)
        for row in reader:
           print(str(row))
           if(str(row[0]) == 'car'):
               am = Car(row[1],'.jpg','4','4')
               s.append(a)
    return s



#def ell(strin):
   # print(strin)


#ell('adadad')
a = 'carnames.csv'
q = readop(a)
machine = q[0]
print(machine.brand)
car = CarBase("Maserati", "mainstream.ff", "2.5")
m = car.get_photo_file_ext()
print(m)
