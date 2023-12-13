# Intialisation. Obviously, this seems to be a very American so we will have a checking account.
checking_balance = 0
savings_balance = 0

# Function for checking the balance
# account_type - string
# checking_balance - float
# savings_balance - float
def checking_balance(account_type, checking_balance, savings_balance):
  if account_type == "checking_balance":
    balance = checking_balance

  elif: account_type == "savings_balance":
    balance = savings_balance

  else:
    return error

  # I separated balance into it's own thing as a def needs a return statement or it goes to None. Then I will return it.
  balance = "Your balance for " + {account_type} + " is $" + {balance}
  return balance
  
# Function for depositing money into the account
def deposit_money(account_type, amount, checking_balance, savings_balance):

# Function for withdrawal of money
