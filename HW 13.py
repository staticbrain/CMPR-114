#Project 1

'''

class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    
    #mutators
    def set_name(self, name):
        self.__name = name
        
    def set_number(self, number):
        self.__number = number
    
    #accessors
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number

class ShiftSupervisor(Employee):

    def __init__(self, name, number, salary, bonus):
        super().__init__(name, number)
        self.__salary = salary
        self.__bonus = bonus
        
    def set_salary(self, salary):
        self.__salary = salary
        
    def set_bonus(self, bonus):
        self.__bonus = bonus
        
    def get_salary(self):
        return self.__salary
    
    def get_bonus(self):
        return self.__bonus
    
    def calculate_total_pay(self):
        return self.__salary + self.__bonus

def main():

    name = input("Please enter supervisor's name: ")
    number = input("Please enter supervisor's number: ")
    salary = float(input("Please enter supervisor's annual salary: "))
    bonus = float(input("Please enter supervisor's annual bonus: "))

    supervisor = ShiftSupervisor(name, number, salary, bonus)

    print("\n")

    print("Supervisor's Information: ")
    print("Name: ", supervisor.get_name())
    print("Number: ", supervisor.get_number())
    print("Salary: ", supervisor.get_salary())
    print("Bonus: ", supervisor.get_bonus())
    print("Total Pay: ", supervisor.calculate_total_pay())

    print("\n")

main()

'''

#Project 2

class Person:

    def __init__(self, name, address, telephone_number):
        self.__name = name
        self.__address = address
        self.__telephone_number = telephone_number

    #mutators
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone_number(self, telephone_number):
        self.__telephone_number = telephone_number

    #accessors
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone_number(self):
        return self.__telephone_number


class Customer(Person):

    def __init__(self, name, address, telephone_number, customer_number, mailing_list):
        super().__init__(name, address, telephone_number)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list


def main():
    customer1 = Customer("John Doe", "123 Home Road", "555-555-5555", "15", True)

    print("Name: ", customer1.get_name())
    print("Address: ", customer1.get_address())
    print("Telephone Number: ", customer1.get_telephone_number())
    print("Customer Number: ", customer1.get_customer_number())
    print("Wants to be on the mailing list: ", customer1.get_mailing_list())

    print("\n")

main()