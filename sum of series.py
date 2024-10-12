#Program for printing this series -> 1+x+x^2+x^3...x^n using for and while loop.

#For loop----------------
x=int(input("Enter the base number: "))
n=int(input("Enter the power: "))
sum1=0
for i in range(n+1):
    sum1=sum1+x**i
    print(x,"^",i,"is",x**i)
print("And the sum of series is: ",sum1)


#While loop------------------
i=0
sum2=0
while i<=n:
    sum2=sum2+x**i
    print(x,"^",i,"is",x**i)
    i+=1
print("And the sum of series is: ",sum2)


