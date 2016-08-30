import csv

class Event(object):

    def __init__(self, name, date, time, location):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.detail_link = True

    def __str__(self):
        return  "Event Name: "+self.name+"\nDate: "+self.date+"\nTime: "+self.time+"\nLocation: "+self.location+"\nLink to Details: "

def createEvents():
	event_objs = []
	events = csv.DictReader(open('2016_chi_leg.csv', 'r'))
	for event in events:
		new_event = Event(name=event["Name"], date=event["Meeting Date"], time=event["Meeting Time"], location=event["Meeting Location"])
		print
		print new_event
		event_objs.append(event)
        
createEvents()
