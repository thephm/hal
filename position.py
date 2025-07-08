import sys
sys.path.insert(1, '../hal/')

import organization

NEW_LINE = "\n"

class Position:
    def __init__(self):
        self.order = 0
        self.title = ""
        self.organization = organization.Organization()
        self.current = False
        self.start_date = ""
        self.end_date = ""
        self.location = ""

    def __str__(self):
        output = "title: " + str(self.title) + NEW_LINE
        output += "organization: " + str(self.organization) + NEW_LINE
        output += "start_date: " + str(self.start_date) + NEW_LINE
        output += "end_date: " + str(self.end_date) + NEW_LINE
        output += "location: " + str(self.location) + NEW_LINE
        output += "current: " + str(self.current)
        return output

