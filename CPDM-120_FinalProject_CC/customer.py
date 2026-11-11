class Customer:

    next_ID = 1  # Class variable to keep track of the next available ID number

    def __init__(self, last_name, phone_number):
        self.last_name = last_name
        self.phone_number = phone_number
        self.customer_ID = Customer.next_ID
        Customer.next_ID += 1   

    def display(self):
        print(f"Customer Name: {self.last_name}")
        print(f"Phone Number: {self.phone_number}") 
        print(f"ID Number: {self.customer_ID}")
