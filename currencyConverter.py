amount=float(input("Enter the amount you'd wish to convert "))
value=input("Reply with a 'U' if amount is in Ugandan Shillings or 'K' if its in Kenyan Shillings? ").upper()

if value=="U":
    convertedAmount=amount/33.31
    print(f"That is {convertedAmount} Kenyan Shillings")

elif value=="K":
    convertedAmount=amount*33.31
    print(f"That is {convertedAmount} Ugandan Shillings")
