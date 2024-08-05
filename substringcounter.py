str= input("enter the string:")
substr = input("enter substr:")
length=len(str)
sublen= len(substr)
count=0
start=0
end=length
while True:
    pos=str.find(substr,start,end)
    if pos!=-1:
        count+=1
        start=pos+sublen
    else:
        break
    if start>=length:
        break
print("no of occurence:",count)