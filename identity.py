import re

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
        self.aliases = []
        self.url = ""
        
    def __str__(self):
        output = "name: " + str(self.name) + NEW_LINE
        output += "first: " + str(self.first_name) + NEW_LINE
        output += "middle: " + str(self.middle_name) + NEW_LINE
        output += "last: " + str(self.last_name) + NEW_LINE
        output += "full: " + str(self.full_name) + NEW_LINE
        output += "nick: " + str(self.nick_name) + NEW_LINE
        output += "nee: " + str(self.nee) + NEW_LINE
        output += "gender: " + str(self.gender) + NEW_LINE
        output += "pronouns: " + str(self.pronouns) + NEW_LINE
        output += "aliases: " + str(self.full_name) + NEW_LINE
        output += "url: " + str(self.url)
        return output
    
    def generate_slug(self, name=""):
        """
        Convert a name string to a slug suitable for use in URLs or filenames.
        
        Parameters:
        - name: The full name string, e.g., "Bob Smith"
        
        Returns:
        - A slugified version of the name, e.g., "bob_smith"
        """

        if not name or name == "":
            name = self.full_name


        # remove anything after and including ' - '
        name = name.split(' - ')[0].strip()

        # remove middle initials with a dot, e.g., " F. "
        name = re.sub(r'\s+[A-Z]\.\s+', ' ', name)
        
        # remove single-letter initials with a dot at the start, e.g., "R. Recio" -> "R Recio"
        name = re.sub(r'^([A-Z])\.\s+', r'\1 ', name)
        
        # remove any periods (e.g., "N." -> "N")
        name = name.replace('.', '')

        # replace apostrophes with nothing
        name = name.replace("'", "")

        # replace spaces and slashes with hyphens, but keep hyphens
        slug = re.sub(r'[ /]+', '-', name)

        # remove any character that is not a-z, 0-9, or hyphen
        slug = re.sub(r'[^a-zA-Z0-9\-]', '', slug)

        # convert to lowercase
        slug = slug.lower()

        # collapse multiple hyphens
        slug = re.sub(r'-+', '-', slug)

        # remove leading/trailing hyphens
        slug = slug.strip('-')

        return slug