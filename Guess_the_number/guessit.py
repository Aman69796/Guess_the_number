import random
n=random.randint(1,100)
a=-1
guesses=0  

'''
if(a<n):
    print("Your number is smaller than the random number ")
elif(a>n):
    print("Your number is larger than the random number ")
else:
    print("Right guess")
    '''
attempts=int(input("Enter in how many attempts you want to guess this number"))
while(a!=n):
    guesses+=1
    attempts-=1
    a=int(input("Enter a number"))
    if(guesses>attempts):
        print("You ran out of attempts")
         
    if(a>n):
        
     print("The number to find is lower")
     
     
     print(f"you have {attempts} attempt left")
     
    
    elif(a<n):
        print("The number to find is greater")
        print(f"you have {attempts} attempt left")
    if(attempts<=0):
        break
        
        
    
     
if(guesses>attempts):
    print(f"You were not able to guess the number in the {guesses} attempt")
else:
 print(f"You have guessed the number {n} right and you have guessed it in {guesses} attempt ")