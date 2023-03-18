def p(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*p(a,b-1)

print(p(6,2))