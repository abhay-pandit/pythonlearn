a=10

def somthing():
    a=15
    print("in function",a)

def somthing():
    global a
    a=15
    print("in function",a)



somthing()

print("outside",a)