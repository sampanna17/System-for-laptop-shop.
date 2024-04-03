import Operation # import the Operation module
from Read import read_name, read_custname, read_phone, startfile, readfile, validid, quantitybuy, quantitysell # import the read module
import Write # import the Write module

#Print a welcome message and start a file
print("\n")
print("-" * 105)# print a line of hyphens
print("|\t\t\t\tWelcome to the PIYA Electronics and Services\t\t\t\t|")
print("-" * 105)
print("|\t\t\t\t\t Address : DurbarMarg\t\t\t\t\t\t|")
print("-" * 105)
print("\t\t\tUnleash your potential with our powerful and portable laptops.")
print("\t\t\t\tDesigned to empower you wherever you go.")
print("-" * 105)
    
startfile()# calling the startfile() function

continueLoop = True

while continueLoop == True:

    try:
        
        #Display options to the user for buying, selling or exiting the program
        print("\n")
        print("Press 1 to buy from manufacturer ") # prompt the user to enter 1 to buy from manufacturer
        print("Press 2 to sell to customer ") # prompt the user to enter 2 to sell to customer
        print("Press 3 to exit from system ") # prompt the user to enter 3 to exit from system

        
        #Get user input to perform an action based on the option selected
        userinput = int(input("Enter from the option : "))

        if userinput == 1:
                
            print("\n")
            print("-" * 105)
            print("Thank you for buying")
            print("-" * 105)
            print("We will need your name and number to print bill")
            print("-" * 105)
            print("\n")

            mydict = readfile() # call the readfile() function and store the returned dictionary in mydict
            name = read_name() # call the read_name() function and store the returned name in name
            phone_number = read_phone() # call the read_phone() function and store the returned phone number in phone_number
            
            buymore = True
            userbuy_dictionary = [] # create an empty list called userbuy_dictionary
            while buymore:

                startfile()
                print("\n")

                valid_id = validid() # call the validid() function and store the returned ID in valid_id
                user_quantity = quantitybuy(valid_id) # call the quantitybuy() function and store the returned quantity in user_quantity

                Product = str(mydict[valid_id][0])
                user_quantity = str(user_quantity)
                perPrice = str(mydict[valid_id][2].replace(("$"), ""))
                netAmount = str(int(perPrice)*int(user_quantity))
                VAT_applicableAmount = ((0.13)*(int(netAmount)))
                totalAmount_withVAT = (int(netAmount)+int(VAT_applicableAmount))
                    
                userbuy_dictionary.append(
                    [Product, user_quantity, perPrice, netAmount, VAT_applicableAmount, totalAmount_withVAT])
                
                print("\n")
                    
                Operation.buy_laptop(name, phone_number, Product, user_quantity, mydict, valid_id, userbuy_dictionary)
                    
                while True:
                    buymore_request = input("Do you want to buy more (Y/N): ").lower()
                    if buymore_request == 'y' or buymore_request == 'yes':
                        buymore = True
                        break
                    elif buymore_request == 'n' or buymore_request == 'no':
                        print("\n")
                        Write.buyBill(name, phone_number, userbuy_dictionary)
                        buymore = False
                        break
                    else:
                        print("\n")
                        print("Invalid input. Please enter Y or N.\n")

        elif userinput == 2:
            
            print("\n")
            print("-" * 105)
            print("Thank you for selling")
            print("-" * 105)
            print("We will need your name and number to print bill")
            print("-" * 105)
            print("\n")
            
            mydict = readfile()
            name = read_custname()
            phone_number = read_phone()
            
            sellmore = True
            usersell_dictionary = []
            while sellmore:

                startfile()
                print("\n")

                valid_id = validid()
                user_quantity = quantitysell(valid_id)

                Product = str(mydict[valid_id][0])
                user_quantity = str(user_quantity)
                perPrice = str(mydict[valid_id][2].replace("$", ''))
                Total = int(perPrice) * int(user_quantity)
                #ShippingCost = 0
                #totalAmount_withShippingCost = ShippingCost + Total
                
                #usersell_dictionary.append([Product, user_quantity, perPrice, Total, ShippingCost , totalAmount_withShippingCost])
                usersell_dictionary.append([Product, user_quantity, perPrice, Total])

                Operation.sell_laptop(name, phone_number, Product, user_quantity,mydict, valid_id, usersell_dictionary)

                while True:
                    sellmore_request = input("Do you want to sell more (Y/N): ").lower()
                    if sellmore_request == 'y' or sellmore_request == 'yes':
                        sellmore = True
                        break
                    elif sellmore_request == 'n' or sellmore_request == 'no':
                        print("\n")
                        sellmore = False    
                        shipping = True
                        while shipping == True:
                            shipping_request = input("DO you want your laptop to be shipped (Y/N) : ").lower()
                            if shipping_request == "y" or shipping_request == "yes":
                                '''ShippingCost = 500
                                totalAmount_withShippingCost = Total + ShippingCost
                                usersell_dictionary[-1][-2] = ShippingCost
                                usersell_dictionary[-1][-1] = totalAmount_withShippingCost'''
                                Write.shipped_sellBill(name, phone_number, usersell_dictionary)
                                shipping = False
                            elif shipping_request == "n" or shipping_request == "no":
                                Write.sellBill(name, phone_number, usersell_dictionary)
                                shipping = False
                            else:
                                print("\n")
                                print("Invalid input. Please enter Y or N.")
                                print("\n")
                                continue
                        break
                    else:
                        print("\n")
                        print("Invalid input.Please enter Y or N.")
                        print("\n")
                if not sellmore:
                    break
                
        #If the user selects '3', the program exits.                
        elif userinput == 3:
            Operation.exit_system()
            continueLoop = False

        else:
            print("\n")
            print("Please check the option and continue")

    except ValueError:
        print("\n")
        print("Invalid input. Please enter a number .")
