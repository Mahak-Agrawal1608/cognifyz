def valid_email(email):
    if "@" in email and "." in email.split("@")[1]:
        return True
    else:
        return False

sample = "cognifyz.technology@gmail.com"

if valid_email(sample):
    print(f"{sample} is a valid email address.")
else:
    print(f"{sample} is not a valid email address.")

#TIME COMPLEXITY OF CODE IS O(n)
#SPACE COMPLEXITY OF CODE IS O(n)