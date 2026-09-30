a = int(input("Enter a number :"))
no=a
sum=0
while a>0:
    sum=(sum*10)+a%10
    a=a//10
if no==sum:
    print("palindrome")
else:
    print(" not palindrome")