t=(12,45,78,63,70,78,44,49,77,89,87)
l=len(t)
if l%2!=0:
    k=(l//2)
    print(t)
    print('The middle element:',t[k])
else:
    print('No middle element found')
