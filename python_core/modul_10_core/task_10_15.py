import pprint

class Contacts:
    current_id = 1
    
    def __init__(self) -> None:
        self.contacts = []
    
    def list_contacts(self) -> list:
        return self.contacts
    
    def get_contact_by_id(self, contact_id: int) -> dict or None:
        for contact in self.contacts:
            if contact['id'] == contact_id:
                return contact
        return None
    
    def add_contact(self, name: str, phone: str, email: str, favorite: bool) -> None:
        contact = {
            'id': Contacts.current_id,
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
#print(contacts_instance.list_contacts())
print(contacts_instance.get_contact_by_id(1))