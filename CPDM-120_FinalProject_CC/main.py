import os
from shop import Shop
from customer import Customer
from rental import Rental

def clear_terminal():
    print("\033[H\033[2J", end="")

shop = Shop(num_skis = 13, num_snowboards = 15, customer_list=[], rental_list=[], total_income = 0)

continue_loop = True
while continue_loop:
    clear_terminal()
    print("\nWelcome to the Ski and Snowboard Rental Shop")
    print("1. Add a new customer")
    print("2. Display customer information")
    print("3. Display customer rentals")
    print("4. Display all open rentals")
    print("5. Create a new rental")
    print("6. Close a rental")
    print("7. Display shop inventory")
    print("8. Display aggregate information")
    user_choice = input("Please select an option (1-8) or 'Q' to quit: ")
    if user_choice.upper() == 'Q':
        continue_loop = False
    elif user_choice == '1':
        last_name = input("\nEnter the customer's last name: ")
        phone_number = input("Enter the customer's phone number: ")
        new_customer = shop.add_customer(last_name, phone_number)
        print(f"Customer added with ID: {new_customer.customer_ID}")
    elif user_choice == '2':
        customer_id = int(input("Enter the customer ID: "))
        customer = shop.find_customer(customer_id)
        if customer:
            customer.display()
        else:
            print("Customer not found.")
    elif user_choice == '3':
        customer_id = int(input("\nEnter the customer ID: "))
        rentals = shop.find_rentals_for_customer(customer_id)
        if rentals:
            for rental in rentals:
                rental.display()
        else:
            print("No rentals found for this customer.")
    elif user_choice == '4':
        for rental in shop.rental_list:
            if not rental.is_closed:
                print("\n")
                rental.display()
    elif user_choice == '5':
        has_ID = input("\nDoes the customer have an ID? (Y/N): ")
        while has_ID.upper() != 'Y' and has_ID.upper() != 'N':
            print("Invalid input. Please enter 'Y' or 'N'.")
            has_ID = input("\nDoes the customer have an ID? (Y/N): ")
        if has_ID.upper() == 'Y':
            customer_id = int(input("Enter the customer ID: "))
            customer = shop.find_customer(customer_id)
            if customer:
                num_skis = int(input("Enter the number of skis to rent: "))
                num_snowboards = int(input("Enter the number of snowboards to rent: "))
                rental_duration = int(input("Enter the rental duration in hours: "))
                new_rental = shop.new_rental(customer_id, num_skis, num_snowboards, rental_duration)
            else:
                print("Customer not found.")
        elif has_ID.upper() == 'N':
            last_name = input("Enter the customer's last name: ")
            phone_number = input("Enter the customer's phone number: ")
            new_customer = shop.add_customer(last_name, phone_number)
            customer_id = new_customer.customer_ID
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    elif user_choice == '6':
        rental_id = int(input("\nEnter the rental ID to close: "))
        shop.complete_rental(rental_id)
    elif user_choice == '7':
        print(f"\nSkis available: {shop.num_skis}")
        print(f"Snowboards available: {shop.num_snowboards}")
    elif user_choice == '8':
        print(f"Total income: ${shop.total_income}")
        print(f"Total customers: {len(shop.customer_list)}")
        print(f"Total rentals: {len(shop.rental_list)}")
    else:
        print("Invalid option. Please try again.")
    if continue_loop:
        input("\nPress Enter to return to the Main Menu")