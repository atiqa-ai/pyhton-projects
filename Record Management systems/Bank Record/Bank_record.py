# Simple Banking Records Manager using Classes and Objects
# This program manages banking records (e.g., account details) using file handling.

class BankingManager:
    # The __init__ method is the constructor that initializes the object.
    def __init__(self, filename):
        self.filename = filename
    
    # This method adds a new bank account record to the file.
    def add_account(self):
        # Ask the user for the account number (assume it's unique).
        account_number = input("Enter account number: ")
        
        # Ask for the account holder's name.
        name = input("Enter account holder name: ")
        
        # Ask for the initial balance (as a float for decimal values).
        balance = input("Enter initial balance: ")
        
        # If the file doesn't exist, it will be created.
        with open(self.filename, 'a') as f:
            # Write the record in the format: AccountNumber,Name,Balance followed by a newline.
            f.write(f"{account_number},{name},{balance}\n")
        
        # Inform the user that the account was added.
        print("Bank account added successfully!")
    
    # This method views all bank account records from the file.
    def view_accounts(self):
        # Try to open the file in read mode.
        try:
            with open(self.filename, 'r') as f:
                # Read all lines from the file.
                lines = f.readlines()
            
            # Check if there are any records.
            if not lines:
                print("No bank accounts found.")
            else:
                # Print a header for clarity.
                print("Bank Account Records:")
                print("Account Number\tName\t\tBalance")
                print("-" * 40)
                
                # Loop through each line and display the record.
                for line in lines:
                    # Remove any trailing newline and split by comma to get AccountNumber, Name, Balance.
                    parts = line.strip().split(',')
                    if len(parts) == 3:  # Ensure the line has exactly 3 parts.
                        account_number, name, balance = parts
                        # Print in a formatted way (using tabs for alignment).
                        print(f"{account_number}\t\t{name}\t\t{balance}")
                    else:
                        # If the line is malformed, skip it and print a warning.
                        print(f"Skipping invalid record: {line.strip()}")
        
        # If the file doesn't exist, inform the user.
        except FileNotFoundError:
            print("No bank records file found. Please add some accounts first.")

# The main function is the entry point of the program.
def main():
    # Set the filename for storing bank records.
    filename = "bank_accounts.txt"
    
    manager = BankingManager(filename)
    
    # Start an infinite loop to keep the program running until the user chooses to exit.
    while True:
        # Display the menu options.
        print("\nBanking Records Manager")
        print("1. Add a new account")
        print("2. View all accounts")
        print("3. Exit")
        
        # Ask the user to choose an option.
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            # Call the add_account method on the manager object.
            manager.add_account()
        elif choice == '2':
            # Call the view_accounts method on the manager object.
            manager.view_accounts()
        elif choice == '3':
            # Exit the program.
            print("Exiting the program. Goodbye!")
            break  
        else:
            # If the user enters something invalid, show an error.
            print("Invalid choice. Please enter 1, 2, or 3.")

# This ensures the main function runs when the script is executed directly.
if __name__ == "__main__":
    main()
