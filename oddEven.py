number=int(input("Enter number "))
def oddEven(number):
  if number%2==1:
    print("Weird")
  if number%2==0 and (number in range(2,6)):
    print("Not weird")
  elif number %2==0 and (number in range(6,21)):
    print("Weird")
  elif (number>20):
    print("Not Weird")
oddEven(number)
