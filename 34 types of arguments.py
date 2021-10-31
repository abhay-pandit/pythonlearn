
def person(name,age):
    print(name)
    print(age-5)

#person(age=28,name="naveen")

def person(name,age=18):
    print(name)
    print(age-5)

#person("naveen",45)

def sum(a,*b): #*b means b is tuple
    c=a+b
    print(c)

# sum(5,6,34,78) can not add a int and a tuple

def sum(a,*b):
    c=a

    for i in b:
        c=c+i

    print(c)

sum(2,6,34,78)