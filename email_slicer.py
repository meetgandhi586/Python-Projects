# -*- coding: utf-8 -*-
"""Email_Slicer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uUWHJ7Orcgf60IeLIWWoU0MCScARK2Hj

# **Email Slicer**

Collect Email From User
split the email using @
split the domain using .
Example:Username: meetgandhi586 Domain: gmail Extension:com
"""

def main():
  print("Welcome to Email-Slicer")
  print("")
  email_input = input("Enter the Email:")
  (username, domain)=email_input.split("@")
  (domain, extension)=domain.split(".")
  print("The username is:",username)
  print("The domain is:",domain)
  print("The extension is:",extension)

main()