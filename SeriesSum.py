n=int(input("Enter how many you want to print for series: "))
x=int(input("Enter the value of x: "))
factorial=1
sum=0
for i in range(1,n+1):
    factorial=factorial*i
    if i%2==0:
        sum-=(x**i)/factorial
    else:
        sum+=(x**i)/factorial
print("Sum of series will be :",sum)