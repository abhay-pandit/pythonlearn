#rather than in build function we can make our own functions to save code for repeted tasks.

def greet():
    print('hello')
    print("good morning")

def add(x,y):
    c=x+y
    return c

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

greet()
result1,result2= add_sub(5,4)
print(result1,result2)