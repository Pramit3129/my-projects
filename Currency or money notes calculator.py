notes = (2000,500,200,100,50,20,10,5,2,1)
print('*'*50)
print("WELCOME TO CURRENCY CALCULATOR")
print('*'*50)
amount = int(input("Enter Amount to be paid : "))
print('-'*50)
print('Required notes amount are as follows:')
for C in notes:
    if amount//C !=0:
        count = amount//C
        print("Note Value of", C,"is required in",count)
        amount = amount%C
print('~'*50)
