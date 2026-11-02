class Customer:

    next_ID = 1  # Class variable to keep track of the next available ID number

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.ID_number = Customer.next_ID
        Customer.next_ID += 1   

    def display(self):
        print(f"Customer Name: {self.name}")
        print(f"Phone Number: {self.phone_number}") 
        print(f"ID Number: {self.ID_number}")
