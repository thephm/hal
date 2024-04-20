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

# fields in a Person file's fronmatter files
FIELD_TAGS = "tags"
FIELD_SLUG = "slug"
FIELD_SUBJECT_ID = "subject_id"

FIELD_LAST_CONTACT = "last_contact"
FIELD_LAST_UPDATED = "last_updated"

FIELD_INTERESTS = "interests"
FIELD_FAVORITES = "favorites"

FIELD_ORGANIZATIONS = "organizations"
FIELD_SKILLS = "skills"

FIELD_CONTACT = "contact"
FIELD_WORK_CONTACT = "work_contact"
FIELD_OTHER_CONTACT = "other_contact"

FIELD_HOMETOWN = "hometown"
FIELD_ADDRESSES = "addresses"

Fields = [FIELD_TAGS, FIELD_SLUG, FIELD_SUBJECT_ID,
          identity.FIELD_NAME, identity.FIELD_FIRST_NAME, identity.FIELD_LAST_NAME, identity.FIELD_NEE, identity.FIELD_NICK_NAME, identity.FIELD_ALIASES, identity.FIELD_GENDER, identity.FIELD_PRONOUNS, 
          life_events.FIELD_BIRTHDAY, life_events.FIELD_DEATHDAY, life_events.FIELD_ANNIVERSARY, 
          position.FIELD_TITLE, FIELD_ORGANIZATIONS, 
          FIELD_LAST_CONTACT, FIELD_LAST_UPDATED, 
          FIELD_SKILLS, FIELD_INTERESTS, 
          contact.FIELD_MOBILE, contact.FIELD_EMAIL, contact.FIELD_URL,
          contact.FIELD_WORK_MOBILE, contact.FIELD_WORK_EMAIL, contact.FIELD_WORK_URL,
          contact.FIELD_OTHER_MOBILE, contact.FIELD_OTHER_EMAIL, contact.FIELD_OTHER_URL,
          socials.FIELD_LINKEDIN_ID, socials.FIELD_FACEBOOK_ID, socials.FIELD_X_ID,socials.FIELD_INSTAGRAM_ID, 
          socials.FIELD_MEDIUM_ID, socials.FIELD_GITHUB_ID, socials.FIELD_SKYPE_ID,
          FIELD_HOMETOWN,
          postal_address.FIELD_ADDRESS, postal_address.FIELD_CITY, postal_address.FIELD_STATE, postal_address.FIELD_COUNTRY, postal_address.FIELD_ZIP, 
          postal_address.FIELD_WORK_ADDRESS, postal_address.FIELD_WORK_CITY, postal_address.FIELD_WORK_COUNTRY, postal_address.FIELD_WORK_STATE, postal_address.FIELD_WORK_ZIP
        ]

# tags at the top of every Person Markdown file

TAG_PERSON = "person"
TAG_ALIST = "alist"
TAG_BLIST = "blist"
TAG_CLIST = "clist"
TAG_DLIST = "dlist"
TAG_ELIST = "elist"
TAG_FLIST = "flist"

Tags = [TAG_PERSON]

# additional tags in a person file
OtherTags = [TAG_ALIST, TAG_BLIST, TAG_CLIST, TAG_DLIST, TAG_ELIST, TAG_FLIST]

class Person:
    def __init__(self):
        self.slug = ""  # unique across all people
        self.FIELD_TAGS = []
        self.FIELD_SUBJECT_ID = None
        self.FIELD_IDENTITY = identity.Name()
        self.FIELD_LAST_CONTACT = None
        self.FIELD_BIRTHDAY = ""
        self.FIELD_DEATHDAY = ""
        self.FIELD_ANNIVERSARY = ""
        self.FIELD_INTERESTS = []
        self.FIELD_FAVORITES = []
        self.people = []
        self.FIELD_TITLE = ""
        self.FIELD_ORGANIZATIONS = []
        self.FIELD_SKILLS = []
        self.FIELD_CONTACT = contact.Contact(contact.QUALIFIER_HOME)
        self.FIELD_WORK_CONTACT = contact.Contact(contact.QUALIFIER_WORK)
        self.FIELD_OTHER_CONTACT = contact.Contact(contact.QUALIFIER_OTHER)
        self.FIELD_SOCIALS = socials.Socials()
        self.email_addresses = [] # collection of email addresses
        self.messages = []  # collection of messages by day
        self.hometown = ""
        self.address = postal_address.PostalAddress(postal_address.QUALIFIER_HOME)
        self.work_address = postal_address.PostalAddress(postal_address.QUALIFIER_HOME)
        self.other_address = postal_address.PostalAddress(postal_address.QUALIFIER_OTHER)

    def __str__(self):
        output = "slug: " + self.slug + NEW_LINE
        output += "tags: " + str(self.tags) + NEW_LINE
        output += "subject_id: " + self.subject_id + NEW_LINE
        output += "last_contact: " + self.last_contact + NEW_LINE
        output += "mobile: " + self.mobile + NEW_LINE
        output += str(self.name)
        output += "gender: " + self.FIELD_GENDER
        output += "pronouns: " + str(self.FIELD_PRONOUNS)
        output += "aliases: " + str(identity.FIELD_ALIASES)
        output += "birthday: " + self.FIELD_BIRTHDAY
        output += "deathday: " + self.FIELD_DEATHDAY
        output += "anniversary: " + self.FIELD_ANNIVERSARY
        output += "interests: " + str(self.FIELD_INTERESTS)
        output += "favorites: " + str(self.FIELD_FAVORITES)
        output += "people: " + str(self.people)
        output += "title: " + self.FIELD_TITLE
        output += "organizations: " + str(self.FIELD_ORGANIZATIONS)
        output += "skills: " + str(self.FIELD_SKILLS)
        output += str(self.FIELD_CONTACT)
        output += str(self.FIELD_WORK_CONTACT)
        output += str(self.FIELD_OTHER_CONTACT)
        output += str(self.FIELD_SOCIALS)
        output += "email_addresses: " + str(self.email_addresses)
        output += "hometown: " + self.FIELD_HOMETOWN
        output += str(self.FIELD_CONTACT)
        output += str(self.FIELD_WORK_CONTACT)
        output += str(self.FIELD_OTHER_CONTACT)
        return output
    
    def people():
        people_slugs = []
        for person in self.people:
            people_slugs.append(person.slug)
        return people_slugs