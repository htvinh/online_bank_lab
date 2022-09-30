from account import Account

from customer import Customer

# Create a Bob customer with
# id = 'C12345', 
# name = 'Bob', 
# tel = '123456789', 
# email = 'bob@gmail.com'
bob = Customer('C12345', 'Bob', '123456789', 'bob@gmail.com')
# Display Bob's details
bob.show_details()

# Create Alice customer with
# id = 'C23456', 
# name = 'Alice', 
# tel = '8989778', 
# email = 'alice@gmail.com'
alice = Customer('C23456', 'Alice', '8989778', 'alice@gmail.com')
alice.show_details()

# Open Account for Bob
# account_number = Customer tel
bob_account = Account(bob.tel, bob.id)
bob_account.show_details()

# Open Account for Alice
# account_number = Customer tel
alice_account = Account(alice.tel, alice.id)
alice_account.show_details()

# Bob deposits 500 USD to his account
bob_account.deposit(500)
bob_account.show_details()

# Bob withdrawlls 100 USD from his account
bob_account.withdraw(100)
bob_account.show_details()

# Bob transfers to Alice 150 USD
bob_account.transfer_to(alice_account, 150)
bob_account.show_details()
alice_account.show_details()