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

#STEP 4: Input helpers - these make sure the user's input is valid
def get_name(prompt="Name: "):
    """Ask for a non-empty name."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Name cannot be empty.")
 
 
def get_phone(prompt="Phone: "):
    """Ask for a phone number: digits only (a leading + is allowed), 7-15 long."""
    while True:
        phone = input(prompt).strip().replace(" ", "")
        digits = phone[1:] if phone.startswith("+") else phone
        if digits.isdigit() and 7 <= len(digits) <= 15:
            return phone
        print("Invalid phone. Use 7-15 digits, e.g. 0241234567 or +233241234567.")
 
 
def get_email(prompt="Email: "):
    """Ask for an email with a basic format check."""
    while True:
        email = input(prompt).strip()
        # Very simple check: has one '@' and a '.' after it
        if "@" in email and "." in email.split("@")[-1] and " " not in email:
            return email
        print("Invalid email. Example: name@example.com")
 
 
def get_choice(prompt, minimum, maximum):
    """Ask for a whole number between minimum and maximum."""
    while True:
        try:
            number = int(input(prompt).strip())
        except ValueError:
            print("Please enter a whole number.")
            continue
        if minimum <= number <= maximum:
            return number
        print(f"Please enter a number from {minimum} to {maximum}.")

#STEP 5: CRUD functions (Create, Read, Update, Delete)
def add_contact():
    """CREATE: add a new contact."""
    print("\n--- Add Contact ---")
    contact = {
        "name": get_name(),
        "phone": get_phone(),
        "email": get_email(),
    }
    contacts = load_contacts()
    contacts.append(contact)
    if save_contacts(contacts):
        print(f"Saved {contact['name']}.")
 
 
def view_contacts():
    """READ: show all contacts in a numbered list."""
    contacts = load_contacts()
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts yet. Add one or load the sample data.")
        return contacts
    print(f"{'No.':<4}{'Name':<20}{'Phone':<16}{'Email'}")
    print("-" * 60)
    for number, contact in enumerate(contacts, start=1):
        print(f"{number:<4}{contact['name']:<20}{contact['phone']:<16}{contact['email']}")
    return contacts
 
 
def update_contact():
    """UPDATE: change a contact's details."""
    contacts = view_contacts()
    if not contacts:
        return
 
    number = get_choice("\nEnter the number of the contact to update: ", 1, len(contacts))
    contact = contacts[number - 1]  # lists start at 0, our numbering starts at 1
 
    print(f"Updating {contact['name']}. Press Enter to keep the current value.")
    # For each field: if the user types nothing, keep the old value
    new_name = input(f"Name [{contact['name']}]: ").strip()
    if new_name:
        contact["name"] = new_name
 
    while True:
        new_phone = input(f"Phone [{contact['phone']}]: ").strip().replace(" ", "")
        if not new_phone:
            break
        digits = new_phone[1:] if new_phone.startswith("+") else new_phone
        if digits.isdigit() and 7 <= len(digits) <= 15:
            contact["phone"] = new_phone
            break
        print("Invalid phone. Use 7-15 digits.")
 
    while True:
        new_email = input(f"Email [{contact['email']}]: ").strip()
        if not new_email:
            break
        if "@" in new_email and "." in new_email.split("@")[-1] and " " not in new_email:
            contact["email"] = new_email
            break
        print("Invalid email. Example: name@example.com")
 
    if save_contacts(contacts):
        print("Contact updated.")
 
 
def delete_contact():
    """DELETE: remove a contact after asking for confirmation."""
    contacts = view_contacts()
    if not contacts:
        return
 
    number = get_choice("\nEnter the number of the contact to delete: ", 1, len(contacts))
    contact = contacts[number - 1]
 
    confirm = input(f"Delete {contact['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        contacts.pop(number - 1)  # remove it from the list
        if save_contacts(contacts):
            print("Contact deleted.")
    else:
        print("Cancelled. Nothing was deleted.")
 
 
def load_sample_data():
    """Add the 5 sample contacts for testing (skips ones that already exist)."""
    contacts = load_contacts()
    existing_phones = {c["phone"] for c in contacts}
    added = 0
    for sample in SAMPLE_CONTACTS:
        if sample["phone"] not in existing_phones:
            contacts.append(dict(sample))  # dict() makes a copy
            added += 1
    if save_contacts(contacts):
        print(f"Added {added} sample contact(s).")

#STEP 6: Main menu loop - repeats until the user chooses Exit
def main():
    """Run the contact book menu."""
    print("Welcome to the DTEN Contact Book!")
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Load 5 sample contacts (for testing)")
        print("6. Exit")
 
        choice = get_choice("Choose an option (1-6): ", 1, 6)
 
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            load_sample_data()
        elif choice == 6:
            print("Goodbye!")
            break
 
 
# Run main() only when this file is run directly
if __name__ == "__main__":
    main()

