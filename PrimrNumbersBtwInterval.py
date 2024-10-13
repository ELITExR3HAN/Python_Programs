lower=int(input("Enter lower value: "))
upper=int(input("Enter upper value: "))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)