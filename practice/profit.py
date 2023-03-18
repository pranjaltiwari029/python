item=int(input("enter item"))
price=int(input("enter the amount"))
bill=item*price
print(bill)
if(bill>1000):
    bill=bill-(bill*0.1)
    print(bill,"after discount")
else:
    print(bill)


