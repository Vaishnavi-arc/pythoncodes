
import re
pattern="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[a-z 0-9]+[.]\w{2,3}$"
email=input("email : ")
if re.search(pattern,email):
    print("Email is valid.")
else:
    print("Email is invalid")
