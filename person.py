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

# additional tags in a person file
OtherTags = [TAG_ALIST, TAG_BLIST, TAG_CLIST, TAG_DLIST, TAG_ELIST, TAG_FLIST]

class Person:
    def __init__(self):
        self.slug = ""  # unique across all people
        self.tags = []
        self.subject_id = None
        self.identity = identity.Identity()
        self.last_contact = None
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
        self.work_address = postal_address.PostalAddress(postal_address.QUALIFIER_HOME)
        self.other_address = postal_address.PostalAddress(postal_address.QUALIFIER_OTHER)
        self.folder_created = False  # whether the folder for this person has been created
        self.linkedin_id = ""
        
    def __str__(self):
        output = "slug: " + self.slug + NEW_LINE
        output += "tags: " + str(self.tags) + NEW_LINE
        output += "subject_id: " + self.subject_id + NEW_LINE
        output += "last_contact: " + self.last_contact + NEW_LINE
        output += "mobile: " + self.mobile + NEW_LINE
        output += str(self.name)
        output += "gender: " + self.gender
        output += "ignore: " + str(self.ignore) + NEW_LINE
        output += "pronouns: " + str(self.pronouns) + NEW_LINE
        output += "aliases: " + str(identity.aliases)
        output += "birthday: " + self.birthday
        output += "deathday: " + self.deathday
        output += "anniversary: " + self.anniversary
        output += "interests: " + str(self.interests)
        output += "favorites: " + str(self.favorites)
        output += "people: " + str(self.people)
        output += "title: " + self.title
        output += "organizations: " + str(self.organizations)
        output += "positions: " + str(self.positions)
        output += "skills: " + str(self.skills)
        output += str(self.contact)
        output += str(self.work_contact)
        output += str(self.other_contact)
        output += str(self.socials)
        output += "email_addresses: " + str(self.email_addresses)
        output += "hometown: " + self.hometown
        output += str(self.contact)
        output += str(self.work_contact)
        output += str(self.other_contact)
        output += "service_id: " + self.service_id + NEW_LINE
        return output
    
    def get_people_slugs(self):
        people_slugs = []
        for person in self.people:
            people_slugs.append(person.slug)
        return people_slugs