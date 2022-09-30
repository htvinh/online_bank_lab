# Create an account class that has the following attributes:
# account_number
# balance
# customer id
# customer name
# transaction_list with transaction details

class Account:
    def __init__(self, account_number, customer_id):
      self.number = account_number
      self.balance = 0.0
      self.customer_id = customer_id
      self.transaction_list = []

    def deposit(self, amount):
      self.balance += amount
      transaction = f"type: deposit, amount: {amount}, balance: {self.balance}"
      self.transaction_list.append(transaction)

    def withdraw(self, amount):
      self.balance -= amount
      # transaction = 'Withdraw ' + str(amount)
      transaction = f"type: withdraw, amount: {amount}, balance: {self.balance}"
      self.transaction_list.append(transaction)

    def transfer_to(self, to_account, amount):
      self.balance -= amount
      to_account.deposit(amount)
      transaction = f"type: transfer, to_account: {to_account.number}, amount: {amount}, balance: {self.balance}"
      self.transaction_list.append(transaction)
      
    def show_details(self):
      print("Account number: " + self.number)
      print("Balance: " + str(self.balance))
      print("Customer ID: " + self.customer_id)
      print("Customer name: " + self.customer_name)
      print("Transaction list: ")
      print(self.transaction_list)
