#
#
#
#
#
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your E-mail:")

if re.search(email_condition,user_email):
    print("Your E-mail is perfect.")
else:
    print("Your E-mail is Improper. \nMake it Proper!")