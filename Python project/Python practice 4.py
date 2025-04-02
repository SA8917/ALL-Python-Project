#Flight management system
import json
import sys
import random

flights = {}
passengers = {}

def add_flight():
    flight_number = random.randint(10000000, 99999999)
    flight_number = str(flight_number)
    destination = input("Enter the destination: ")
    flights[flight_number] = destination
    print(f"Flight {flight_number} from {destination} added successfully.")
    save_info()
def remove_flight():
    flight_number = input("Enter the flight number to remove: ")
    if flight_number in flights:
        del flights[flight_number]
        print(f"Flight {flight_number} removed successfully.")
        print("flight tooked off successfully")
        save_info()
    else:
        print(f"Flight {flight_number} not found.")
def save_info():
    try:
        with open('flights.json', 'w') as storage:
            json.dump(flights, storage)
    except Exception as e:
        print(f"An error occuerred while saving info: {e}")

def save_info_passengers():
    try:
        with open('passengers.json', 'w') as storage:
            json.dump(passengers, storage)
    except Exception as e:
        print(f"An error occuerred while saving info: {e}")

def load_info_passengers():
    global passengers
    try:
        with open('passengers.json', 'r') as storage:
            passengers = json.load(storage)
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        passengers = {}
    except Exception as e:
        print(f"An error occurred while loading info: {e}")
        passengers = {}
def load_info():
    global flights
    try:
        with open('flights.json', 'r') as storage:
            flights = json.load(storage)
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        flights = {}
    except Exception as e:
        print(f"An error occurred while loading info: {e}")
        flights = {}
def display_flights():
    for flight_number, destination in flights.items():
        print(f"Flight: {flight_number}, Destination: {destination}")
def Ticket_ganerator():
    while True:
        display_flights()
        a=input("Enter the Flight Number you want to book: ")
        c=input("Enter your name: ")
        if a in flights:
            try:
                ticket=random.randint(1000,9999)
                return ticket, print("Flight booked successfully"),print(f"{c}, your ticket number is {ticket} for flight {a}"), save_info()
            except:
                print("Error in ticket generation")
        else:
            print("Flight not found")
            break
def display_passengers():
    load_info_passengers()
    for ticket_number, details in passengers.items():
        print(f"Ticket Number: {ticket_number}, Name: {details['Name']}, Flight: {details['Flight']}")

#All the functions
def authentication():
    while True:
        I=int(input("Enter your Flight Ticket no: "))
        L=input("Enter your Name: ")
        C=input("Enter your flight number: ")
        if C in flights():
            passengers[I]={"Name":L,"Flight":C}
        if I in flights():
            print("Authentication Successfull")
            save_info_passengers()

        else:
            print("Authentication Failed")
            print("Try again and Enter valid details")
            break

def main():
    while True:
        load_info()
        print("\nWelcome to Flight Management System")
        print("1. Display Flights")
        print("2. Ticket Generator")
        print("3. Authentication to your Flight Ticket")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_flights()
        elif choice == "2":
            Ticket_ganerator()
        elif choice == "3":
            authentication()
        elif choice == "4":
            break
        elif choice == "5":
            add_flight()
        elif choice == "6":
            remove_flight()
        elif choice == "7":
            display_passengers()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()