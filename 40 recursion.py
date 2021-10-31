# import sys
# print(sys.getrecursionlimit())
#
# i=1
# def greet():
#     global i
#     print("hello",i)
#     i+=1
#     greetx ()
#
# greet()

def check(i):
    if i % 2 == 0:
        return  True
    return  False


x = [ 2 , 3 ,54 ,2 ,4 ,2 ,9]

x = filter(check , x)

for i in x:
    print(i)

print(x)

