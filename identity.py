NEW_LINE = "\n"

class Identity:
    def __init__(self):
        self.name = ""
        self.first_name = ""
        self.middle_name = ""
        self.last_name = ""
        self.full_name = ""
        self.nick_name = ""
        self.nee = ""
        self.gender = ""
        self.pronouns = ""

    def __str__(self):
        output = "name: " + self.name + NEW_LINE
        output += "first: " + self.first_name + NEW_LINE
        output += "middle: " + self.middle_name + NEW_LINE
        output += "last: " + self.last_name + NEW_LINE
        output += "full: " + self.full_name + NEW_LINE
        output += "nick: " + self.nick_name + NEW_LINE
        output += "nee: " + self.nee + NEW_LINE
        output += "gender: " + self.gender + NEW_LINE
        output += "pronouns: " + self.pronouns + NEW_LINE
        return output