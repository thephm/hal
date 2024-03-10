NEW_LINE = "\n"

FIELD_NAME = "name"
FIELD_FIRST_NAME = "first_name"
FIELD_MIDDLE_NAME = "middle_name"
FIELD_LAST_NAME = "last_name"
FIELD_NICK_NAME = "nick_name"
FIELD_ALIASES = "aliases"
FIELD_NEE = "nee"
FIELD_PRONOUNS = "pronouns"
FIELD_GENDER = "gender"

class Identity:
    def __init__(self):
        self.FIELD_NAME = ""
        self.FIELD_FIRST_NAME = ""
        self.FIELD_MIDDLE_NAME = ""
        self.FIELD_LAST_NAME = ""
        self.FIELD_NICK_NAME = ""
        self.FIELD_NEE = ""
        self.FIELD_GENDER = ""
        self.FIELD_PRONOUNS = ""

    def __str__(self):
        output = "name: " + self.FIELD_NAME + NEW_LINE
        output += "first: " + self.FIELD_FIRST_NAME + NEW_LINE
        output += "middle: " + self.FIELD_MIDDLE_NAME + NEW_LINE
        output += "last: " + self.FIELD_LAST_NAME + NEW_LINE
        output += "nick: " + self.FIELD_NICK_NAME + NEW_LINE
        output += "nee: " + self.FIELD_NEE + NEW_LINE
        output += "gender: " + self.FIELD_GENDER + NEW_LINE
        output += "pronouns: " + self.FIELD_PRONOUNS + NEW_LINE
        return output