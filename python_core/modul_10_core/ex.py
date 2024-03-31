from collections import UserDict

contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}]


class Customer(UserDict):
    def get_phone(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def get_email(self):
        return f"{self.get('name')}: {self.get('email')}"


customers = [Customer(contact) for contact in contacts]
print(customers)
for cus in customers:
    print(cus.get_phone())
    print(cus.get_email())
