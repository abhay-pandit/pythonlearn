#break
av=5 #avialable stock
x=int(input("how many candies you want?"))

i=1
while i<=x:

    if i>av:
        print('out of stock')
        break
    print("candy")
    i=i+1
print("thank you")

#continue

for i in range(1,101):
    if i%3==0:
        continue # continue will skip this statement
    print(i)

#pass
for i in range(1,101):
    if i%2==0:
        pass # pass will pass this statement
    else:
        print(i)