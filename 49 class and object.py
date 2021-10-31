
class computer: # we have to define 2 things in a class attribute ---- variables and behavior ----- methods(functions)

    def config(self):
        print("i5,16gb,1TB")

com1=computer() # this is an object
com2=computer()

computer.config(com1)
computer.config(com2)

com1.config() #normally we use this syntex
com2.config()