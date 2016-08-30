import urllib, random, webbrowser, re

ROOT = "https://chicago.legistar.com/"

#EVENT CLASS

class Event(object):

    def __init__(self, name, date, time, location, detail_link, department_members = []):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.detail_link = detail_link
        self.department_members = department_members

    def __str__(self):
        return  "Event Name: "+self.name+"\nDate: "+self.date+"\nTime: "+self.time+"\nLocation: "+self.location+"\nLink to Details: "+self.detail_link


#BUSINESS LOGIC


def parseEventHtml():
    web_page = urllib.urlopen(ROOT+"Calendar.aspx")
    contents = web_page.read()
    web_page.close()

    meetings_code = re.findall(r'class="(?:rgRow|rgAltRow)".+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+</td>', contents)
    return meetings_code


def findEventName(event_html):
    dirty_time = re.search(r'DepartmentDetail.+</font>',event_html)
    dirty_time = dirty_time.group()
    dirty_time = re.search(r'"Blue"\ssize="2".+</',dirty_time)
    dirty_time = dirty_time.group()
    dirty_time = dirty_time[:-2]
    clean_time = dirty_time[16:]
    return clean_time

def findEventDate(event_html):
    dirty_date = re.search(r'DepartmentDetail.+\n.+rgSorted',event_html)
    dirty_date = dirty_date.group()
    dirty_date = re.search(r'"Tahoma"\ssize="2".+</',dirty_date)
    dirty_date = dirty_date.group()
    dirty_date = dirty_date[:-9]
    clean_date = dirty_date[18:]
    return clean_date

def findEventTime(event_html):
    dirty_time = re.search(r'Time"><font.+',event_html)
    clean_time = re.search(r'(?:\d|\d\d):\d\d\s\w\w',dirty_time.group())
    clean_time = clean_time.group()
    return clean_time

def findEventLocation(event_html):
    dirty_location = re.search(r'Time"><.+\n.+',event_html)
    dirty_location = dirty_location.group()
    dirty_location = dirty_location.split("<br")[0]
    dirty_location = dirty_location.split('"Tahoma" size="2">')[1]
    if dirty_location.endswith("="):
        clean_location = dirty_location[:-27]
    else:
        clean_location = dirty_location
    return clean_location

def findEventDetailLink(event_html):
    dirty_link = re.search(r'DepartmentDetail.+"><',event_html)
    dirty_link = dirty_link.group()
    dirty_link = dirty_link[:-3]
    clean_link = ROOT+dirty_link
    return clean_link

#Start of functionality to create objects for politicians

# def findEventDepartmentMembers(obj):
#     web_page = urllib.urlopen(obj.detail_link)
#     contents = web_page.read()
#     web_page.close()
#     return contents



def createEvents():
    event_objs = []
    events_html = parseEventHtml()

    for event_html in events_html:
        event = Event(name=findEventName(event_html), date=findEventDate(event_html), time=findEventTime(event_html), location=findEventLocation(event_html), detail_link=findEventDetailLink(event_html), department_members="a")
        print
        print event
        event_objs.append(event)


#DRIVER CODE
createEvents()