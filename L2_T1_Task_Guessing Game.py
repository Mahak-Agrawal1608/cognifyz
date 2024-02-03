import random 

def guess():
    i = random.randint(1,100)
    while True:
        num = int(input("Guess the number between 1 to 100 : "))
        
        if i > num:
            print("Too low")
        elif i < num:
            print("Too high")
        else: 
            print(f"{i} is the right guess.")
            break
        

print("##### Number Guessing Game #####\n")
while True:
    guess()
    break
print("\nThank you for playing.!")

#TIME COMPLEXITY OF CODE IS O(1)
#SPACE COMPLEXITY OF CODE IS O(1)