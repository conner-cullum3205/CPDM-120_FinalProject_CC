class Rental:

    next_ID = 1  # Class variable to keep track of the next available ID number

    def __init__(self, customer_id, skis_rented, snowboards_rented, rental_duration):
        self.customer_id = customer_id
        self.skis_rented = skis_rented
        self.snowboards_rented = snowboards_rented
        self.rental_duration = rental_duration
        self.rental_id = Rental.next_ID
        Rental.next_ID += 1

        self.is_closed = False  # Initialize the rental as open

    def display(self):
        print(f"Rental ID: {self.rental_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Skis Rented: {self.skis_rented}")
        print(f"Snowboards Rented: {self.snowboards_rented}")
        print(f"Rental Duration: {self.rental_duration} days")
        if self.is_closed:
            print("Rental Status: Closed")
        else:
            print("Rental Status: Open")