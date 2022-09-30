# Create a Customer class with the following attributes:
# customer_id
# customer_name
# customer telephone number
# customer email

class Customer:
    def __init__(self, id, name, tel, email):
        self.id = id
        self.name = name
        self.tel = tel
        self.email = email

    def show_details(self):
        print("Customer ID: " + self.id)
        print("Customer name: " + self.name)
        print("Customer telephone: " + self.tel)
        print("Customer email: " + self.email)
    