# Create Loan class with the following attributes:
# # loan_id
# # loan_amount
# # loan_term
# # loan_rate
# # customer_id

class Loan:
  counter = 0 # To simplify the generation of the Loan ID
  def __init__(self, amount, term, rate, customer_id):
    Loan.counter += 1
    id = Loan.counter
    self.id = id
    self.amount = amount
    self.term = term
    self.rate = rate
    self.customer_id = customer_id

  def show_details(self):
    print("Loan ID: ", self.id)
    print("Loan amount: ", self.amount)
    print("Loan term: ", self.term)
    print("Loan rate: ", self.rate)
    print("Customer ID: ", self.customer_id)
    print('\n')

# A class for Loan Application
class LoanApplication():
  counter = 0 # To simplify the generation of the Loan Application ID
  def __init__(self, amount, term, rate, customer_id):
    LoanApplication.counter += 1 
    id = LoanApplication.counter
    self.id = id
    self.amount = amount
    self.term = term
    self.rate = rate
    self.status = 'New' # 'Approuved', 'Rejected'
    self.customer_id = customer_id
    print('\nA new Loan Application is created')
    self.show_details()

  # Apply for a loan
  def apply_loan(self, amount, term, rate, customer_id):
    new_loan_application = LoanApplication(amount, term, rate, customer_id)
    print('\nA new Loan Application is created')
    new_loan_application.show_details()
    return new_loan_application
    
  # Approuve a loan
  def approuve_loan(self, id):
    amount = self.amount
    rate = self.rate
    term = self.term
    customer_id = self.customer_id
    new_loan = Loan(amount, term, rate, customer_id)
    print(f'\nCreate a new loan for this customer {customer_id}')
    new_loan.show_details()
    self.status = 'Approuved'
    return new_loan

  # Reject a loan
  def reject_loan(self, id):
    print(f'\nThe Loan Application with ID {id} is rejeted')
    self.status = 'Rejected'

  # Show LoanApplication details
  def show_details(self):
    print("Application ID: ", self.id)
    print("Loan amount: ", self.amount)
    print("Loan term: ", self.term)
    print("Loan rate: ", self.rate)
    print("Customer ID: ", self.customer_id)
    print("Status : ", self.status)
    print('\n')

    