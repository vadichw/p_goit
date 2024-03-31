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