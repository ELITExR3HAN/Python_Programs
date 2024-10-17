n=int(input("For how many digits you want to print fibonacci sequence: "))
a=0
b=1
if n<=0:
    print("Plz enter a positive number!!")
elif n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)