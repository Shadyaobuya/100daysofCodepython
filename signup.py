def login():
    userName=input("Enter Your Username: ")
    password=input("Enter Your password: ")
   
    if (len(password)<=6):
      
      print("Should be more than 6 Characters ")
    if (password.islower()==True):
      print("Your Password should have At least one Uppercase character")

    if (password.isdigit()==True):
      print("Password should have at least one Number")
    if (userName[0:5] == password[0:5]) :
      print("Password should not contain your name")
    else:
        print("Account created Successfully")
    
login()
