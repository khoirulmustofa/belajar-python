class Person:
    def __init__(self, name, age, jalan):
        self.name = name
        self.age = age
        self.jalan = jalan

    def say_hello(self):
        print("Hello, my name is {} and I am {} years old".format(self.name, self.age))
    
    def berjalan(self):
        print(f"Berjalan : {self.jalan} ")

print("Hallo OOP")

oPerson = Person("Budi",19,"Maju")
oPerson.say_hello()
oPerson.berjalan()

php artisan serve