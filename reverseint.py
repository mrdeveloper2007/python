num=int(input("enter number:"))
reverse=0
while num:
    last_digit=int(num%10)
    num=int(num/10)
    reverse=reverse*10 + last_digit
print(reverse)