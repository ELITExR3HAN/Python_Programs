# Program to find factorial of a number
n=int(input("Enter any number: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("Factorial of a given number",n,"is:",factorial)