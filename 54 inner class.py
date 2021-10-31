# class inside a class - inner class

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.Laptop = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.Laptop.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('naveen', 2)
s2 = Student('jenny', 3)

s2.show()
