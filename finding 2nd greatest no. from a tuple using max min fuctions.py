t=(551,15,551,84,97,44,59)
k=t[0]
for i in t:
    if i>k:
        k=i
ind=t.index(k)
if ind==0:
    k2=t[1]
else:
    k2=t[0]
for i in t:
    if i!=k:
        if i>k2:
            k2=i
print(t)
print('Higest value:',k)
print('Second highest value:',k2)
