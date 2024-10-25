n=int(input("Enter how many term you want to enter for printinf the series: "))
x=int(input("Enter the value of x: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    sum+=(x**i)/factorial
print("Sum of series is ",sum)