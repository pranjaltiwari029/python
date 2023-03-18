def prime(n):
    for i in range(0,n+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    print(i," is not a prime no.")
                    break
                else:
                    print(i,"is a prime number")
                    break

prime(6)                   