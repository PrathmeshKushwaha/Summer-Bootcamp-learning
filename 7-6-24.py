# Introduction to OOP principles in Python

class Employee:
    # Data members (attributes)
    _company_name = "Tech Solutions Inc."  # Class variable (shared among all instances)

    def __init__(self, name, salary):
        self.name = name        # Instance variable
        self._salary = salary   # Instance variable with data hiding (conventionally private)

    # Methods in class
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self._salary}")

    def give_raise(self, amount):
        if amount > 0:
            self._salary += amount
            print(f"{self.name} received a raise of ${amount}. New salary is ${self._salary}.")
        else:
            print("Raise amount must be positive!")

    # Special methods (magic methods)
    def __str__(self):
        return f"Employee({self.name}, ${self._salary})"

    def __del__(self):
        print(f"Employee object for {self.name} is being deleted.")

# Creating objects (instances) of the Employee class
emp1 = Employee("John Doe", 50000)
emp2 = Employee("Jane Smith", 60000)

# Accessing methods
emp1.display_info()
emp2.display_info()

# Giving a raise
emp1.give_raise(5000)
emp2.give_raise(3000)

print(emp1)
print(emp2)

print(f"Company Name: {Employee._company_name}")

# Destructor will be called when the object is deleted or program ends
del emp1
del emp2