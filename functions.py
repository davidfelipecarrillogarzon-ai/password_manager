import bcrypt
import sys
import os

if not os.path.exists("user_name.txt"):
    open("user_name.txt", "w").close()
if not os.path.exists("pass.txt"):
    open("pass.txt", "wb").close()
def principal_greet():
    user = ""
    with open("user_name.txt", "r") as archivo:
        content = archivo.read().strip()
    if not content:
         user = input ("Let's start with your name:\n").strip()
         with open("user_name.txt", "w") as archivo:
          archivo.write(user)
         print(f"Welcome to our password manager {user}, what are you going to do now: ")
    else:
     print(f"Welcome to our password manager {content}, what are you going to do now: ")
    principal_password()
    
def principal_password():##Function to check if the user already has a main password or to create one
    
    with open("pass.txt", "rb") as f:
        stored_hash = f.read()
    
    if not stored_hash:
     main_password = input(f"We're going to define your main password\n")
     confirmation_main_password = input("Confirm your main password\n")
    
     while main_password != confirmation_main_password:
         confirmation_main_password = input("You wrote a wrong password verification, try again\n")
        
     password_bytes = main_password.encode('utf-8')##For bcrypt to work
    
     hashed_principal_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    
     with open("pass.txt", "wb") as f:
         f.write(hashed_principal_password)
     main_password_verification()
    else:
        main_password_verification()
    
def main_password_verification():
    main_p_verification = input("write your main password\n")
    
    main_p_v_encode = main_p_verification.encode('utf-8')
    
    with open("pass.txt", "rb") as f:
     stored_hash = f.read()
    attemps = 2
    while not bcrypt.checkpw (main_p_v_encode, stored_hash):
        main_p_verification = input(f"Wrong password remaining attemps {attemps} \n")
        main_p_v_encode = main_p_verification.encode('utf-8')
        attemps -= 1
        if attemps == 0:
            sys.exit("The attempts were defeated")
    print("Correct password")
        
        
def save_password():
    print("Coming soon...")
    
def edit_password():
    print("Coming soon...")

def delete_password():
    print("Coming soon...")
    
def main_menu():
    principal_greet()
    while True:
        try:
            menu_option = int(input("==MENU==\n 1.Save a new password\n 2.Edit a password\n 3.Delete a password\n 4.Exit\n"))
            if menu_option == 1:
              save_password()
            elif menu_option == 2:
              edit_password()
            elif menu_option == 3:
              delete_password()
            elif menu_option == 4:
              sys.exit("You exited the password manager...")
            else:
               print("Select a correct option")
        except ValueError:
             print("Enter only numbers")