def show_all():
    if not contacts:
        return "No contacts available."
    else:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()