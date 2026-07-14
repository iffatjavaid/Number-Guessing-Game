#Random Number ::
import random
print("*"*40)
print("           Random Guessing Game              ")
print("*"*40)
while True:
   secret=random.randint(1,10)
   attempts=0
   while True:
        guess=int(input("Guess the No between (1,10): "))
        attempts+=1
        if(secret==guess):
           print("You Win!")
           print("Total Attempts: ",attempts)
           break
        elif secret>guess:
           print("Too low")    
        else:
           print("Too High") 
          
   play_again=input("Play Again Yes/No : ").lower()
   if(play_again!="yes"):
      print("Thanks for playing!")
      break
#......................................................................
