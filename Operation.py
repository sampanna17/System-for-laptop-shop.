import Read # Importing the Read module

def buy_laptop(name, phone_number, Product, user_quantity, mydict, valid_id, userbuy_dictionary):
    # Reading data from the text file
    mydict = Read.readfile()
    
    # Update the text file
    mydict[valid_id][3] = int(mydict[valid_id][3]) + int(user_quantity)

    with open('LaptopDetails.txt', 'w') as file:
        for values in mydict.values():
            if len(values) == 6:
                file.write(f"{values[0]},{values[1]},{values[2]},{values[3]},{values[4]},{values[5]}\n")

    # Print thank you message for the user       
    print("-" * 105)
    print("\n")
    print("\t\t\t\t\t Thank you for your purchase.")
    print("\n")
    print("-" * 105)
    print("\n")

    return userbuy_dictionary, valid_id


def sell_laptop(name, phone_number, Product, user_quantity,mydict, valid_id, usersell_dictionary):
    
    # Reading data from the text file
    mydict = Read.readfile()

    # Update the text file
    mydict[valid_id][3] = int(mydict[valid_id][3]) - int(user_quantity)
    
    with open('LaptopDetails.txt', 'w') as file:
        for values in mydict.values():
            if len(values) == 6:
                file.write(f"{values[0]},{values[1]},{values[2]},{values[3]},{values[4]},{values[5]}\n")
    print("\n")    
    print("-" * 105)
    print("\n")
    print("\t\t\t\t\t Thank you for Selling.")
    print("\n")
    print("-" * 105)
    print("\n")

    return usersell_dictionary, valid_id
    print("\n")

def exit_system():
    print("\n")
    print("*" * 105)
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t  "+"Thank you for using the system"+"\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("*" * 105)
