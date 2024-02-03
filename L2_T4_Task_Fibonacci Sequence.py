num = int(input("Enter the fibonacci range : "))
i = 0
first_number = 0
second_number = 1
print(first_number)
print(second_number)
while(i<num-2):
    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number
    i = i + 1
    print(next_number)


#TIME COMPLEXITY OF CODE IS O(n)
#SPACE COMPLEXITY OF CODE IS O(1)