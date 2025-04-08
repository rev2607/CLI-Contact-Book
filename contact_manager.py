import json
import os

FILE_PATH = 'storage.json' 

#intializes the manager and loads existing data
class ContactManager: 
    def __init__(self):
        self.contacts = []
        self.load_contacts()
    
    #loads contacts from JSON File
    def load_contacts(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'r') as f:
                self.contacts = json.load(f)
        else:
            self.contacts = []
    
    #save contacts to JSON File
    def save_contacts(self):
        with open(FILE_PATH, 'w') as f:
            json.dump(self.contacts, f, indent=4)

     #add a new contact
    def add_contact(self, name, phone, email, address):
        contact = {
            'name' : name,
            'phone' : phone,
            'email' : email,
            'address' : address
        }
        self.contacts.append(contact)
        self.save_contacts()
    
    #list all contacts
    def list_contacts(self):
        return self.contacts
    
    #search contacts
    def search_contact(self,query):
        return [c for c in self.contacts if query.lower() in c['name'].lower() or query in c['phone']]
    
    #delete contact
    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'].lower() != name.lower()]
        self.save_contacts()
    
    #edit contact
    def edit_contact(self, name, new_data):
        for c in self.contacts:
            if c['name'].lower() == name.lower():
                c.update(new_data)
                break
        self.save_contacts()