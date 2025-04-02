#Welcome to American Shipment Company
import json
Buyer={}
name = []
address = []
item_name = []
weight = []
distance = []
cost = []

#All THE Functions:

def buy():#buy function
    print("Welcome to American Shipment Company")
    calculate()
def sell():#sell function
    print("Welcome to American Shipment Company")
    seller()
def money():#money function
    while True:
        global Money
        global cost
        Money = 0
        print("Please Enter 1.If the item is a mobile phone")
        print("Please Enter 2.If the item is a laptop/ laptop accessories")
        print("Please Enter 3.If the item is a camera")
        print("Please Enter 4.If the item is a tablet")
        print("Please Enter 5.If the item is a printer")
        print("Please Enter 6.If the item is a TV/ TV Accessories")
        print("Please Enter 7.If the item is a computer/ Computer Accessories")
        print("Please Enter 8.If the item is an other electronic item")
        b= input("What is the electronic item you want to sell: ")
        if b == 1:
            Money = Money + 10000
            print("If you want to Discuss with the price then contact us on +91 9999999999")
        elif b == 2:
            Money = Money + 100000
            print("If you want to Discuss with the price then contact us on +91 9999999999")
        elif b == 3:
            Money = Money + 25000
            print("If you want to Discuss with the price then contact us on +91 9999999999")
        elif b == 4:
            Money = Money + 14500
            print("If you want to Discuss with the price then contact us on +91 9999999999")
        elif b == 5:
            Money = Money + 10000
            print("If you want to Discuss with the price then contact us on +91 9999999999")
        elif b == 6:
            Money = Money + 20000
            print("If you want to Discuss with the price then contact us on +91 9999999999")
        elif b == 7:
            Money = Money + 250000
            print("If you want to Discuss with the price then contact us on +91 9999999999")
        elif b == 8:
            print("Please contact us on +91 9999999999 if you want to talk to our contractor to sell your item") 
        a = input("What is the condition of the item?(Good/Bad): ")
        if a == "Good":
            Money = Money
            print("Thanks for using our service")
        elif a == "Bad":
            Money = Money - 7500
            print("If you want to Discuss with the price then contact us on +91 9999999999")
            print("Thanks for using our service")
        else:
            print("Invalid Input")
        return print("The cost of shipping your item is: ", Money)
def seller():#seller function
    global item_name
    print("Welcome to American Shipment Company")
    name=input("Enter your name: ")
    address=input("Enter your address in coordinates: ")
    item_name=input("Enter the name of the item: ")
    if item_name == "Electronics":
        money()
    weight = float(input("Enter the weight of the package in Kgs: "))
    distance = float(input("Enter Your distance from our office in Km: "))
    if weight > 40 and weight < 50:
        Money = Money - 250
    elif weight > 50 and weight < 100:
        Money = Money + 400
    elif weight > 100:
        Money = Money - 1000
    if distance > 2500 and distance < 5000:
        Money = Money - 500
    elif distance > 5000:
        Money = Money - 1000
    return print("The cost of shipping your item is: ", Money)

def reciving():#reciving function
    print("Welcome to American Shipment Company")
    name=input("Enter your name: ")
    address=input("Enter your address in coordinates: ")
    item_name=input("Enter the name of the item: ")
    weight = float(input("Enter the weight of the package in Kgs: "))
    if name in Buyer:
        if item_name in Buyer[name]:
            if address in Buyer[name][item_name]:
                if weight in Buyer[name][item_name][address]:
                    print("The item you want to receive is: ", Buyer[name][item_name][address][weight])
                    print('it will be recived in 3-5 working days')
                    print("Thanks for using our service")
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
def receive():#receive function
    print("Welcome to American Shipment Company")
    reciving()

def ship():#ship function
    print("Welcome to American Shipment Company")
    calculate()


def calculate():#calculate function
    global name
    global address
    global cost
    global item_name
    global weight
    global distance
    name=input("Enter your name: ")
    address=input("Enter your address in coordinates: ")
    cost = 0
    item_name=input("Enter the name of the item: ")
    weight = float(input("Enter the weight of the package in Kgs: "))
    distance = float(input("Enter Your distance from our office in Km: "))
    cost = weight * distance
    if weight > 40 and weight < 50:
        cost = cost + 100
    elif weight > 50 and weight < 100:
        cost = cost + 200
    elif weight > 100:
        cost = cost + 1000
    if distance > 2500 and distance < 5000:
        cost = cost + 500
    elif distance > 5000:
        cost = cost + 1000
    return print("The cost of shipping your item is: ", cost) ,stores() ,Itemtype()
        
def terms():#terms function
    print("Welcome to American Shipment Company")
    print("Please Read our Terms and Conditions Carefully before ordering")
    print("The cost of shipping your item is totally fair as we uses the distance and weight to calculate the costing and high advanced algorithm is being used to calculate the cost")
    print("If you want to Discuss with the price then contact us on +91 9999999999")
    print("The items will be recived in 3-5 working days")
    print("The items sold by us are 100% authentic and 100% safe")
    print("The items once sold to us are not if the item had been sold to us within a few weeks returnable")
    print("The items once sold to us are not refundable if the item is not in the same condition as it was when it was sold to us")
    print("If your item is damaged or not in the same condition as it was when it was sold by us to you then it is not refundable")
    print("The items once received by us are refundable if you contact us within 7 days of receiving the item on our office or online chat bots")
    print("There are many fraud companies in the market which might have similiar name like us so please buy from our official website only")
    print("You can also buy from our official website only")
    print("Thanks for using our service")
        
def Itemtype():#Item type function
    global cost
    global item_type
    global A 
    print("Please Enter 1.If the item is an electronic item")
    print("Please Enter 2.If the item is a food item")
    print("Please Enter 3.If the item is a clothing item")
    print("Please Enter 4.If the item is a book")
    print("Please Enter 5.If the item is a general item")
    print("Please Enter 6.If the item is a medical item")#item type of item")
    item_type = int(input("Please Enter the Number of the option you want to choose: "))
    if item_type == 1:
        print("Additional Charges will be applyed to your package as it is an electronic item and its fragile")
        cost = cost + 500
        print("The cost of shipping your item is: ", cost)
    elif item_type == 2:
        print("Additional Charges will be applyed to your package as it is a food item and its fragile")
        cost = cost + 500
        print("The cost of shipping your item is: ", cost)
    elif item_type == 3:    
        A = input("Do you think the general item your ordering is fragile as you dont want it to be damaged? (yes/no): ")
        if A.lower()=='yes':
            print("Thank you for keeping the transparancy with us and for your trust")
            print("No additional Charges will be applyed to your package for keeping the transparancy with us and for your trust")
            print("Thanks for using our service")
        else:
            print("Invalid Input")
        if A.lower()=='no':
            print("Thank you for keeping the transparancy with us and for your trust")
            print("No additional Charges will be applyed to your package as it is a general item and not fragile")
            print("Thanks for using our service")
            print("The cost of shipping your item is: ", cost)
        else:
            print("Invalid Input")
    elif item_type == 4:
        A = input("Do you think the general item your ordering is fragile as you dont want it to be damaged? (yes/no): ")
        if A.lower()=='yes':
            print("Thank you for keeping the transparancy with us and for your trust")
            print("No additional Charges will be applyed to your package for keeping the transparancy with us and for your trust")
            print("Thanks for using our service")
            print("The cost of shipping your item is: ", cost)
        else:
            print("Invalid Input")
        if A.lower()=='no':
            print("Thank you for keeping the transparancy with us and for your trust")
            print("No additional Charges will be applyed to your package as it is a general item and not fragile")
            print("Thanks for using our service")
            print("The cost of shipping your item is: ", cost)
        else:
            print("Invalid Input")
    elif item_type == 5:
        A = input("Do you think the general item your ordering is fragile as you dont want it to be damaged? (yes/no): ")
        if A.lower()=='yes':
            print("Thank you for keeping the transparancy with us and for your trust")
            print("No additional Charges will be applyed to your package for keeping the transparancy with us and for your trust")
            print("Thanks for using our service")
            print("The cost of shipping your item is: ", cost)
        else:
            print("Invalid Input")
        if A.lower()=='no':
            print("Thank you for keeping the transparancy with us and for your trust")
            print("No additional Charges will be applyed to your package as it is a general item and not fragile")
            print("Thanks for using our service")
            print("The cost of shipping your item is: ", cost)
        else:
            print("Invalid Input")
    elif item_type == 6:
        print("Since the item is a medical item and its fragile yet we understand the medical items are neccessary for you we will not charge any additional charges from you")
        print("Thanks for using our service")
        print("The cost of shipping your item is: ", cost)
    else:
        print("Invalid Input")
def stores():#stores function
    global Buyer
    Buyer[name] = {"Address": address, "Item": item_name, "Weight": weight, "Distance": distance, "Cost": cost}
    json_data = json.dumps(Buyer)
    with open('py.json', 'w') as file:
        file.write(json_data)
def load():
    global Buyer
    with open('py.json', 'r') as file:
        data = file.read()
        Buyer = json.loads(data)
def main():
    import sys
    while True:
        print("Welcome to American Shipment Company")
        print('''Our Branches Location Cordinates are:
        1. ( 28.642966802735483, 77.2190250237659 )
        2. ( 42.99159002797445, -78.70605469543624 ) 
        3. ( 53.777932356167625, -60.973767135984616 )
        4. ( 28.585062835728753, 77.00110368094337 )''')
        print("You just have to copy the coordinates and paste it in Google Maps and put your real time location and distance will be calculated")
        print("Enter that calculated distance in Km when asked for distance")
        print("\nPlease Enter 1.If want to buy any package")
        print("Please Enter 2.If You want to sell any package")
        print("Please Enter 3.If You have any package to be received")
        print("Please Enter 4.If You have any package to be shipped")
        print("Please Enter 5.If You want to read our terms and conditions")
        print("Please Enter 6.If You want to Exit")
        choose = int(input("Please Enter the Number of the option you want to choose: "))
        if choose == 1:
            buy()
            load()
        elif choose == 2:
            sell()
        elif choose == 3:
            receive()
        elif choose == 4:
            ship()
        elif choose == 5:
            load()
            terms()
        elif choose == 6:
            print("Thanks For Visiting ")
            sys.exit()
            break
        else:
            print("Invalid Input")

if __name__ == '__main__':
    main()

