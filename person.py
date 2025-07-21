# Classes that represent a Person

import sys
sys.path.insert(1, './') 
import identity
import life_events
import contact
import socials
import postal_address
import position

NEW_LINE = "\n"

# tags at the top of every Person Markdown file
TAG_PERSON = "person"
TAG_ALIST = "alist" # a-lister
TAG_BLIST = "blist"
TAG_CLIST = "clist"
TAG_DLIST = "dlist"
TAG_ELIST = "elist"
TAG_FLIST = "flist" # avoid

Tags = [TAG_PERSON]

Fields = ["slug", "tags", "subject_id", "slug", "last_contact", "connected_on", "birthday", "deathday", "anniversary", "interests", "favorites", "ignore", "people", "email_addresses", "conversation_id", "service_id", "title", "url", "organizations", "positions", "skills", "messages", "hometown", "folder_created"]

#Fields = ["slug", "tags", "subject_id", "slug", "last_contact", "connected_on", "birthday", "deathday", "anniversary", "interests", "favorites", "ignore", "people", "email_addresses", "conversation_id", "service_id", "title", "url", "organizations", "positions", "skills", "messages", "hometown", "city", "province", "country", "address", "work_address", "home_address", "other_address", "folder_created"]

# additional tags in a person file
OtherTags = [TAG_ALIST, TAG_BLIST, TAG_CLIST, TAG_DLIST, TAG_ELIST, TAG_FLIST]

class Person:
    def __init__(self):
        self.slug = ""  # unique across all people
        self.tags = []
        self.subject_id = None
        self.identity = identity.Identity()
        self.last_contact = None
        self.connected_on = None
        self.birthday = ""
        self.deathday = ""
        self.anniversary = ""
        self.interests = []
        self.favorites = []
        self.ignore = False # whether to ignore this person in processing
        self.people = []
        self.email_addresses = [] # collection of email addresses
        self.conversation_id = "" # needed for Signal only
        self.service_id = ""  # unique across all services
        self.title = ""
        self.url = ""  # URL to the person's profile, if available
        self.organizations = []
        self.positions = []
        self.skills = []
        self.contact = contact.Contact(contact.QUALIFIER_HOME)
        self.work_contact = contact.Contact(contact.QUALIFIER_WORK)
        self.other_contact = contact.Contact(contact.QUALIFIER_OTHER)
        self.socials = socials.Socials()
        self.messages = []  # collection of messages by day
        self.hometown = ""
        self.address = postal_address.PostalAddress(postal_address.QUALIFIER_HOME)
        self.work_address = postal_address.PostalAddress(postal_address.QUALIFIER_WORK)
        self.other_address = postal_address.PostalAddress(postal_address.QUALIFIER_OTHER)
        self.folder_created = False  # whether the folder for this person has been created
        
    def __str__(self):
        output = "slug: " + str(self.slug) + NEW_LINE
        output += str(self.identity     ) + NEW_LINE
        output += "tags: " + str(self.tags) + NEW_LINE
        output += "subject_id: " + str(self.subject_id) + NEW_LINE
        output += "last_contact: " + str(self.last_contact) + NEW_LINE
        output += "connected_on: " + str(self.connected_on) + NEW_LINE
        output += "ignore: " + str(self.ignore) + NEW_LINE
        output += "birthday: " + self.birthday + NEW_LINE
        output += "deathday: " + self.deathday + NEW_LINE
        output += "anniversary: " + self.anniversary + NEW_LINE
        output += "interests: " + str(self.interests) + NEW_LINE
        output += "favorites: " + str(self.favorites) + NEW_LINE
        output += "people: " + str(self.people) + NEW_LINE
        output += "title: " + self.title + NEW_LINE
        output += "organizations: " + str(self.organizations) + NEW_LINE
        output += "skills: " + str(self.skills) + NEW_LINE
        output += "email_addresses: " + str(self.email_addresses) + NEW_LINE
        output += str(self.contact) + NEW_LINE
        output += str(self.work_contact) + NEW_LINE
        output += str(self.other_contact) + NEW_LINE
        output += str(self.socials) + NEW_LINE
        output += "hometown: " + self.hometown + NEW_LINE
        output += "service_id: " + self.service_id + NEW_LINE
        output += "positions: " + NEW_LINE
        for position in self.positions:
            output += str(position) + NEW_LINE
        return output
    
    def get_people_slugs(self):
        people_slugs = []
        for person in self.people:
            people_slugs.append(person.slug)
        return people_slugs