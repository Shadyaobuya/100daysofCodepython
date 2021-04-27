import sys
laboratory={
    'pipette':3,
    'lab Stool':4,
    'burette':20,
    'measuring cylinder':35
}
print("Type 'check' to view items in the inventory\n'update to update an item'\n and 'delete' to delete item")
action=input("What do you want to do?: ")
if action=='check':
    print(" Type in 'view' to view the whole inventory or 'name' to view the value of a certain stored object ")
    check_action=input()
    if check_action=='view':
        print(laboratory)
        for name,value in laboratory.items():
            if value <= 5:
                print(f"Looks like you are almost running out of stock for {name}:{value}. Update? ")
                update=input()
                if update=='yes':
                        updateval=int(input('Enter new value: '))
                        laboratory[name]=updateval
                        print("Successfully updated: "+str(laboratory))
                elif update=='no':
                        print("database not updated "+str(laboratory))


    elif check_action=='name':
        input_name=input("What do you want to check? ")
        if input_name in laboratory:
            print("{}:{} ".format (input_name,laboratory[input_name]))
        else:
            print("Item does not exist in your inventory")
            add=input("Would you like to add it? ")
            if add=="yes":
                amount=int(input("Enter its value: "))
                laboratory.setdefault(input_name,amount)
                print(f"Item has been successfully added: {str(laboratory)}")
                #sys.exit()
            else:
                print(laboratory)
                #sys.exit()

elif action=='update':
    print(str(laboratory)+"\n Key in name of item you want to update?: ")
    keyupdate=input()
    if keyupdate in laboratory.keys():
        newval=int(input("Enter new value: "))
        laboratory[keyupdate]=newval
        print("Database successfully updated: "+str(laboratory))
    else:
        print("item does not exist in database. ")

elif action=='delete':
    print(str(laboratory)+"\n What do you want to delete? ")
    delval=input()
    if delval in laboratory.keys():
        del laboratory[delval]
        print(str(laboratory)+"\nItem successfully deleted from database")
else:
    print("Enter a valid action ")


   
    

    
    





        

