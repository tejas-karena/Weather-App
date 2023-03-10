import random
def check(comp,user):
    if (comp==user):
        return 0
    elif (comp==0 and user == 1):
        return -1
    elif (comp==1 and user ==2):
        return -1
    elif (comp == 2 and user ==1):
        return -1
    else:
        return 1                
comp = random.randint(0,2)
s=0
c=0
for i in range(3):
 user =int(input(" 0 for Snake, 1 for Water, 2 for Gun\n"))
 score = check(comp,user)
 print("You:",user)
 print("Computer:",comp)
 if(score==0):
     print("Its Draw")
 elif(score==-1):
     print("You Lose")
     c+=1
 else:
     print("You Won")
     s+=1    
print(f"Your Score {s} \nComputer's Score {c}") 
if(s>c):
    print("You Won !!!")            
elif(s==c):
    print("Its Draw")
else:
    print("Computer Won")    