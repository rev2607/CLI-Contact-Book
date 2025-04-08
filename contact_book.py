from contact_manager import ContactManager

def print_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def get_contact_input():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    return name, phone, email, address

def main():
    manager = ContactManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            print("\nEnter contact details:")
            name, phone, email, address = get_contact_input()
            manager.add_contact(name, phone, email, address)
            print("✅ Contact added.")

        elif choice == '2':
            contacts = manager.list_contacts()
            if not contacts:
                print("🚫 No contacts found.")
            else:
                for i, c in enumerate(contacts, 1):
                    print(f"\n📇 Contact {i}")
                    print(f"Name: {c['name']}")
                    print(f"Phone: {c['phone']}")
                    print(f"Email: {c['email']}")
                    print(f"Address: {c['address']}")

        elif choice == '3':
            query = input("🔍 Search by name or phone: ")
            results = manager.search_contact(query)
            if not results:
                print("🚫 No matching contacts.")
            else:
                print("\n📄 Search Results:")
                for c in results:
                    print(f"- {c['name']} | {c['phone']} | {c['email']} | {c['address']}")

        elif choice == '4':
            name = input("✏️ Enter name of contact to edit: ")
            print("Leave blank to keep current values.")
            new_phone = input("New Phone: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")

            new_data = {}
            if new_phone:
                new_data['phone'] = new_phone
            if new_email:
                new_data['email'] = new_email
            if new_address:
                new_data['address'] = new_address

            manager.edit_contact(name, new_data)
            print("🔁 Contact updated (if found).")

        elif choice == '5':
            name = input("🗑️ Enter name of contact to delete: ")
            manager.delete_contact(name)
            print("🧹 Contact deleted (if it existed).")

        elif choice == '6':
            print("👋 Exiting Contact Book. Bye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == '__main__':
    main()
