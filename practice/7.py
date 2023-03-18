def check(n):
    u=0
    l=0
    for i in n:
        if i.islower():
            l=l+1
        elif i.isupper():
            u=u+1
    print(u)
    print(l)

check("Pranjal")
    