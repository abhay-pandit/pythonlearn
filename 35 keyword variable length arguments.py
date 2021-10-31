def person(name, **data): # ** means passing keyword data in tuple
    print(name)
    for i,j in data.items():
        print(i,j)

person('navin',age=28,city='mumbai',mob=7999907722)