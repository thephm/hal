NEW_LINE = "\n"

class Socials:
    def __init__(self):
        self.linkedin_id = ""
        self.facebook_id = ""
        self.instagram_id = ""
        self.bluesky_id = ""
        self.x_id = ""
        self.github_id = ""
        self.medium_id = ""
        self.threads_id = ""

    def __str__(self):
        output = "linkedin_id: " + self.linkedin_id + NEW_LINE
        output += "facebook_id: " + self.facebook_id + NEW_LINE
        output += "instagram_id: " + self.instagram_id + NEW_LINE
        output += "bluesky_id: " + self.instagram_id + NEW_LINE
        output += "x_id: " + self.x_id + NEW_LINE
        output += "github_id: " + self.github_id + NEW_LINE
        output += "medium_id: " + self.medium_id + NEW_LINE
        output += "threads_id: " + self.threads_id
        return output