# donor_manager.py

import data_storage

def get_unique_donors():
    """
    Extracts a list of unique donor names from all donations.
    
    Returns:
        list: A list of unique donor name strings.
    """
    donations = data_storage.get_donations()
    unique_names = []
    
    # Simple loop to collect unique names without using 'set'
    for donation in donations:
        name = donation['donor_name']
        is_unique = True
        for existing_name in unique_names:
            if name == existing_name:
                is_unique = False
                break
        if is_unique:
            unique_names.append(name)
            
    return unique_names

def get_donor_summary():
    """
    Calculates the total amount donated by each unique donor.
    
    Returns:
        dict: A dictionary where keys are donor names (str) and values 
              are the total amounts donated (float).
    """
    donations = data_storage.get_donations()
    donor_totals = {}
    
    for donation in donations:
        name = donation['donor_name']
        amount = donation['amount']
        
        if name in donor_totals:
            # Update existing total
            donor_totals[name] += amount
        else:
            # Start new total
            donor_totals[name] = amount
            
    return donor_totals