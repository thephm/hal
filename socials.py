FIELD_LINKEDIN_ID = "linkedin_id" 
FIELD_FACEBOOK_ID = "facebook_id"
FIELD_X_ID = "x_id"
FIELD_INSTAGRAM_ID = "instagram_id"
FIELD_MEDIUM_ID = "medium_id"
FIELD_GITHUB_ID = "github_id"
FIELD_SKYPE_ID = "skype_id"
FIELD_THREADS_ID = "threads_id"

class Socials:
    def __init__(self):
        self.linkedin_id = ""
        self.facebook_id = ""
        self.x_id = ""
        self.github_id = ""
        self.medium_id = ""
        self.threads_id = ""

    def __str__(self):
        output += "linkedin_id: " + self.linkedin_id
        output += "facebook_id: " + self.facebook_id
        output += "instagram_id: " + self.instagram_id
        output += "x_id: " + self.x_id
        output += "github_id: " + self.github_id
        output += "medium_id: " + self.medium_id
        output += "threads_id: " + self.threads_id
        return output