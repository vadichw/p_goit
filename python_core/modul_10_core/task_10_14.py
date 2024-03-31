from pprint import pprint

class Contacts:
    current_id = 1
    
    def __init__(self) -> None:
        self.contacts = []
    
    def list_contacts(self):
        return self.contacts
    
    def add_contact(self, name, phone, email, favorite):
        contact = {
            'id' : Contacts.current_id,
            'name': name,
            'phone': phone,
            'email': email,
            'favorite': favorite,
        }
        
        self.contacts.append(contact)
        Contacts.current_id += 1
        
contacts_instance = Contacts()
contacts_instance.add_contact("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
contacts_instance.add_contact("Vadim", "(068) 176-1760", "vadim2001@gmail.com", False)
pprint(contacts_instance.list_contacts())
