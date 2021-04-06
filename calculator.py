print("This is a simple calculator that takes in two digits, performs a mathematical operation and prints out the result")
print("Enter the values \n")
value1=float(input("Value 1: "))
value2=float(input("Value 2: "))
print("Choose an operation to perform on the values given")
sign=input("""
'+' to add the values
'-' to subtract the values
'*' to multiply the two values
'/' to divide the two values \n""")

if sign =="+":
    add =value1+value2
    print(add)
elif sign =="-":
    subtract=value1-value2
    print(subtract)
elif sign =="*":
    multiply=value1*value2
    print(multiply)
elif sign =="/":
    divide=value1/value2
    print(divide)
else:
    print("Enter a valid sign")
