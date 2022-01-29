n=input("ENTER STRING: ")
cg=input("Enter in which you want to convert: ")
noo=' '
an=ord(cg)
ctn=0
for i in n:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        noo+=cg
        if an==ord(i):
            print('Do nothing with',i)
            pass
        else:
            diff=int(ord(cg))-int(ord(i))
            if diff<0:
                diff=-(diff)
                print('Go back',diff,'steps with',i,'to reach',cg)
            else:
                print("Go forward",diff,"steps with",i," to reach",cg)
                pass
            ctn+=diff
            
    else:
        if i==' ':
            k='_'
        else:
            k=i
        print('Do nothing with',k)
        
        noo+=i
print('Times we have to move:',ctn)
print('string converted to:',noo)
    
