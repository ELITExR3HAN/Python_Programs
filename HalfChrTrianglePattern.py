n=int(input("Enter the value: "))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k+=1
    print()
