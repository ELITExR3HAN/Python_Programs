# Program for printing this series->x/1-x^2/2+x^3/3-----x^n/n
n=int(input("Enter how terms you to enter for printing series: "))
x=int(input("ENter the value of x: "))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum-=(x**i)/i
    else:
        sum+=(x**i)/i
print("The sum of series will be:",sum)