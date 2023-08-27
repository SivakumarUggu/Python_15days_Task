#6. Given a JSON file with customer data, create a customer class to store and manipulate the data.
import json


class Customer:


    with open('/Python_In_15days_ Q&A/Customer_Data.json', 'r') as file1:
            data=json.load(file1)


import json

class Customer:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

class CustomerDatabase:
    def __init__(self, json_file):
        self.customers = self.load_customers_from_json(json_file)

    def load_customers_from_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            customers = [Customer.from_json(customer_data) for customer_data in data]
            return customers

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def get_all_customers(self):
        return self.customers

# Create an instance of the CustomerDatabase class
customer_db = CustomerDatabase('customer_data.json')

# Example usage
all_customers = customer_db.get_all_customers()
for customer in all_customers:
    print(f"Customer ID: {customer.id}")
    print(f"Name: {customer.name}")
    print(f"Email: {customer.email}")
    print(f"Phone: {customer.phone}")
    print("=" * 20)
