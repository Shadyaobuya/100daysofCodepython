import math
print("""This prgram calculate the compound Interest, Amount or time in years:
      Enter T to calculate time
      A to calculate amount
      CI to calculate Compound Interest """)
askInput=input("What are you trying to calculate: ").upper()

if (askInput == "CI" or askInput =="A" or askInput=="T"):
    

    
    principal=float(input("Enter the principal Amount: "))
    rate=float(input("Enter the rate in Decimal form: "))
    n=float(input("How many times is the amount being compounded: "))     

    if askInput=="CI":
        time=float(input("Enter time in years: "))
        amount=principal*((1+(rate/n))**(n*time))
        compoundInterest=amount-principal
        print(f"The compounded interest is {compoundInterest:.2f} after {time} years")

    elif askInput=="A":
        time=float(input("Enter time in years: "))
        amount=principal*((1+(rate/n))**(n*time))
        print(f"The total amount is {amount:.2f}")


    elif askInput=="T":
        amount=float(input("Enter the total Amount: "))
        time=math.ceil((math.log(amount/principal))/(math.log(1+rate)))
        print(f"The time it will take for the given amount to have the given interest is {time} years")
       
else:
    print("Enter valid value")



        

    
    

    
