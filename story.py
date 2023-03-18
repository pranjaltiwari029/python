def countMEMY():
    
    f = open('stroy.txt','r')
    count=0
    a=f.read()
    b=a.split()
    for i in b:
        if i== "me" or i=="Me" or i=="my" or i=="My":
            count+=1
    print("no. of me and my in file are=",count)

        
countMEMY()
       
        
