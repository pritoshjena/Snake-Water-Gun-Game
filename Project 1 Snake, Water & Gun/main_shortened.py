'''
1 for snake 
-1 for water 
0 for gun
'''
import random
print("s for snake\nw for water\ng for gun\n")

computer= random.choice([-1,0,1])
youstr=input("Enter your choice : ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"Snake",-1:"Water",0:"Gun"}

you=youdict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if (computer==you):
    print("Its a draw")

else:
    '''
    if(computer == -1 and you ==1): (computer-you)=-2
        print("You win")
    
    elif (computer==-1 and you==0):(computer-you)=-1
        print("You lose")
    
    elif(computer == 1 and you ==-1): (computer-you)=2
        print("You lose")
    
    elif (computer==1 and you==0):(computer-you)=1
        print("You win")
    
    elif(computer == 0 and you ==-1):(computer-you)=1
        print("You win")
    
    elif (computer==0 and you==1):(computer-you)=-1
        print("You lose")
    
    else:
        print("Something went wrong!")

    The below logic is written on the basis of the value of (computer-you)

    '''

if (((computer-you))==-1 or ((computer-you))==2):
    print("You lose!")
else:
    print("You win!")
    