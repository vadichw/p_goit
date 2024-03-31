def get_emails(list_contacts):
    emails = list(map(lambda contact: contact['email'], list_contacts ))
    return emails





print(get_emails([{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}]))