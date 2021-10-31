
def evenodd(lst):

    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst=[1,2,3,56,43,65,8,34,67,435,345,234]

even,odd=evenodd(lst)
print("even number=",even,"odd number=",odd)
print("even:{},odd:{}".format(even,odd))