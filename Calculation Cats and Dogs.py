'''

Explaination:



Example 1: There is one cat and one dog. The number of legs of these animals on the ground are 8, it can be possible when both cat and dog are standing on the ground.

Example 2: There is one cat and one dog. The number of legs of these animals on the ground are 4, it can be possible if the cat will ride on the dog, so its legs won't be counted by Chef, only the dog's legs will be counted.

Example 3: There is one cat and one dog. The number of legs of these animals are 2, it can not be true at all, Chef might have made some mistake. Hence, the answer is no.

'''
cat=int(input('Enter the no.s of cats: '))
dog=int(input('Enter the no.s of dogs: '))
l_cat=cat*4
l_dog=dog*4
opi=int(input('Enter your calculation: '))
if opi>=(l_cat or l_dog) and opi<=(l_cat+l_dog):
    if opi%4==0:
        print('Yes')
        
    else:
        print('No')
else:
    print('No')
