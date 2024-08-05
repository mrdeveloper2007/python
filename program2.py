smaller=small=0
for i in range(5):
    n=int(input("enter no :"))
    if i==0:
        smaller=n
    elif i==1:
        if n<smaller:
            small=smaller
            smaller=n
        else:
            small=n
    else:
        if n<smaller:
            small=smaller
            smaller=n
        elif smaller<n<small:
            small=n
        
print("lowest:",smaller)
print("2nd lowest:",small)    