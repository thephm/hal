NEW_LINE = "\n"

FIELD_ORDER = 0
FIELD_TITLE = "title"
FIELD_ORGANIZATION = "organization"
FIELD_CURRENT = False
FIELD_START_DATE = "start_date"
FIELD_END_DATE = "end_date"
FIELD_LOCATION = "location"

class Position:
    def __init__(self):
        self.FIELD_ORDER = 0
        self.FIELD_TITLE = ""
        self.FIELD_ORGANIZATION = ""
        self.FIELD_CURRENT = False
        self.FIELD_START_DATE = ""
        self.FIELD_END_DATE = ""
        self.FIELD_LOCATION = ""

    def __str__(self):
        output = "title: " + self.FIELD_TITLE + NEW_LINE
        output += "organization: " + self.FIELD_ORGANIZATION + NEW_LINE
        output += "start_date: " + self.FIELD_START_DATE + NEW_LINE
        output += "end_date: " + self.FIELD_END_DATE + NEW_LINE
        output += "location: " + self.FIELD_LOCATION + NEW_LINE
        output += "current: " + str(self.FIELD_CURRENT) + NEW_LINE
        return output

