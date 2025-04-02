#Welcome to my party maker
import json
import sys
import random

guest_list = []


#All THE Functions:
def main():
    while True:
        print("Welcome to my party maker")
        print("Please Enter 1.If you want to add a guest")
        print("Please Enter 2.If you want to remove a guest")
        print("Please Enter 3.If you want to see the guest list")
        print("Please Enter 4.If you want to permanently save the guest list")
        print("Please Enter 5.If you want to permanently delete the guest list")
        print("Enter 6 to activate the party maker calculator")
        print("Enter 7 if you want to rent an apartment for your party")
        print("Enter 8 to activate the party planner automative service")
        print("Please Enter 9.If you want to Exit")
        choice = int(input("Please Enter the Number of the option you want to choose: "))
        if choice == 1:
            add_guest()
        elif choice == 2:
            remove_guest()
        elif choice == 3:
            see_guest()
        elif choice == 4:
            save_guest()
        elif choice == 5:
            delete_guest()
        elif choice == 6:
            party_calculator()
        elif choice == 7:
            apartment()
        elif choice == 8:
            party_automative()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")


def add_guest():
    name = input("Enter the name of the guest: ")
    guest_list.append(name)
    print(f"{name} has been added to the guest list.")
    save_guest()

def remove_guest():
    name = input("Enter the name of the guest to remove: ")
    if name in guest_list:
        guest_list.remove(name)
        print(f"{name} has been removed from the guest list.")
    else:
        print(f"{name} is not in the guest list.")
        save_guest()

def see_guest():
    print("Guest List:")
    for guest in guest_list:
        print(guest)

def save_guest():
    with open("guest_list.json", "w") as file:
        json.dump(guest_list, file)
    print("Guest list has been saved to guest_list.json.")

def delete_guest():
    guest_list.clear()
    print("Guest list has been deleted.")
    with open("guest_list.json", "w") as file:
        json.dump(guest_list, file)
    print("Guest list has been deleted and saved to guest_list.json.")
    save_guest()
def load_guest():
    try: 
        with open("guest_list.json","r") as file:
            json_data = json.load(file)
            guest_list = json_data
            return guest_list
    except FileNotFoundError:
        return [],print("Guest list not found.")


def apartment():
    print("Welcome to the apartment rental service!")
    print("Enter 1 to rent an apartment for a party.")
    print("Enter 2 to exit.")
    choice = int(input("Please Enter the Number of the option you want to choose: "))
    if choice == 1:
        budget = int(input("Enter your budget: "))
        if budget < 1000:
            print("Sorry, your budget is too low to rent an apartment for a party.")
            return
        if budget > 10000:
            print("You have chosen to rent an apartment you hav choosen best appartment for the party.")
            print("Please enter the number of days you want to rent the apartment.")
            days = int(input("Enter the number of days: "))
            print(f"You have chosen to rent the apartment for {days} days.")
            print("Please enter the number of people in your party.")
            room_cost_total = budget*days
            people = int(input("Enter the number of people: "))
            print(f"You have chosen to rent the apartment for {people} people.")
            print("Your total cost for the apartment is: ", room_cost_total)
            room_cost_total = room_cost_total/people
            print("Your cost for each person is: ", room_cost_total)
            sys.exit()
        if budget > 1000 and budget < 10000:
            print("You have chosen to rent an apartment you hav choosen best appartment for the party.")
            print("Please enter the number of days you want to rent the apartment.")
            days = int(input("Enter the number of days: "))
            print(f"You have chosen to rent the apartment for {days} days.")
            print("Please enter the number of people in your party.")
            room_cost_total = budget*days
            people = int(input("Enter the number of people: "))
            print(f"You have chosen to rent the apartment for {people} people.")
            print("Your total cost for the apartment is: ", room_cost_total)
            room_cost_total = room_cost_total/people
            print("Your cost for each person is: ", room_cost_total)
            sys.exit()
        if budget > 15000:
            print("You have chosen to rent an apartment you hav choosen best appartment for the party.")
            print("Please enter the number of days you want to rent the apartment.")
            days = int(input("Enter the number of days: "))
            print(f"You have chosen to rent the apartment for {days} days.")
            print("Please enter the number of people in your party.")
            room_cost_total = budget*days
            people = int(input("Enter the number of people: "))
            print(f"You have chosen to rent the apartment for {people} people.")
            print("Your total cost for the apartment is: ", room_cost_total)
            room_cost_total = room_cost_total/people
            print("Your cost for each person is: ", room_cost_total)
            sys.exit()
        if budget > 15000 and budget < 50000:
            print("You have chosen to rent an apartment you hav choosen best appartment for the party.")
            print("Please enter the number of days you want to rent the apartment.")
            days = int(input("Enter the number of days: "))
            print(f"You have chosen to rent the apartment for {days} days.")
            print("Please enter the number of people in your party.")
            room_cost_total = budget*days
            people = int(input("Enter the number of people: "))
            print(f"You have chosen to rent the apartment for {people} people.")
            print("Your total cost for the apartment is: ", room_cost_total)
            room_cost_total = room_cost_total/people
            print("Your cost for each person is: ", room_cost_total)
            sys.exit()
        if budget > 50000:
            print("You have chosen to rent an apartment you hav choosen best appartment for the party.")
            print("Please enter the number of days you want to rent the apartment.")
            days = int(input("Enter the number of days: "))
            print(f"You have chosen to rent the apartment for {days} days.")
            print("Please enter the number of people in your party.")
            room_cost_total = budget*days
            people = int(input("Enter the number of people: "))
            print(f"You have chosen to rent the apartment for {people} people.")
            print("Your total cost for the apartment is: ", room_cost_total)
            room_cost_total = room_cost_total/people
            print("Your cost for each person is: ", room_cost_total)
            sys.exit()
def party_calculator():
    while True:
        num_guests = int(input("Enter the number of guests: "))
        num_drinks = int(input("Enter the number of drinks: "))
        num_desserts = int(input("Enter the number of desserts: "))
        num_sides = int(input("Enter the number of sides: "))
        num_main = int(input("Enter the number of main dishes: "))
        cost_drinks = int(input("Enter the cost of 1 drinks: "))
        cost_desserts = int(input("Enter the cost of 1 desserts: "))
        cost_sides = int(input("Enter the cost of 1 sides: "))
        cost_main = int(input("Enter the cost of 1 main dishes: "))
        total_cost = (num_drinks * cost_drinks) + (num_desserts * cost_desserts) + (num_sides * cost_sides) + (num_main * cost_main)
        per_person_cost = total_cost / num_guests
        print(f"The total cost of the party is: ${total_cost}")
        print(f"The cost for each person is: ${per_person_cost}")
        print("Hence your overal budget is: ", per_person_cost * num_guests)
        print("Do you want to rent an apartment for your party?")
        print("Enter 1 for yes and 2 for no")
        choice = int(input("Please Enter the Number of the option you want to choose: "))
        if choice == 1:
            apartment()
        elif choice == 2:
            break
        else:
            print("Invalid choice. Please try again.")
    
def special_apartment():
    while True:
        print("Welcome tto spacial appartment selection")
        print("Caution this is a automative process which means onece you enter the process you can't go back to previous process\n""Or neither you can undo the process once you have completed the process")
        print("Please proceed only if you have a good budget for appartment rental")
        print("Please enter ok/OK to continue this process else enter no/NO to exit this process")
        choice = input("Enter your choice: ")
        if choice.lower() == "ok" or choice.upper() == "OK":
            budget= random.randint(10000,500000)
            print("You have chosen to rent an apartment you hav choosen best appartment for the party.")
            print("Please enter the number of days you want to rent the apartment.")
            days = int(input("Enter the number of days: "))
            print(f"You have chosen to rent the apartment for {days} days.")
            print("Please enter the number of people in your party.")
            room_cost_total = budget*days
            people = int(input("Enter the number of people: "))
            print(f"You have chosen to rent the apartment for {people} people.")
            print("Your total cost for the apartment is: ", room_cost_total)
            room_cost_total = room_cost_total/people
            print("Your cost for each person is: ", room_cost_total)
            sys.exit()
        elif choice.lower() == "no" or choice.upper() == "NO":
            break
def party_automative():
        while True:
            num_guests = int(input("Enter the number of guests: "))
            num_drinks = int(input("Enter the number of drinks: "))
            num_desserts = int(input("Enter the number of desserts: "))
            num_sides = int(input("Enter the number of sides: "))
            num_main = int(input("Enter the number of main dishes: "))
            cost_drinks = int(input("Enter the cost of 1 drinks: "))
            cost_desserts = int(input("Enter the cost of 1 desserts: "))
            cost_sides = int(input("Enter the cost of 1 sides: "))
            cost_main = int(input("Enter the cost of 1 main dishes: "))
            total_cost = (num_drinks * cost_drinks) + (num_desserts * cost_desserts) + (num_sides * cost_sides) + (num_main * cost_main)
            per_person_cost = total_cost / num_guests
            print(f"The total cost of the party is: ${total_cost}")
            print(f"The cost for each person is: ${per_person_cost}")
            print("Hence your overal budget is: ", per_person_cost * num_guests)
            print("Do you want to rent an apartment for your party?")
            print("Enter 1 for yes and 2 for no")
            choice = int(input("Please Enter the Number of the option you want to choose: "))
            if choice == 1:
                special_apartment()
            elif choice == 2:
                break
            else:
                print("Invalid choice. Please try again.")
                sys.exit()

if __name__ == "__main__":
    main()

