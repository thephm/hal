NEW_LINE = "\n"

class Interaction:
    def __init__(self):
        self.slug = 0
        self.date = None
        self.service = ""

    def __str__(self):
        output = self.slug + ": " + str(self.date)
        if self.service:
            output += " on " + self.service
        return output

class InteractionHistory:
    def __init__(self):
        self.slug = ""
        self.interactions = []
        self.date = None

    def __str__(self):
        output = ""
        for interaction in self.interactions:
            output += str(interaction) + NEW_LINE
        return output
    
# count the number of interactions
class InteractionsByMonth:
    def __init__(self):
        self.month = 0
        self.year = 0
        self.count = 0
