import csv  # built-in module for reading/writing CSV files
import os   # built-in module for working with file pa

#STEP 1: Settings
# We build the file path from this script's own folder, so the CSV file is always saved next to the script no matter where you run it from.

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.csv")
FIELDS = ["name", "phone", "email"]  # the column headings of the CSV
 
# 5 sample records used to test the program (Task 2 requirement)
SAMPLE_CONTACTS = [
    {"name": "Ama Mensah",   "phone": "0241234567", "email": "ama@example.com"},
    {"name": "Kofi Boateng", "phone": "0207654321", "email": "kofi@example.com"},
    {"name": "Esi Owusu",    "phone": "0551112233", "email": "esi@example.com"},
    {"name": "Yaw Darko",    "phone": "0269988776", "email": "yaw@example.com"},
    {"name": "Akua Asare",   "phone": "0503344556", "email": "akua@example.com"},
]

#STEP 2: READ from the file
def load_contacts():
    """Read all contacts from the CSV file."""
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)  # reads each row as a dictionary
            return list(reader)
    except FileNotFoundError:
        # First run: the file doesn't exist yet, so start with an empty list
        return []
    except (OSError, csv.Error) as error:
        print(f"Could not read the file: {error}")
        return []

# STEP 3: WRITE to the file
def save_contacts(contacts):
    """Write all contacts to the CSV file. Returns True if it worked."""
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()          # first row: name,phone,email
            writer.writerows(contacts)    # one row per contact
        return True
    except OSError as error:
        print(f"Could not save the file: {error}")
        return False


