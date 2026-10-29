File Handling Mini Project

A contact book that stores records in a CSV file.
Features: Add, View, Update, Delete (plus a sample-data loader for testing).

About the Project

This program lets you manage a list of contacts (name, phone, email). Everything is stored in a file called contacts.csv, so your contacts are still there the next time you run the program.

Features
Add a new contact
View all contacts in a numbered table
Update an existing contact (press Enter to keep the old value)
Delete a contact (with a yes/no confirmation)
Load 5 sample contacts with one menu option for quick testing
Saves and reads data from a CSV file

Error Handling:Problem	How it is handled
contacts.csv does not exist yet	The program starts with an empty list and creates the file on the first save
Empty name	Asks again
Invalid phone (letters, too short or too long)	Asks again; accepts 7-15 digits, with an optional leading +
Invalid email (no @ or no .)	Asks again
Non-numeric or out-of-range menu choice	Asks again
File cannot be read or written	Shows a friendly error message instead of crashing

Requirements
Python 3.8 or newer (uses only built-in modules: csv and os)

How to Test (5 Sample Records)
Run the program and choose 5 to load the 5 sample contacts.
Choose 2 to view them.
Choose 3 to update one and 4 to delete one.
Type invalid input on purpose (for example, letters as a phone number) to see the validation.
Choose 6 to exit, then run it again and choose 2. Your changes should still be there.

Python Concepts Used
File handling: reading and writing CSV files with the csv module
Functions
Lists and dictionaries
try / except error handling
Input validation with loops
while loop menu
