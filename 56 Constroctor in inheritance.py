# how constructor behaves

class A:
    def __init__(self):
        print('init of A')

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

a1 = B() # if you created object of sub class it will first try find init of sub class if it is not found then it will call init of super class
print('')

# how to use super() in inheritance

class A:
    def __init__(self):
        print('init of A')

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):

    def __init__(self):
        super().__init__()
        print('init of B')

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

n1= B()

# Method Resolution Order



