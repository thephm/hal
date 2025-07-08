import re

NEW_LINE = "\n"

class Organization:
    def __init__(self):
        self.order = 0
        self.name = ""
        self.aliases = []
        self.slug = ""

    def __str__(self):
        output = "name: " + str(self.name) + NEW_LINE
        output += "order: " + str(self.order) + NEW_LINE
        output += "aliases: " + str(self.slug) + NEW_LINE
        output += "slug: " + str(self.slug)
        return output

    def generate_slug(self, name=""):
        """
        Convert a name string to a slug suitable for use in URLs or filenames.
        
        Parameters:
        - name: The organization name string, e.g., "Nortel Networks"
        
        Returns:
        - A slugified version of the name, e.g., "nortel"
        """
        slug = ""
        org_name = name if name else self.name
        
        if org_name:
            slug = org_name.lower()
            slug = slug.replace('&', 'and')  # replace & with 'and'
            slug = re.sub(r"[']", '', slug)  # remove apostrophes
            slug = re.sub(r"[.]", '', slug)  # remove periods
            slug = re.sub(r"[^a-z0-9\- ]", '', slug)  # remove other punctuation except hyphens and spaces
            slug = slug.split(' - ')[0].strip()  # remove anything after and including ' - '
            slug = slug.replace(" ", "-")
            slug = re.sub(r'-+', '-', slug)  # collapse multiple hyphens

        return slug
