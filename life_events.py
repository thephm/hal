NEW_LINE = "\n"

FIELD_BIRTHDAY = "birthday"
FIELD_DEATHDAY = "deathday"
FIELD_ANNIVERSARY = "anniversary"

class LifeEvents:
    def __init__(self):
        self.FIELD_BIRTHDAY = ""
        self.FIELD_DEATHDAY = ""
        self.FIELD_ANNIVERSARY = ""

    def __str__(self):
        output = "birthday: " + self.FIELD_BIRTHDAY + NEW_LINE
        output += "deathday: " + self.FIELD_DEATHDAY + NEW_LINE
        output += "anniversary: " + self.FIELD_ANNIVERSARY + NEW_LINE
        return output

