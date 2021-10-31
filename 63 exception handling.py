'''
Errors
    Compile time
        syntactical error

    Logical error

    Run time error

        eg. - divid by zero
'''

a = 5
b = 2



try:
    print("resource Open")
    print(a/b)
    k = int(input("enter a number"))
    print(k)

except ZeroDivisionError as e:
    print(" Hey, You cannot divide a Nuber by Zero, e")

except Exception as e:
    print("Invalid Input", e)

finally:
    print(" resource closed")