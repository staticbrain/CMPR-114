#Challenge Exercise 1

'''
class AnimalType:
    def eats(self):
        print("This animal likes to eat: ")
        
class rabbits(AnimalType): #inherits from AnimalType
    def munch(self):
        print("carrots")
        
class birds(rabbits):
    def munch1(self):
        print("seeds")
    
class cows(birds):
    def munch2(self):
        print("grass")

RabbitObject = rabbits()
RabbitObject.eats() 
RabbitObject.munch()

print("\n")

#inherits from two classes
BirdObject = AnimalType()
BirdObject = birds()

BirdObject.eats() 
BirdObject.munch1()

print("\n")

CowObject = cows()
CowObject.eats() 
CowObject.munch2()

'''

#Challenge Exercise 2

'''
class person:
    def __init__(self, name, age, address, city, state, zipCode):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        
#inherits from person class
class Student(person):
    def __init__(self, name, age, studentID, GPA, address, city, state, zipCode):
        name = input("Please enter a student's name: ")
        age = input("Please enter their age: ")
        studentID = input("Please enter their Student ID: ")
        GPA = input("Please enter their GPA: ")
        address = input("Please enter their street address: ")
        city = input("Please enter the city in which they live: ")
        state = input("Please enter the state in which they live: ")
        zipCode = input("Please enter their zipcode: ")
        
        #the super keyword calls the super class (person class, passes name, and age)
        super().__init__(name,age, address, city, state, zipCode)
        
        self.studentID = studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name, age, TeacherID, ClassTeaching, address, city, state, zipCode):
        super().__init__(name,age, address, city, state, zipCode)
        
        name = input("Please enter a teacher's name: ")
        age = input("Please enter their age: ")
        TeacherID = input("Please enter their Teacher ID: ")
        ClassTeaching = input("Please enter the name of the course taught: ")
        address = input("Please enter their street address: ")
        city = input("Please enter the city in which they live: ")
        state = input("Please enter the state in which they live: ")
        zipCode = input("Please enter their zipcode: ")
        
        print("\n")

        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching
  
student = Student("Jane Doe", 25, 777, 3.8, "123 Home Road", "Town City", "California", 90001)

print("\n")

print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student ID: ", student.studentID)
print("Student GPA: ", student.GPA)
print("Street Address: ", student.address)
print("City: ", student.city)
print("State: ", student.state)
print("Zip Code: ", student.zipCode)

print("\n")

teacher = Teacher("Ms. Cantor", 47 , 7 , "Python", "000 Home Road", "Town City", "California", 90001)

print("Teacher Name: ", teacher.name)
print("Teacher Age: ", teacher.age)
print("Teacher ID: ", teacher.TeacherID)
print("Teacher Course: ", teacher.ClassTeaching)
print("Street Address: ", teacher.address)
print("City: ", teacher.city)
print("State: ", teacher.state)
print("Zip Code: ", teacher.zipCode)
'''

#Challenge Exercise 3

'''
class Automobiles:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    #these are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    #These are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price


class CarDemo(Automobiles):
    def __init__(self, make, model, mileage, price):
        super().__init__(make, model, mileage, price)


def main():
    used_car1 = CarDemo("Audi", 2022, 45000, 80000.0)
    used_car2 = CarDemo("Honda", 2022, 45000, 80000.0)

    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_mileage())
    print("Price: ", used_car1.get_price())

    print("\n")

    print("Make: ", used_car2.get_make())
    print("Model: ", used_car2.get_model())
    print("Mileage: ", used_car2.get_mileage())
    print("Price: ", used_car2.get_price())

main()

'''

#Challenge Exercise 4

'''
class Automobiles:
    def __init__(self, make, model, mileage, price, doors):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__doors = doors

    #These are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def set_doors(self, doors):
        self.__doors = doors

    #These are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_doors(self):
        return self.__doors

class CarDemo(Automobiles):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price, doors)

def main():
    used_car = CarDemo("Audi", 2022, 45000, 80000.0, 4)
    print("Make: ", used_car.get_make())
    print("Model: ", used_car.get_model())
    print("Mileage: ", used_car.get_mileage())
    print("Price: ", used_car.get_price())
    print("Doors: ", used_car.get_doors())

    new_car = CarDemo("Honda", 2022, 45000, 80000.0, 2)
    print("\nMake: ", new_car.get_make())
    print("Model: ", new_car.get_model())
    print("Mileage: ", new_car.get_mileage())
    print("Price: ", new_car.get_price())
    print("Doors: ", new_car.get_doors())


main()

'''

#Challenge Exercise 5
'''

class Insect:
    def __init__(self, wings, legs):
        self.__wings = wings
        self.__legs = legs

    def set_wings(self, wings):
        self.__wings = wings

    def set_legs(self, legs):
        self.__legs = legs

    def get_wings(self):
        return self.__wings

    def get_legs(self):
        return self.__legs


class Bumblebee(Insect):

    def __init__(self, wings, legs, sting, collect_pollen):
        super().__init__(wings, legs)
        self.__sting = sting
        self.__collect_pollen = collect_pollen

    #mutators
    def set_sting(self, sting):
        self.__sting = sting

    def set_collect_pollen(self, collect_pollen):
        self.__collect_pollen = collect_pollen

    #accessors
    def get_sting(self):
        return self.__sting

    def get_collect_pollen(self):
        return self.__collect_pollen

    #prints information
    def info(self):
        print("\nIn addition to the common Insect characteristics, the bumblebee can: ")

        if self.__sting:
            print("sting")

        if self.__collect_pollen:
            print("collect pollen")


class Grasshopper(Insect):

    def __init__(self, wings, legs, jump, chirp):
        super().__init__(wings, legs)
        self.__jump = jump
        self.__chirp = chirp

    #mutators
    def set_jump(self, jump):
        self.__jump = jump

    def set_chirp(self, chirp):
        self.__chirp = chirp

    #accessors
    def get_jump(self):
        return self.__jump

    def get_chirp(self):
        return self.__chirp

    #prints information
    def info(self):
        print("\nIn addition to the common Insect characteristics, the grasshopper can: ")

        if self.__jump:
            print("jump")

        if self.__chirp:
            print("chirp")


bumblebee = Bumblebee(2, 6, True, True)

print("Bumblebee wings:", bumblebee.get_wings())
print("Bumblebee legs:", bumblebee.get_legs())

bumblebee.info()

print("\n")


grasshopper = Grasshopper(2, 6, True, True)

print("Grasshopper wings:", grasshopper.get_wings())
print("Grasshopper legs:", grasshopper.get_legs())

grasshopper.info()

print("\n")

'''

#Challenge Exercise 6

'''
class Automobiles:

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    #These are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    #These are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

class Truck(Automobiles):

    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)

class SUV(Automobiles):

    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)

class ElectricVehicle(Automobiles):

    def __init__(self, make, model, mileage, price):
        super().__init__(make, model, mileage, price)

def main():

    used_car = Automobiles("Audi", 2022, 45000, 80000.0)
    print("Make: ", used_car.get_make())
    print("Model: ", used_car.get_model())
    print("Mileage: ", used_car.get_mileage())
    print("Price: ", used_car.get_price())

    print("\n")

    used_car1 = Automobiles("Honda", 2022, 45000, 80000.0)
    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_mileage())
    print("Price: ", used_car1.get_price())

    print("\n")

    truck = Truck("Toyota", "Tacoma", 40000, 12000.0)
    print("Make: ", truck.get_make())
    print("Model: ", truck.get_model())
    print("Mileage: ", truck.get_mileage())
    print("Price: ", truck.get_price())

    print("\n")

    suv = SUV("Volvo", "SE", 30000, 18500.0)
    print("Make: ", suv.get_make())
    print("Model: ", suv.get_model())
    print("Mileage: ", suv.get_mileage())
    print("Price: ", suv.get_price())

    print("\n")

    electric_car = ElectricVehicle("Tesla", "Model S", 10000, 80000.0)
    print("Make: ", electric_car.get_make())
    print("Model: ", electric_car.get_model())
    print("Mileage: ", electric_car.get_mileage())
    print("Price: ", electric_car.get_price())

    print("\n")

main()

'''

#Challenge Exercise 7

class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):

    def __init__(self, name, number, shift, hourly_pay_rate):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__hourly_pay_rate = hourly_pay_rate

    #mutators
    def set_shift(self, shift):
        self.__shift = shift

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    #accessors
    def get_shift(self):
        return self.__shift

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


def main():
    name = input("Please enter employee name: ")
    number = input("Please enter employee number: ")
    shift = int(input("Please enter shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Please enter hourly pay rate: "))

    worker = ProductionWorker(name, number, shift, hourly_pay_rate)

    print("\n")

    print("Employee name:", worker.get_name())
    print("Employee number:", worker.get_number())
    print("Shift number:", worker.get_shift())
    print("Hourly pay rate:", worker.get_hourly_pay_rate())

    print("\n")

main()
