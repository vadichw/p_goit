class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contact(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contact(self, contact_id: int) -> None:
        for contact in self.contacts:
            if contact['id'] == contact_id:
                self.contacts.remove(contact)
                break

contacts_instance = Contacts()
contacts_instance.add_contact("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
contacts_instance.add_contact("Vadim", "(068) 176-1760", "vadim2001@gmail.com", False)
print(contacts_instance.list_contacts())
#print(contacts_instance.get_contact_by_id(1))

