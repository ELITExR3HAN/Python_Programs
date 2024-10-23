s=list(input("Enter any string: "))
for i in s:
    if i in "AEIOUaeiou":
        print("*",end="")
    else:
        print(i,end="")


