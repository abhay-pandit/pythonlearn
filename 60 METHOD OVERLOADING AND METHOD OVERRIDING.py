'''
Methods in Python can be called with zero, one, or more parameters. This process of calling the same method in different
ways is called method overloading. It is one of the important concepts in OOP. Two methods cannot have the same name in
Python; hence method overloading is a feature that allows the same operator to have different meanings.
'''

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a + b + c

        elif a!=None and b!=None:
            s = a + b

        else:
            s = a

        return s


s1 = Student(58,69)

print(s1.sum(7))

'''
Method overriding is a concept of object oriented programming that allows us to change the implementation of a function in the child class 
that is defined in the parent class. It is the ability of a child class to change the implementation of any method which is already provided by one of its parent class(ancestors).

Following conditions must be met for overriding a function:

Inheritance should be there. Function overriding cannot be done within a class. We need to derive a child class from a parent class.
The function that is redefined in the child class should have the same signature as in the parent class i.e. same number of parameters.
'''

class A:

    def show(self):             #overriden method
        print ('in A show')
    def abc(self):              #inherited method
        print("i am inherited method")
class B(A):

    def show(self):             #overriding method
        print('in B show')

a1 = B()
a1.show()