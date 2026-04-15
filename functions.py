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