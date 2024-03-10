NEW_LINE = "\n"

FIELD_TITLE = "title"
FIELD_ORGANIZATION = "organization"
FIELD_CURRENT = False

class Position:
    def __init__(self):
        self.FIELD_TITLE = ""
        self.FIELD_ORGANIZATION = ""
        self.FIELD_CURRENT = False

    def __str__(self):
        output = "title: " + self.FIELD_TITLE + NEW_LINE
        output += "organization: " + self.FIELD_ORGANIZATION + NEW_LINE
        output += "current: " + str(self.FIELD_CURRENT) + NEW_LINE
        return output

