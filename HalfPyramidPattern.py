n=int(input("Enter how many rows and coloums you want to print in your pattern: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()