# main_app.py

import donation_manager
import donor_manager
import reporting

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- NGO Donation Tracking System ---")
    print("1. Add New Donation")
    print("2. View All Donations")
    print("3. View Donor Summary")
    print("4. View Key Reports")
    print("5. Exit")
    print("----------------------------------")

def handle_add_donation():
    """Gathers user input and adds a new donation."""
    print("\n--- Add New Donation ---")
    name = input("Enter donor name: ")
    
    # Simple input validation for amount
    while True:
        try:
            amount_str = input("Enter amount donated (e.g., 50.00): ")
            amount = float(amount_str)
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount format. Please enter a number.")
            
    date = input("Enter date (YYYY-MM-DD): ")
    
    new_id = donation_manager.add_donation(name, amount, date)
    print(f"\nSUCCESS: Donation added with ID: {new_id}")

def handle_view_donations():
    """Displays all donation records in a formatted list."""
    donations = donation_manager.view_all_donations()
    
    if not donations:
        print("\nNo donations recorded yet.")
        return
        
    print("\n--- All Donation Records ---")
    print(f"{'ID':<6} {'Donor Name':<20} {'Amount':>10} {'Date':>12}")
    print("-" * 50)
    for d in donations:
        # Basic string formatting without f-strings (for maximum compatibility/simplicity)
        print("%-6d %-20s %10.2f %12s" % (d['id'], d['donor_name'], d['amount'], d['date']))
        
def handle_donor_summary():
    """Displays the total contributions per donor."""
    summary = donor_manager.get_donor_summary()
    
    if not summary:
        print("\nNo donor data available.")
        return
        
    print("\n--- Donor Contribution Summary ---")
    print(f"{'Donor Name':<20} {'Total Donated':>15}")
    print("-" * 35)
    
    # Simple loop to iterate and display the summary
    for name in summary:
        total = summary[name]
        print("%-20s %15.2f" % (name, total))
        
def handle_key_reports():
    """Calculates and displays simple key metrics for the NGO."""
    donations = donation_manager.view_all_donations()
    
    if not donations:
        print("\nReports cannot be generated: No donation data.")
        return
        
    total_amount = reporting.calculate_total_donations(donations)
    total_count = reporting.count_donations(donations)
    
    donor_summary = donor_manager.get_donor_summary()
    top_donor_info = reporting.get_top_donor(donor_summary)
    
    print("\n--- Key Performance Reports ---")
    print("Total Donations Received: $%.2f" % total_amount)
    print("Number of Transactions:   %d" % total_count)
    
    if top_donor_info:
        name, amount = top_donor_info
        print("Top Donor:                %s ($%.2f)" % (name, amount))
    else:
        print("Top Donor:                N/A")
    print("-----------------------------")

def main():
    """The main loop of the application."""
    print("Welcome to the NGO Donation Tracker.")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            handle_add_donation()
        elif choice == '2':
            handle_view_donations()
        elif choice == '3':
            handle_donor_summary()
        elif choice == '4':
            handle_key_reports()
        elif choice == '5':
            print("\nExiting system. Thank you for using the tracker!")
            break
        else:
            print("\nInvalid choice. Please select a number from 1 to 5.")

# This ensures the main function runs only when the file is executed directly.
if __name__ == '__main__':
    main()