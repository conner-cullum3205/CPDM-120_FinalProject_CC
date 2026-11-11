from rental import Rental
from customer import Customer

class Shop:

    def __init__(self, num_skis = 10, num_snowboards = 10, customer_list = [], rental_list = [], total_income = 0):
        self.num_skis = num_skis
        self.num_snowboards = num_snowboards
        self.customer_list = customer_list
        self.rental_list = rental_list
        self.total_income = total_income

        self.setup_inventory(num_skis, num_snowboards)

    def find_customer(self, customer_ID):
        for customer in self.customer_list:
            if customer.customer_ID == customer_ID:
                return customer
        return None

    def find_rental(self, rental_id):
        for rental in self.rental_list:
            if rental.rental_id == rental_id:
                return rental
        return None

    def find_rentals_for_customer(self, customer_id):
        rentals_for_customer = []
        for rental in self.rental_list:
            if rental.customer_id == customer_id:
                rentals_for_customer.append(rental)
        return rentals_for_customer

    def add_customer(self, name, phone_number):
        new_customer = Customer(name, phone_number)
        self.customer_list.append(new_customer)
        return new_customer

    def new_rental(self, customer_id, skis_rented, snowboards_rented, rental_duration):
        if skis_rented > self.num_skis or snowboards_rented > self.num_snowboards:
            print("Not enough equipment available for this rental.")
            return None
        new_rental = Rental(customer_id, skis_rented, snowboards_rented, rental_duration)
        self.rental_list.append(new_rental)
        self.num_skis -= skis_rented
        self.num_snowboards -= snowboards_rented
        return new_rental

    def complete_rental(self, rental_id):
        rental = self.find_rental(rental_id)
        if rental is None:
            print("Rental not found.")
            return
        if rental.is_closed:
            print("Rental is already closed.")
            return
        rental.is_closed = True
        self.num_skis += rental.skis_rented
        self.num_snowboards += rental.snowboards_rented
        income = (rental.skis_rented + rental.snowboards_rented) * rental.rental_duration * 10  # Assuming $10 per day per item
        self.total_income += income
        print(f"Rental completed. Total income from this rental: ${income}")

    def setup_inventory(self, num_skis, num_snowboards):
        self.num_skis = num_skis
        self.num_snowboards = num_snowboards