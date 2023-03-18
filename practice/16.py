# import random 
# a=random.randint(1,601)
# print("id no. ",a,"won the prize")

def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)

print(sum(8))