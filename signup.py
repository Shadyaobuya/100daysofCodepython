def login():
    userName=input("Enter Your Username: ")
    password=input("Enter Your password: ")
   
    if (len(password)<=6)or(password.islower()==True) or (password.isdigit()==True)or (userName[0:5] == password[0:5]) :
        print("Your Password should have At least one Uppercase character,\nA number,\nShouldnt be less than 6 characters\nAnd your Password should not contain your name")  
    else:
        
        print("Account created Successfully")

login()