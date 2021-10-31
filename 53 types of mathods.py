class student:

    school = 'eadda'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def ave(self):                                  #instance method (it will work with instance variable)
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getschool(cls):                             #class method (it will work with class variable)
        return cls.school

    @staticmethod
    def info():                                     #anything else is static mathod which dose not effected by any variable
        print("this is student class.. in abc module")

s1 = student(34,47,32)
s2 = student(89,32,12)

print(s1.ave())
print(student.getschool())

student.info()