# To test if Customer class works

from customer import Customer

# Create a Bob customer with
# id = 'C12345', 
# name = 'Bob', 
# tel = '123456789', 
# email = 'bob@gmail.com'
bob = Customer('C12345', 'Bob', '123456789', 'bob@gmail.com')
# Display Bob's details
bob.show_details()
id = 'C12345'
name = 'Bob'
tel = '123456789'
email = 'bob@gmail.com'
bob = Customer(id, name, tel, email)

bob = Customer()


# Create a Alice customer with
# id = 'C23456', 
# name = 'Alice', 
# tel = '8989778', 
# email = 'alice@gmail.com'
print('\n\n')
print('Please provide customer infos')
id = input('Customer ID ? ')
name = input('Customer Name ? ') 
tel = input('Customer Tel ? ')
email = input('Customer email ? ')
alice = Customer(id, name, tel, email)
alice.show_details()
tel = input('Customer Tel ? ')
alice.tel = tel
alice.show_details()