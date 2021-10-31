# the numbers which is only divisible by 1 and themsleves is called prime number

num = 1
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("its prime")
