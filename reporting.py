# reporting.py

def calculate_total_donations(donations):
    """
    Calculates the grand total of all donation amounts.
    
    Returns:
        float: The sum of all donation amounts.
    """
    total = 0.0
    for donation in donations:
        total += donation['amount']
    return total

def count_donations(donations):
    """
    Counts the total number of donation records.
        
    Returns:
        int: The number of records in the list.
    """
    count = 0
    for _ in donations:
        count += 1
    return count

def get_top_donor(donor_summary):
    """
    Finds the donor who has contributed the highest total amount.
    
    Returns:
        tuple or None: (donor_name: str, total_amount: float) of the top donor, 
                       or None if the summary is empty.
    """
    if not donor_summary:
        return None
        
    top_donor_name = ""
    max_amount = -1.0
    
    # Iterates through keys and values in the dictionary
    for name in donor_summary:
        amount = donor_summary[name]
        
        if amount > max_amount:
            max_amount = amount
            top_donor_name = name
            
    return (top_donor_name, max_amount)