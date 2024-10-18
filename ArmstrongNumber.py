#Program for finding an integer is Armstrong integer or not.
num=int(input("Enter any integer here: "))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10

if sum==num:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

