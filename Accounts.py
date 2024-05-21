""" Create an Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance

    # This method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the account"""
        self.interest = interest
        
        #ADDING:
        
        from Accounts import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance."""
    account = Account(balance, 0)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    updated_balance = balance + interest_earned
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)
    return updated_balance, interest_earned

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance."""
    account = Account(balance, 0)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    updated_balance = balance + interest_earned
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)
    return updated_balance, interest_earned

def main():
    """Main function to interact with the user and display account information."""
    
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings account interest rate (APR): "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f"Savings Account - Interest Earned: ${interest_earned_savings:.2f}, Updated Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD account interest rate (APR): "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print(f"CD Account - Interest Earned: ${interest_earned_cd:.2f}, Updated Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
