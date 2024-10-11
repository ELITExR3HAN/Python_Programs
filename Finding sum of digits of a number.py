n=int(input("Enter any three digit number: "))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print("The sum of a given three digit number is",sum)
