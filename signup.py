def login():
    userName=input("Enter Your Username: ")
    password=input("Enter Your password: ")
   
    if (len(password)<=6):
      
      print("Should be more than 6 Characters ")
    if (password.islower()==True):
      print("Your Password should have At least one Uppercase character")

    if (password.isdigit()==False):
        print("Account created Successfully")
    
login()

