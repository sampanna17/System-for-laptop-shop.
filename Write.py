from Operation import buy_laptop, sell_laptop
from datetime import date
from datetime import datetime
from Read import *

def buyBill(name, phone_number, userbuy_dictionary):
    
    print("-" * 105)
    print("\t\t\t\t\tBILL")
    print("-" * 105)
    print("\t\t\t\tPIYA Electronics and Services")
    print("\t\t\t\t Address : DurbarMarg")
    print("-" * 105)
    print("\n")
    print("Name of company : " + name)
    print("Phone number of customer : "+ phone_number)
    print("\n")
    print("-" * 105)
    print("\t\t\t\t\tYour order")
    print("-" * 105)
    print("\n\nProduct name\t Quantity\t Unit Price\t Net Amount\t Applicable VAT Amount\t Total Amount\n")
   
    for i in userbuy_dictionary:
        print(i[0],"\t",i[1],"\t\t $",i[2],"\t $",i[3],"\t $",i[4],"\t\t $",i[5])
        print("\n")
        
    total = 0

    # loop through the dictionary and add up the totalAmount_withShippingCost for each laptop
    for index, sublist in enumerate(userbuy_dictionary):
        total += sublist[-1]
        
    # print the total
    print("Your total amount : $" + str(total))
    print("\n")
    
    today = date.today()
    now = datetime.now()
    print("-" * 105)
    print("Sent on: " + today.strftime("%B %d, %Y") +
          " at " + now.strftime("%H:%M:%S"))
    print("-" * 105)

    with open('buy_Bill.txt', 'w') as buy:
        buy.write("-" * 105)
        buy.write("\n")
        buy.write("\t\t\t\t\t\tBILL")
        buy.write("\n")
        buy.write("-" * 105)
        buy.write("\n")
        buy.write("\t\t\t\t     PIYA Electronics and Services")
        buy.write("\n")
        buy.write("-" * 105)
        buy.write("\n")
        buy.write("\t\t\t\t\tAddress : DurbarMarg")
        buy.write("\n")
        buy.write("-" * 105)
        buy.write("\n")
        buy.write("\n")
        buy.write("Name of Customer : " + name + "\n")
        buy.write("Phone number     : " + phone_number)
        buy.write("\n")
        buy.write("\n")
        buy.write("-" * 105)
        buy.write("\n")
        buy.write("\t\t\t\t\tYour order")
        buy.write("\n")
        buy.write("-" * 105)
        buy.write("\n")
        buy.write("\nProduct name\t  Quantity\tUnit Price\tNet Amount\tApplicable VAT Amount\tTotal Amount\n")
        buy.write("\n")
        for i in userbuy_dictionary:
            buy.write(str(i[0])+"\t  "+str(i[1])+"\t\t$"+str(i[2]) +"\t\t$"+str(i[3])+"\t\t$"+str(i[4])+"\t\t\t$"+str(i[5]))
            buy.write("\n")
            
        total = 0

        # loop through the dictionary and add up the totalAmount for each laptop
        for index, sublist in enumerate(userbuy_dictionary):
            total += sublist[-1]
        
        # print the total
        buy.write("\n")
        buy.write("Your total amount : $" + str(total))
        buy.write("\n")
        
        buy.write("\n")
        buy.write("-" * 105)
        today = date.today()
        now = datetime.now()
        buy.write("\n")
        buy.write("Ordered on "+today.strftime("%B %d, %Y") +
                  " at " + now.strftime("%H:%M:%S"))
        buy.write("\n")
        buy.write("-" * 105)
            

def sellBill(name, phone_number, usersell_dictionary):
    
    print("\n")
    print("-" * 105)
    print("\t\t\t\t\tBILL")
    print("-" * 105)
    print("\t\t\t\t PIYA Electronics and Services")
    print("\t\t\t\t  Address : DurbarMarg")
    print("-" * 105)
    print("\nName of customer       : " + name)
    print("Phone number of customer : " + phone_number)
    print("\n"+("-" * 105))
    print("\t\t\t\t   Your order")
    print("-" * 105)
    print("\nProduct name\t  Quantity\tUnit Price\tTotal Price\n")
    
    for i in usersell_dictionary:
         print(str(i[0]) + "\t  " + str(i[1]) + "\t\t$ " + str(i[2]) + "\t\t$ " + str(i[3]))
         
    total = 0
    
    # loop through the dictionary and add up the totalAmount_withoutShippingCost for each laptop
    for index, sublist in enumerate(usersell_dictionary):
        total += sublist[-1]
        
    Shipping_Cost = 0
    print("\nShipping Cost = $"+str(Shipping_Cost))
    Total_Amount = total + Shipping_Cost
    # print the total
    print("Total amount without shipping cost for all laptops sold : $" + str(Total_Amount))
    
    today = date.today()
    now = datetime.now()
    print("\n"+("-" * 105))
    print("Sent on: " + today.strftime("%B %d, %Y") +
          " at " + now.strftime("%H:%M:%S"))
    print("-" * 105)
    
    with open('sell_Bill.txt', 'w') as sell:
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("\t\t\t\t  BILL")
        sell.write("\n")
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("\t\t\tPIYA Electronics and Services")
        sell.write("\n")
        sell.write("\t\t\t    Address : DurbarMarg")
        sell.write("\n")
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("\n")
        sell.write("Name of customer        : "+name)
        sell.write("\n")
        sell.write("\n")
        sell.write("Phone number of customer: " + phone_number)
        sell.write("\n")
        sell.write("\n")
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("\t\t\t\tYour order :")
        sell.write("\n")
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("Product\t\t\tQuantity\tUnit Price\tTotal\n")
        sell.write("\n")
        for i in usersell_dictionary:
            sell.write(str(i[0])+"\t\t"+str(i[1])+"\t\t$ "+str(i[2])+"\t\t$ "+str(i[3]))
            sell.write("\n")
        sell.write("-" * 80)
        
        total = 0

        # loop through the dictionary and add up the totalAmount_withoutShippingCost for each laptop
        for index, sublist in enumerate(usersell_dictionary):
            total += sublist[-1]
        
        sell.write("\n")
        sell.write("\n")
        Shipping_Cost = 0
        sell.write("Shipping Cost = $"+str(Shipping_Cost))
        Total_Amount = total + Shipping_Cost
        sell.write("\n")
        # print the total
        sell.write("\n")
        sell.write("Total amount without shipping cost for all laptops sold : $" + str(Total_Amount))
        sell.write("\n")
        sell.write("\n")
        sell.write("-" * 80)

        today = date.today()
        now = datetime.now()
        sell.write("\n")
        sell.write("Sold on " + today.strftime("%b %d %y ") + now.strftime("%H:%M:%S"))
        sell.write("\n")
        sell.write("-" * 80)

def shipped_sellBill(name, phone_number, usersell_dictionary):
    
    print("\n")
    print("-" * 105)
    print("\t\t\t\t\tBILL")
    print("-" * 105)
    print("\t\t\t\t PIYA Electronics and Services")
    print("\t\t\t\t  Address : DurbarMarg")
    print("-" * 105)
    print("\nName of customer        : "+name)
    print("\nPhone number of customer: "+phone_number)
    print("\n"+("-" * 105))
    print("\t\t\t\t   Your order")
    print("-" * 105)
    print("\nProduct name\t Quantity\tUnit Price\tTotal price\n")
    
    for i in usersell_dictionary:
        print(str(i[0])+"\t "+str(i[1])+"\t\t$"+str(i[2]) +"\t\t$"+str(i[3]))
    
    total = 0

    # loop through the dictionary and add up the totalAmount_withShippingCost for each laptop
    for index, sublist in enumerate(usersell_dictionary):
        total += sublist[-1]
        
    Shipping_Cost = 500
    print("\nShipping Cost = $",Shipping_Cost)
    Total_Amount = total + Shipping_Cost

    # print the total
    print("Total amount with shipping cost for all laptops sold : $" + str(Total_Amount))
    
    today = date.today()
    now = datetime.now()
    print("\n"+("-" * 105))
    print("Sent on: " + today.strftime("%B %d, %Y") +
          " at " + now.strftime("%H:%M:%S"))
    print("-" * 105)
    
    with open('sell_Bill.txt', 'w') as sell:
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("\t\t\t\t  BILL")
        sell.write("\n")
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("\t\t\tPIYA Electronics and Services")
        sell.write("\n")
        sell.write("\t\t\t    Address : DurbarMarg")
        sell.write("\n")
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("\n")
        sell.write("Name of customer        : "+name)
        sell.write("\n")
        sell.write("\n")
        sell.write("Phone number of customer: " + phone_number)
        sell.write("\n")
        sell.write("\n")
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("\t\t\t\tYour order :")
        sell.write("\n")
        sell.write("-" * 80)
        sell.write("\n")
        sell.write("Product\t\t\tQuantity\tUnit Price\tTotal\n")
        sell.write("\n")
        for i in usersell_dictionary:
            sell.write(str(i[0])+"\t\t"+str(i[1])+"\t\t$ "+str(i[2])+"\t\t$ "+str(i[3]))
            sell.write("\n")
        sell.write("-" * 80)
        
        total = 0

        # loop through the dictionary and add up the totalAmount_withShippingCost for each laptop
        for index, sublist in enumerate(usersell_dictionary):
            total += sublist[-1]
        
        sell.write("\n")
        sell.write("\n")
        Shipping_Cost = 500
        sell.write("Shipping Cost = $"+str(Shipping_Cost))
        Total_Amount = total + Shipping_Cost
        sell.write("\n")
        # print the total
        sell.write("\n")
        sell.write("Total amount with shipping cost for all laptops sold : $" + str(Total_Amount))
        sell.write("\n")
        sell.write("\n")
        sell.write("-" * 80)

        today = date.today()
        now = datetime.now()
        sell.write("\n")
        sell.write("Sold on " + today.strftime("%b %d %y ") + now.strftime("%H:%M:%S"))
        sell.write("\n")
        sell.write("-" * 80)
        
