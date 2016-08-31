import csv

class LegBody(object):

    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __str__(self):
        return self.name


class Event(object):

    def __init__(self, name, date, time, location):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.detail_link = True

    def __str__(self):
        return  "Event Name: "+self.name+"\nDate: "+self.date+"\nTime: "+self.time+"\nLocation: "+self.location+"\nLink to Details: "


class Member(object):

    def __init__(self, name, ward, phone, fax, email, website_url, office_address, office_city, office_state, office_zip, city_hall_phone, city_hall_address):
        self.name = name
        self.ward = ward
        self.phone = phone
        self.fax = fax
        self.email = email
        self.website_url = website_url
        self.office_address = office_address
        self.office_city = office_city
        self.office_state = office_state
        self.office_zip = office_zip
        self.city_hall_phone = city_hall_phone
        self.city_hall_address = city_hall_address

    def __str__(self):
        return  "Member Name: "+self.name+"\nWard: "+self.ward+"\nPhone: "+self.phone+"\nFax: "+self.fax+"\nEmail: "+self.email+"\nWebsite: "+self.website_url+"\nOffice Address: "+self.office_address+"\nOffice City: "+self.office_city+"\nOffice State: "+self.office_state+"\nOffice Zip: "+self.office_zip+"\nCity Hall Phone: "+self.city_hall_phone+"\nCity Hall Address: "+self.city_hall_address


def createLegBodies():
    legbodies_objs = []
    legbodies = csv.DictReader(open('csv/leg_bodies.csv', 'r'))
    return [LegBody(name=legbody[" Legislative Body "], members=[]) for legbody in legbodies]

def createEvents():
    event_objs = []
    events = csv.DictReader(open('csv/meetings.csv', 'r'))
    return [Event(name=event["\xef\xbb\xbfName"], date=event[" Meeting Date "], time=event["Meeting Time"], location=event["Meeting Location"]) for event in events]

def createMembers():
    members = csv.DictReader(open('csv/members.csv', 'r'))
    return [Member(name=member[" Person Name "], ward=member["Ward/Office"], phone=member["Ward Office Phone"], fax=member["Fax"], email=member["E-mail"], website_url=member["Web Site"], office_address=member["Ward Office Address"], office_city=member["City"], office_state=member["State"], office_zip=member["Zip"], city_hall_phone=member["City Hall Phone"], city_hall_address=member["City Hall Address"]) for member in members]

legbodies = createLegBodies()
for legbody in legbodies:
    print legbody

events = createEvents()
for event in events:
    print
    print event

members = createMembers()
for member in members:
    print
    print member
