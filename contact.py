import sys
sys.path.insert(1, './') 
import postal_address

NEW_LINE = "\n"

QUALIFIER_HOME = "home"
QUALIFIER_WORK = "work"
QUALIFIER_OTHER = "other"

FIELD_QUALIFIER = "qualifier"
FIELD_EMAIL = "email"
FIELD_MOBILE = "mobile"
FIELD_PHONE = "phone"
FIELD_URL = "url"

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
        self.FIELD_QUALIFIER = qualifier
        self.FIELD_MOBILE = ""
        self.FIELD_PHONE = ""
        self.FIELD_URL = ""
        self.address = postal_address.PostalAddress()

    def __str__(self):
        output = "qualifier: " + self.FIELD_QUALIFIER + NEW_LINE
        output += "mobile: " + self.FIELD_MOBILE + NEW_LINE
        output += "phone: " + self.FIELD_PHONE + NEW_LINE
        output += "url: " + self.FIELD_URL + NEW_LINE
        return output