#you can add extra features to existing function
# here is the code for divison of two numbers in which the result always be more then 1 (means numerator is bigger then denomirator)

# example of decorator

def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div =smart_div(div)

div(4,40)

count = 0
while True:
    print('helllo dudu')
    print(count)
    count+=1



