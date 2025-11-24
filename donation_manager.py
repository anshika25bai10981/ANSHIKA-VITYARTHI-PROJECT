# donation_manager.py

import data_storage

def add_donation(name, amount, date):
    """
    Creates a new donation record and adds it to the data storage.
    
    Args:
        name (str): The name of the donor.
        amount (float): The donation amount.
        date (str): The donation date (e.g., YYYY-MM-DD).
    """
    donations = data_storage.get_donations()
    new_id = data_storage.generate_new_id()
    
    # Create the new donation dictionary
    new_donation = {
        'id': new_id, 
        'donor_name': name, 
        'amount': amount, 
        'date': date
    }
    
    # Add to the in-memory list
    donations.append(new_donation)
    return new_id

def view_all_donations():
    """Returns the list of all donation records."""
    return data_storage.get_donations()

def find_donation_by_id(donation_id):
    """
    Searches for a specific donation by its ID.
    
    Args:
        donation_id (int): The ID to search for.
        
    Returns:
        dict or None: The matching donation dictionary, or None if not found.
    """
    donations = data_storage.get_donations()
    for donation in donations:
        if donation['id'] == donation_id:
            return donation
    return None