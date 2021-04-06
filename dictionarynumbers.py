numbers=input("Enter any number from 0-10 to see how it's read in Swahili: ")
conversion={
    "1":"Moja",
    "2":"Mbili",
    "3":"Tatu",
    "4":"Nne",
    "5":"Tano",
    "6":"Sita",
    "7":"Saba",
    "8":"Name",
    "9":"Tisa",
    "10":"Kumi",
    "0":"Sufuri"
}
for number in numbers:
    print(conversion.get(number))