# Create a Bank class with the following attributes:
# bank_name
# bank_address
# bank_telephone
# customer_list
# account_list

from customer import Customer
from account import Account
from loan import LoanApplication

class Bank:
  def __init__(self, name, address, tel):
    self.name = name
    self.address = address
    self.tel = tel
    self.customer_list = []
    self.account_list = []
    self.loan_application_list = []
    self.loan_list = []

  # Create a new customer with the following attributes:
  # customer_id
  # customer_name
  # customer telephone number
  # customer email
  def create_customer(self, id, name, tel, email):
    new_customer = Customer(id, name, tel, email)
    self.customer_list.append(new_customer)

  # Create an account for a customer with the following attributes:
  # account_number
  # balance
  # customer_id
  def create_account(self, account_number, customer_id):
    new_account = Account(account_number, customer_id)
    self.account_list.append(new_account)

  # Create a new customer and a new account for this new customer
  # customer_id
  # customer_name
  # customer telephone number
  # customer email
  # account_number
  # balance
  # customer_id
  def create_customer_and_account(self, customer_id, customer_name,
    customer_tel, customer_email, account_number):
    self.create_customer(customer_id, customer_name, customer_tel, customer_email)
    self.create_account(account_number, customer_id)

  # Show customer list
  def show_customer_list(self):
    for customer in self.customer_list:
      # rint(customer.id, customer.name, customer.tel, customer.email)
      print(f"Name: {customer.id}, ID: {customer.name}, Tel: {customer.tel}, Email: {customer.email}")

  # Show customer list
  def show_account_list(self):
    for account in self.account_list:
      # print(account.number, account.customer_id, account.balance)
      print(f"Account number: {account.number}, Customer ID: {account.customer_id}, Balance: {account.balance}")
    
  # Show the details of the bank
  def show_details(self):
    print('\n=============\n')
    print("Bank name: " + self.name)
    print("Bank address: " + self.address)
    print("Bank telephone: " + self.tel)
    print("\nCustomer list: ")
    self.show_customer_list()
    print("\nAccount list: ")
    self.show_account_list()
    print("\nLoan Application list: ")
    self.show_loan_application_list()
    print("\nLoan list: ")
    self.show_loan_list()

  # Search for an account by account number
  def search_account_by_number(self, account_number):
    for account in self.account_list:
      if account.number == account_number:
        return account
    return None
    
  # Allow a customer to deposit by giving his account number and the amount
  def deposit(self, account_number, amount):
    account = self.search_account_by_number(account_number)
    if account: # If found an account with this number
      account.deposit(amount)
      print(f'\n{amount} was deposited to this account number {account_number}.')
    else:
      print(f'\nNo account with this number is {account_number} found')
    
  # Allow a customer to withdraw by giving his account number and the amount
  def withdraw(self, account_number, amount):
    account = self.search_account_by_number(account_number)
    if account: # If found an account with this number
      account.withdraw(amount)
      print(f'\n{amount} was withdrew from this account number {account_number}.')
    else:
      print(f'\nNo account with this number {account_number} is found')
    
  # Allow a customer to make a transfer from his/her account
  # to another account
  # by giving his/her account number, the target account number, and the amount
  def transfer_to(self, from_account_number, to_account_number, amount):
    from_account = self.search_account_by_number(from_account_number)
    to_account = self.search_account_by_number(to_account_number)
    if from_account and to_account: # If from_account and to_account were found, make transfer
      from_account.transfer_to(to_account, amount)
      print(f'\n{amount} was transfered from this account number {from_account_number} to this account number {to_account_number}')
    else:
      print(f'\nCannot find {from_account_number}/{to_account_number}')

  # Show Loan Application list
  def show_loan_application_list(self):
    for application in self.loan_application_list:
      application.show_details()
      
  # Show Loan list
  def show_loan_list(self):
    for loan in self.loan_list:
      loan.show_details()
    
  # Allow to apply for a loan
  def apply_loan(self, amount, term, rate, customer_id):
    new_loan_application = LoanApplication(amount, term, rate, customer_id)
    # new_loan_application = LoanApplication.apply_loan(self,amount, term, rate, customer_id)
    self.loan_application_list.append(new_loan_application)

  # Search a loan application by ID
  def search_loan_application(self, id):
    for application in self.loan_application_list:
      if application.id == id:
        return application
    return None
    
  # Allow to approve a loan
  def approuve_loan(self, loan_application_id):
    loan_application = self.search_loan_application(loan_application_id)
    if loan_application: # If found
      new_loan = loan_application.approuve_loan(loan_application.id)
      self.loan_list.append(new_loan)
    else:
      print(f'\nNo Loan Application with this ID {loan_application_id} exists')

  # Allow to reject a loan
  def reject_loan(self, loan_application_id):
    loan_application = self.search_loan_application(loan_application_id)
    if loan_application: # If found
      loan_application.reject_loan(loan_application.id)
    else:
      print(f'\nNo Loan Application with this ID {loan_application_id} exists')