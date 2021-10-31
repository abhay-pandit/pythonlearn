
class computer():

    def __init__(self):
        self.name='abhay'
        self.age= 26

    def update(self):
        self.age= 30

    def compare(self,other):
        if self.age== c2.age:
            return True
        else:
            return False

c1=computer()
c2=computer()

#c2.update()

if c1.compare(c2):
    print('they are same')
else:
    print('they are not same')

'''
size of an object 
    depends on the no of variables and size of each variable
who allocates size to object
    constructor {the () are the constructor}
'''