# Simple Contact Book (File Handling)

# File to store contacts
CONTACTS_FILE = "contacts.txt"

def add_contact():
    """Add a new contact to the file."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    
    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone}\n")
    
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    """Display all saved contacts."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()
            
            if not contacts:
                print("No contacts found.")
                return
            
            print("\n📒 Saved Contacts:")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name: {name} | Phone: {phone}")
    except FileNotFoundError:
        print("No contacts found. Please add a contact first.")

def main():
    """Main menu for the contact book."""
    while True:
        print("\n===== Simple Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("📌 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
