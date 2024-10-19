lower=int(input("Enter lower value: "))
upper=int(input("Enter upper value: "))

for num in range(lower,upper+1):
    sum=0
    temp=num
    order=len(str(num))

    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if sum==num:
        print(num,"is an armstrong number")
    else:
        print(num,"is not an armstrong number")
