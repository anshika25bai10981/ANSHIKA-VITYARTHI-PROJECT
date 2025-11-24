# 💰DonorFlow: An NGO Donation Tracking System

## 🌟 Overview 

**DonorFlow** application is a simple tool designed for Non-Governmental Organizations (NGOs) to track incoming donations.
The entire system is built using only fundamental Python concepts (lists, dictionaries, loops, and basic I/O).
The data is stored in-memory, making the system lightweight and portable, but it requires careful execution as data is not persistent.

## 🚀 Key Features

* **Add Donations**: Record new donor contributions including the donor's name, the amount, and the date of the contribution.

* **View Records**: Display a comprehensive, formatted list of all recorded donation transactions.

* **Donor Summary**: Automatically calculate and view the total accumulated amount contributed by each unique donor.

* **Key Reports**: Generate high-level organizational metrics, including the grand total of all funds received and the identification of the single top donor.

* **Modular Design**: Logic is cleanly separated across five distinct Python modules for maintainability and clarity.

## 💻 Technologies/Tools Used

| Component   | Tool/Technology               | Details                                                                 |
|-------------|-------------------------------|-------------------------------------------------------------------------|
| Language    | Python 3.x                    | Used exclusively.                                                       |
| Data Storage| Python Lists & Dictionaries    | Data is stored in the application's memory (`data_storage.py`). No external databases or persistent file I/O are used. |
| Interface   | Command-Line Interface (CLI)  | User interaction is handled via standard Python `input()` and `print()` functions. |

## 🛠️ Steps to Install & Run the Project

Since this project has no external dependencies, installation is minimal.

Prerequisites

You only need a standard Python 3.x installation.

Execution

* **Organize Files**: Ensure all five Python files (```data_storage.py```, ```donation_manager.py```, ```donor_manager.py```, ```reporting.py```,and ```main_app.py```) are placed together in the same directory.

* **Open Terminal**: Open your operating system's command-line interface (CLI) or terminal application.

* **Navigate**: Use the cd command to navigate to the directory where the files are stored.

* **Run Application**: Execute the main entry point file:
```
      python main_app.py
```

* **Interact**: The main menu will appear. Follow the prompts (1-5) to use the system.

## ✅ Instructions for Testing

Since the application has built-in sample data, you can test all features immediately upon running the application.

**1. Test 2 (View All Donations)**: Run option 2 to confirm the initial 5 sample records are displayed correctly.

**2. Test 3 (View Donor Summary)**: Run option 3 to confirm that contributions from 'Anya Sharma' and 'Ben Carter' are correctly totaled.

**3. Test 4 (View Key Reports)**: Run option 4 to verify the total amount and identify the 'Top Donor'.

**4. Test 1 (Add New Donation)**:

* **Select option 1.**

* **Add a new record (e.g., Name: ```New Donor```, Amount: ```75.50```, Date: ```2025-12-01```).**

* **Re-run option 2 to confirm the new entry appears.**

* **Re-run option 4 to confirm the ```Total Donations Received``` figure has updated correctly.**
