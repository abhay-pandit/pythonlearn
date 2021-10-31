
class computer: # we have to define 2 things in a class-> attribute ---- variables and behavior ----- methods(functions)

    def __init__(self,cpu,ram):     #atributes(variables)
        self.cpu= cpu
        self.ram= ram

    def config(self):               # behavior(methods)
        print("config is",self.cpu,self.ram)

com1=computer('i5','8gb')
com2=computer('ryzen 3','16gb')

com1.config()
com2.config()