'''
Python operators work for built-in classes. But the same operator behaves differently with different types. For example,
the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.

This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.
'''


class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3


s1 = Student(58,69)
s2 = Student(60,65)

s3 = s1 + s2

print(s3.m2)