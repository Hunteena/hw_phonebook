import csv
import re

PHONE_POSITION = 5


class ContactInfo(list):
    def format_name(self):
        names = self[:3]
        if not all(names):
            full_name = []
            for name_part in names:
                full_name.extend(name_part.split())
            while len(full_name) < 3:
                full_name.append('')
            self[:3] = full_name

    def format_phone(self):
        main_phone, extension, ext_phone = self[PHONE_POSITION].partition('доб')
        main_pattern = r"(\+7|8)[-(\s]*(\d{3})[-)\s]*(\d{3})-*(\d{2})-*(\d{2})\D*"
        main_phone = re.sub(main_pattern, r"+7(\2)\3-\4-\5", main_phone)
        if extension:
            ext_pattern = r"\D*(\d+)\D*"
            ext_phone = re.sub(ext_pattern, r"\1", ext_phone)
            self[PHONE_POSITION] = f"{main_phone} доб.{ext_phone}"
        else:
            self[PHONE_POSITION] = f"{main_phone}"

    def fill_missing(self, info):
        for i, data in enumerate(self):
            if not data and info[i]:
                self[i] = info[i]


class Phonebook(dict):
    def update_contact(self, info):
        lastname, firstname = info[:2]
        phonebook_id = f"{lastname} {firstname}"
        if phonebook_id in self.keys():
            self[phonebook_id].fill_missing(info)
        else:
            self[phonebook_id] = info

    def write_to(self, filename):
        with open(filename, "w") as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(self.values())


def get_raw_from(filename):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=",")
        return list(rows)
