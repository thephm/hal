NEW_LINE = "\n"

QUALIFIER_HOME = "home"
QUALIFIER_WORK = "work"
QUALIFIER_OTHER = "other"

# not used very often
FIELD_WORK_ADDRESS = "work_address"
FIELD_WORK_CITY = "work_city"
FIELD_WORK_COUNTRY = "work_country"
FIELD_WORK_STATE = "work_state"
FIELD_WORK_ZIP = "work_zip"

class PostalAddress:
    def __init__(self, qualifier=QUALIFIER_HOME):
        self.qualifer = qualifier
        self.street = ""
        self.city = ""
        self.state = ""
        self.country = ""
        self.zip = ""

    def __str__(self):
        output = "qualifier: " + self.qualifier + NEW_LINE
        output += "address: " + self.address + NEW_LINE
        output += "city: " + self.city + NEW_LINE
        output += "state: " + self.state + NEW_LINE
        output += "country: " + self.country + NEW_LINE
        output += "zip: " + self.zip + NEW_LINE
        return output