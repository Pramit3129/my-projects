t=(12,3,9,1,7,44)
s=0
l=[]
for i in t:
    if i%2!=0:
        s+=i
        l.append(i)
print(t)
print('The odd values in the tuple are:',l)
print('The sum of all the odd values in the list is:',s)
