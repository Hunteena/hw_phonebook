from contacts import ContactInfo, Phonebook, get_raw_from


def main():
    phonebook = Phonebook()
    contact_list = get_raw_from("phonebook_raw.csv")
    for row in contact_list:
        contact = ContactInfo(row[:7])
        contact.format_name()
        contact.format_phone()
        phonebook.update_contact(contact)
    phonebook.write_to("phonebook.csv")


if __name__ == '__main__':
    main()
