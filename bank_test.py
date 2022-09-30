# To test Bank class

from bank import Bank

# Create a new bank with:
# name = 'IFI Bank'
# address = '144 Xuan Thuy'
# tel = '1234567'

name = 'IFI Bank'
address = '144 Xuan Thuy'
tel = '1234567'
ifi_bank = Bank(name, address, tel)

ifi_bank.show_details()

# Create a new customer Bob and open for him an account with the account number is his tel.
# id = 'C12345', 
# name = 'Bob', 
# tel = '123456789', 
# email = 'bob@gmail.com'

bob_id = 'C12345'
name = 'Bob'
tel = '123456789' 
email = 'bob@gmail.com'
account_number = tel
ifi_bank.create_customer_and_account(bob_id, name, tel, email, account_number)
ifi_bank.show_details()

# Create a new customer Alice and open for her an account with the account number is her tel.
# id = 'C23456', 
# name = 'Alice', 
# tel = '8989778', 
# email = 'alice@gmail.com'

alice_id = 'C23456'
name = 'Alice'
tel = '8989778' 
email = 'alice@gmail.com'
account_number = tel
ifi_bank.create_customer_and_account(alice_id, name, tel, email, account_number)
ifi_bank.show_details()

# Bob wants to deposit 500 USD to his account
bob_account_number = '123456789'
amount = 500
ifi_bank.deposit(bob_account_number, amount)
ifi_bank.show_details()

# Bob wants to withdraw 100 USD from his account
bob_account_number = '123456789'
amount = 100
ifi_bank.withdraw(bob_account_number, amount)
ifi_bank.show_details()

# Bob wants to transfer 150 USD from his account to Alice account
bob_account_number = '123456789'
amount = 150
alice_account_number = '8989778'
ifi_bank.transfer_to(bob_account_number, alice_account_number, amount)
ifi_bank.show_details()

# Bob wants to apply for a loan with:
# amount = 1000 USD
# rate = 10 # Percent
# term = 6 # months
amount = 1000 # USD
rate = 10 # Percent
term = 6 # months
ifi_bank.apply_loan(amount, term, rate, bob_id)
ifi_bank.show_details()

# IFI Bank approuves Bob Loan Application
bob_loan_application_id = 1
ifi_bank.approuve_loan(bob_loan_application_id)
ifi_bank.show_details()

# Alice wants to apply for a loan with:
# amount = 1000 USD
# rate = 5 # Percent
# term = 12 # months
amount = 800 # USD
rate = 7 # Percent
term = 12 # months
ifi_bank.apply_loan(amount, term, rate, alice_id)
ifi_bank.show_details()

# IFI Bank rejects Alice Loan Application
alice_loan_application_id = 2
ifi_bank.reject_loan(alice_loan_application_id)
ifi_bank.show_details()