def strength_checker(var):
    
    digit = ["0","1","2","3","4","5","6","7","8","9"]
    upper_alpha = {"Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"}
    lower_alpha = {"q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"}
    special_char = {"!","@","#","$","%","^","&","*","_","+","-" ,"=" ,";" ,":","."}
    
    if len(var) < 8 :
        return "Weak : Password length should be atleast 8 ."
        
    if not any(char in digit for char in var):
        return "Password is Weak : Password should contain atleast one number."
    
    if not any(char in upper_alpha for char in var):
        return "Password is Weak : Password should contain atleast one Uppercase Alphabet."
    
    if not any(char in lower_alpha for char in var):
        return "Password is Weak : Password should contain atleast one lowercase Alphabet."
    
    if not any(char in special_char for char in var):
        return "Password is Weak : Password should contain atleast one special character."
    
    return "Password is strong ."
            
var = input("Enter your password : ")        
password = strength_checker(var)
print(password)

#TIME COMPLEXITY OF CODE IS O(n)
#SPACE COMPLEXITY OF CODE IS O(1)