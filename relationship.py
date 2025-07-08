NEW_LINE = "\n"

class Relationship:
    def __init__(self):
        self.slug = 0
        self.label = ""
        self.strength = None

    def __str__(self):
        output = self.slug + ": " + str(self.slug)
        output += self.label + ": " + str(self.label)
        output += self.strength + ": " + str(self.strength)
        return output
