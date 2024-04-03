
def readfile():
    # Open the file "LaptopDetails.txt" in read mode
    file = open("LaptopDetails.txt", "r")
    # Create an empty dictionary to store laptop details
    mydict = {}
    laptopid = 1

    for line in file:
        # Remove newline character from the line
        line = line.replace("\n", "")
        # Split the line by comma and add the resulting list to the dictionary with the laptop ID as the key
        mydict[laptopid] = line.split(",")
        # Increment the laptop ID for the next iteration
        laptopid += 1
    file.close()
    # Return the dictionary of laptop details
    return mydict

def startfile():
    # Print the headers for the laptop details table
    print("\n")
    print("S.N.\tName\t\t\tBrand\t\tPrice\t\tQuantity\tProcessor\tGraphics")
    a = 1
    # Open the file "LaptopDetails.txt" in read mode
    with open("LaptopDetails.txt", "r") as file:
        for line in file:
            # Remove whitespace characters from the line and split it by comma
            line = line.strip().split(",")
            if line == ['']:
                continue
            print(f"{a}\t{line[0]}\t{line[1]}\t{line[2]}\t\t{line[3]}\t\t{line[4]}\t{line[5]}")
            a += 1

def read_name():
    # Loop until a valid name is entered
    name_Loop = True
    while name_Loop: 
        try:
            name = input("Enter the name of the company : ")
            # Convert the name to string to check for invalid input
            str(name)  # try to convert name to string to check for invalid input
            print("\n")
            if name == "" :
                print("Enter valid name")
                print("\n")
                continue
            # If no exception is raised, break out of the loop
            name_Loop = False # if no exception is raised, break out of the loop
        except ValueError:
            # If an invalid name is entered, print an error message and continue the loop
            print("Invalid input. Please enter a valid name.\n")
            print("\n")
    return name

def read_custname():
    name_Loop = True
    while name_Loop: 
        try:
            name = input("Enter the name of the customer : ")
            print("\n")
            # If the name is empty, prompt the user to enter a valid name and continue the loop
            if name == "" :
                print("Enter valid name")
                print("\n")
                continue
            name_Loop = False # if no exception is raised, break out of the loop
        except ValueError:
            # If an invalid name is entered, print an error message and continue the loop
            print("Invalid input. Please enter a valid name.\n")
            print("\n")
    return name

def read_phone():
    phone_Loop = True
    while True: 
        try:
            phone_number = input("Enter phone number: ")
            # try to convert phone number to integer to check for invalid input
            int(phone_number)
            break # if no exception is raised, break out of the loop
        except ValueError:
            print("\n")
            
            print("Invalid input. Please enter a valid phone number.")
            print("\n")
    return phone_number

def validid():
    mydict = readfile()
    loop = True
    while True:
        try:
            valid_id = int(
                input("Provide the ID of the laptop : "))
            if valid_id <= 0 or valid_id > len(mydict) or valid_id == "":
                raise ValueError
            # if no exception is raised, break out of the loop
            break
        except ValueError:
            print("\n")
            print("Error: Please provide a valid laptop ID.")
            print("\n")
    return valid_id


def quantitybuy(valid_id):
    mydict = readfile()
    quantitybuyloop = True
    while True:
        try:
            user_quantity = int(
                input("Enter the quantity of  the laptop you want to buy :"))
            get_quantity = mydict[valid_id][3]
            if user_quantity == "":
                print("\n")
                print("Error: The quantity you are looking for is not available at the moment. Please choose from the laptop details provided.\n")
            else:
                break
        except ValueError:
            print("\n")
            print("Error: Please enter a valid quantity.\n")
    return user_quantity

def quantitysell(valid_id):
    mydict = readfile()
    quantityselloop = True
    while True:
        try:
            user_quantity = int(
                input("Enter the quantity of  the laptop you want to sell :"))
            get_quantity = mydict[valid_id][3]
            if user_quantity <= 0 or user_quantity > int(get_quantity) or user_quantity == "":
                print("\n")
                print("Error: The quantity you are looking for is not available at the moment. Please choose from the laptop details provided.\n")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid quantity.\n")
    return user_quantity
