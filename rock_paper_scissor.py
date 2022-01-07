import random

def GameWin(comp,you):
    if comp==you:
        return None

    if comp=='r' and you=='p':
        return True
    if comp=='p' and you=='r':
        return False

    if comp=='s' and you=='p':
        return False
    if comp=='p' and you=='s':
        return True

    if comp=='s' and you=='r':
        return True
    if comp=='r' and you=='s':
        return False

print("Comp's Turn: ")
comp=print("Comp has choosen")
RandNo=random.randint(1, 3)
if RandNo==1:
    comp='r'
elif RandNo==2:
    comp='p'
elif RandNo==3:
    comp='s'

print("Your Turn: ")
you=input("Enter 'r' for Rock, 'p' for Paper and 's' for Scissor: \n")

print(f"comp has choosen {comp}")
print(f"You have choosen {you}")


Result=GameWin(comp,you)
if Result==None:
    print("Game Draw")
elif Result==True:
    print("You Win")
else:
    print("You Loose")