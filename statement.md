# 🎯DonorFlow: Project Statement

 ## 1. Problem Statement

Non-Governmental Organizations (NGOs), especially those in their early stages or operating with minimal technical infrastructure, require a simple, accessible, and lightweight tool for tracking and summarizing incoming financial donations. Existing solutions are often complex, costly, or rely on external dependencies that are difficult to manage. The core problem is the need for a fundamental, dependency-free system to maintain essential donation records and generate immediate, critical financial insights (like total funds received and top donors) without relying on persistent storage or complex libraries.

## 2. 🌐 Scope of the Project
The project is strictly scoped to be a **command-line interface (CLI)** application built entirely using fundamental Python data structures (lists and dictionaries) and basic I/O functions.
* **Inclusions**:
* Recording donor name, amount, and date for each donation.
* Displaying a full list of all recorded transactions.
* Calculating and summarizing the total donations per unique donor.
* Generating high-level reports: Grand Total of all donations and the identification of the single Top Donor.
* Modular architecture across five distinct Python files.

## 3. 👥 Target Users
* **Small/Start-up NGOs**: Organizations with limited IT resources and budget that need an immediate, free, and simple tracking solution.
* **Fundraising/Finance Teams**: Staff members responsible for recording daily donations and needing quick, ad-hoc financial summaries.
* **Educators/Students**: Individuals learning Python fundamentals who need a practical, real-world application built exclusively with core language concepts.

## 4. ✨ High-Level Features 

| Feature Name     | Description                                                                                                              | Core Technology/Concept                                                           |
|------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Add Donations    | Allows users to input and record new donation entries (name, amount, date) into the in-memory data structure.            | Basic `input()` function and List/Dictionary manipulation.                        |
| View Records     | Displays a formatted, sequential list of every single donation transaction currently held in memory.                     | Basic `print()` and looping through the master list.                              |
| Donor Summary    | Calculates and presents the aggregated total amount contributed by each unique donor across all transactions.            | Dictionary key-value pairing for aggregation and looping.                         |
| Key Reports      | Generates crucial organizational metrics, including the total funds received and the identification of the top donor.   | Arithmetic operations, looping, and conditional logic.                            |
| Modular Design   | Application logic is cleanly separated into five Python files (`data_storage`, `donation_manager`, `donor_manager`, `reporting`, `main_app`). | Python `import` mechanism.                                                          |
