NEW_LINE = "\n"

FIELD_RELATIONSHIP_SLUG = "slug"
FIELD_RELATIONSHIP_LABEL = "label"
FIELD_RELATIONSHIP_STRENGTH = ""

class Relationship:
    def __init__(self):
        self.FIELD_RELATIONSHIP_SLUG = 0
        self.FIELD_RELATIONSHIP_LABEL = ""
        self.FIELD_RELATIONSHIP_STRENGTH = None

    def __str__(self):
        output = self.slug + ": " + str(self.FIELD_RELATIONSHIP_SLUG)
        output += self.label + ": " + str(self.FIELD_RELATIONSHIP_LABEL)
        output += self.strength + ": " + str(self.FIELD_RELATIONSHIP_STRENGTH)
        return output
