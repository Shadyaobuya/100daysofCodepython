
fruit=input("what do you want to buy? ")
if fruit=="mango" or fruit=="orange" or fruit=="banana":
    number=int(input(f"How many {fruit}(s) do you want to buy "))
    if fruit=="mango":
        price=30*number
        print(f"The item(s) in your cart cost {price} Kenyan Shillings. ")
    elif fruit=="banana":
        price=20*number
        print(f"The item(s) in your cart cost {price} Kenyan Shillings. ")
    elif fruit =="orange":
        price=30*number
        print(f"The item(s) in your cart cost {price} Kenyan Shillings. ")


    checkOut=input("Proceed to checkout? ")
    if checkOut=="yes":
        payment=input("""Choose a payment method: 
                                M-Pesa
                                MasterCard
                                Cash\n""")
        if payment=="M-Pesa":
            print("A code has been sent to your phone. Enter pin to confirm purchase")
            print("Thank you for shopping with us")
        elif payment=="MasterCard":
            cardnumber=int(input("Enter your card number: "))
            print("Thank you for shopping with us")
        elif payment=="Cash":
            print(f"Youll be charged {price} Ksh on delivery")
            print("Thank you for shopping with us")

    else:
            print("Back to shop")
else:
    print(f"Sorry. We are out of {fruit}s now. Check in later")