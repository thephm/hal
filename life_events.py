NEW_LINE = "\n"

class LifeEvents:
    def __init__(self):
        self.birthday = ""
        self.deathday = ""
        self.anniversary = ""

    def __str__(self):
        output = "birthday: " + self.birthday + NEW_LINE
        output += "deathday: " + self.deathday + NEW_LINE
        output += "anniversary: " + self.anniversary + NEW_LINE
        return output

