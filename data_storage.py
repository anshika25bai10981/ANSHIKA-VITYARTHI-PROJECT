# data_storage.py

# This module holds the core data structure (in-memory) for the system.
# Data is lost when the program closes, as we are avoiding complex file I/O 
# like JSON/OS operations to meet the constraint.

# The list of dictionaries to store donation records.
# Each dictionary has: 'id', 'donor_name', 'amount', 'date'
DONATIONS = [
    {'id': 1001, 'donor_name': 'Anya Sharma', 'amount': 500.00, 'date': '2024-11-01'},
    {'id': 1002, 'donor_name': 'Ben Carter', 'amount': 150.50, 'date': '2024-11-05'},
    {'id': 1003, 'donor_name': 'Anya Sharma', 'amount': 1000.00, 'date': '2024-11-10'},
    {'id': 1004, 'donor_name': 'Chris Jones', 'amount': 50.00, 'date': '2024-11-15'},
    {'id': 1005, 'donor_name': 'Ben Carter', 'amount': 500.00, 'date': '2024-11-20'},
]

# Simple counter for generating unique IDs
NEXT_ID = 1006

def get_donations():
    """Returns the main list of donation records."""
    return DONATIONS

def generate_new_id():
    """Increments and returns the next available unique ID."""
    global NEXT_ID
    new_id = NEXT_ID
    NEXT_ID += 1
    return new_id