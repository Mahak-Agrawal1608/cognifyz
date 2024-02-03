def palindrome(s):
    s = s.lower()
    rev_s = s[::-1]
    return s == rev_s
    
str = "madam"
if palindrome(str):
    print(f"{str} is the palindrome. ")
else:
    print(f"{str} is not the palindrome. ")


#TIME COMPLEXITY OF CODE IS O(n)
#SPACE COMPLEXITY OF CODE IS O(n)