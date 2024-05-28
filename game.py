import random
def computer_guess(a,b):
     return random.randint(a,b)

    
def again(computer):
   
    user_input=int(input("Enter your guess:"))
    result(computer,user_input)
    
def result(computer,user_input):
    
    if (computer==user_input):
        print(" Congratultions!!your guess is correct:👏🎉")
        print()
        print("***Enter 'yes' continue and 'no'to exit***")
        User_response=input()
        User_response=User_response.lower()
        if(User_response=='yes'):
            beginning()
        else:
            exit()
            
    elif(computer<user_input):
        print("Opps!!🤯🤯your guess is more than computer's guess")  
        again(computer)
            
    elif(computer>user_input):
        print("Oops!!🤯🤯your guess is less than computer's guess") 
        again(computer)
    
        


def beginning():
    x=int(input("Enter the  lower range of number: "))
    y=int(input("Enter the  upper range of number: "))


    computer = computer_guess(x,y)
    


    print("     ***Computer has selected a random number form the given range***  ")

    user_input=int(input("Enter your guess: "))
    if(user_input>=x and user_input<=y):
        result(computer,user_input)
    else:
        print("your guess is out of range:")
        exit()
beginning()
    

