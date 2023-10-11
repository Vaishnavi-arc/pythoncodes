import re
password=input("Enter your password.")
if len(password)<8:
    print("Password length must be atleast 8 characters or more.")
elif not  re.search("[A-Z]",password) :
    print("Password must contain one UPPERCASE letter.")
elif not  re.search("[a-z]",password):
    print("Password must contain one lower case letter.")
elif not  re.search("[0-9]",password):
    print("Password must contain one digit.")
elif not  re.search("[._@#$!&]",password):
    print("Password must contain one of these ._-@#$!& symbols.")
else:
    print("Password is Strong")




