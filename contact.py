import sys
sys.path.insert(1, './') 
import postal_address

NEW_LINE = "\n"

QUALIFIER_HOME = "home"
QUALIFIER_WORK = "work"
QUALIFIER_OTHER = "other"

FIELD_WORK_EMAIL = "work_email"
FIELD_WORK_MOBILE = "work_mobile"
FIELD_WORK_PHONE = "work_phone"
FIELD_WORK_URL = "work_url"

FIELD_OTHER_EMAIL = "other_email"
FIELD_OTHER_MOBILE = "other_mobile"
FIELD_OTHER_PHONE = "other_phone"
FIELD_OTHER_URL = "other_url"

class Contact:
    def __init__(self, qualifier=QUALIFIER_HOME):
        self.qualifier = qualifier
        self.mobile = ""
        self.email = ""
        self.phone = ""
        self.url = ""
        self.address = postal_address.PostalAddress()

    def __str__(self):
        output = "qualifier: " + str(self.qualifier) + NEW_LINE
        output += "mobile: " + str(self.mobile) + NEW_LINE
        output += "email: " + str(self.mobile) + NEW_LINE
        output += "phone: " + str(self.phone)
        return output