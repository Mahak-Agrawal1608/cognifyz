import random 

def guess():
    i = random.randint(1,10)
    while True:
        num = int(input("Guess the number between 1 to 10 : "))
        
        if i > num:
            print(f"{num} is too low")
        elif i < num:
            print(f"{num} is too high")
        else: 
            print(f"{i} is the right guess.")
            break
        

print("##### Number Guessing Game #####\n")
while True:
    guess()
    break
print("\nThank you for playing.!")

#TIME COMPLEXITY OF CODE IS O(n)
#SPACE COMPLEXITY OF CODE IS O(1)