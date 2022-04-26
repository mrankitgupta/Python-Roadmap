# Constructors
# Default Constructor
class code:
	# default constructor
	def __init__(self):
		self.me = "Ankit Gupta"
	# a method for printing data members
	def print_Geek(self):
		print(self.me)
# creating object of the class
obj = code()
# calling the instance method using the object obj
obj.print_Geek()

# Non-Parameterized Constructor
class Founder:
    # no-argument constructor
    def __init__(self):
        self.name = "Ankit Gupta"
        self.address = "Pune"
    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)
# creating object of the class
f1 = Founder()
# calling the instance method using the object
f1.show()

# Parameterized Constructor
# Example of More than One Constructor in Single class
class Addition:
	first = 0
	second = 0
	answer = 0
	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))
	def calculate(self):
		self.answer = self.first + self.second
# creating object of the class, # this will invoke parameterized constructor
obj = Addition(1000, 2000)
# perform Addition
obj.calculate()
# display result
obj.display()

# Constructor chaining
class Vehicle:
    # Constructor of Vehicle
    def __init__(self, engine):
        print('Inside Vehicle Constructor')
        self.engine = engine
class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed
class Electric_Car(Car):
    # Constructor of Electric Car
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range
# Object of electric car
ev = Electric_Car('1500cc', 240, 750)
print(f'Engine={ev.engine}, Max Speed={ev.max_speed}, Km range={ev.km_range}')

# Destructor
# Python program to illustrate destructor
class Employee:
	# Initializing
	def __init__(self):
		print('Employee created.')
	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')
obj = Employee()
del obj
