README for Katie's Customer Banking System

Overview:

The Customer Banking System is a Python application designed to help users calculate and track interest earned on savings and Certificate of Deposit (CD) accounts. This system allows users to input their account details, calculate the interest earned, and view the updated balances after a specified number of months. This README provides an overview of the project, its functionality, and the code implementation.

Project Features:

Savings Account Interest Calculation: Users can input their savings account balance, interest rate (APR), and the number of months. The system will calculate the interest earned and update the account balance accordingly.

CD Account Interest Calculation: Similar to the savings account, users can input their CD account details to calculate the interest earned and update the balance.

User Interaction: The main function interacts with the user through the console, prompting for necessary inputs and displaying the results.


Code Structure:

create_savings_account
The create_savings_account function creates a savings account, calculates the interest earned, and updates the account balance.

Parameters:
balance: Initial balance of the savings account.
interest_rate: Annual percentage rate (APR) for the savings account.
months: Duration for which interest is calculated.
Returns: Updated balance and interest earned.
create_cd_account
The create_cd_account function creates a CD account, calculates the interest earned, and updates the account balance.

Parameters:
balance: Initial balance of the CD account.
interest_rate: Annual percentage rate (APR) for the CD account.
months: Duration for which interest is calculated.
Returns: Updated balance and interest earned.
main
The main function interacts with the user and displays account information.


Functionality:

Prompts the user for savings and CD account details.
Calculates the interest earned and updates the balances.
Displays the results in a user-friendly format.
Usage

Run the application by executing the main function.
Follow the prompts to enter the necessary account details.
View the calculated interest and updated balances for both savings and CD accounts.
Potential Enhancements

GUI Integration: Develop a graphical user interface for a more user-friendly experience.
Account Persistence: Implement a database to save and retrieve account information.
Additional Account Types: Extend the application to support other types of accounts, such as checking accounts.


Conclusion:

This Customer Banking System provides a simple yet effective way to manage and track interest earned on savings and CD accounts. It demonstrates fundamental programming concepts, including user input handling, interest calculation, and basic object-oriented programming with the Account class. This project is an excellent addition to a tech portfolio, showcasing skills relevant to financial application development.


