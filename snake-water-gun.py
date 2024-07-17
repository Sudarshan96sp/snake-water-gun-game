import random 

computer = random.choice([1,-1,0])
youstr = input("Enter Your Choice : ")
youDict = {"s":1,"w":-1,"g":0}
reverseStr = {1:"snake",-1:"water",0:"gun"}
you = youDict[youstr]
print(f"You Chose : {reverseStr[you]} \n Computer Chose : {reverseStr[computer]}")


if(computer==you):
    print("Match Drawn!")
    
else:
    if(you==0 and computer==-1):
        print("You Lose")
    elif(you==0 and computer==1):
        print("You Win!")
    elif(you==-1 and computer==0):
        print("You Win!")
    elif(you==-1 and computer==1):
        print("You Lose!")
    elif(you==1 and computer==-1):
        print("You Win!") 
    elif(you==1 and computer==0):
        print("You Lose!")
    else:
        print("Something Went Wrong!")