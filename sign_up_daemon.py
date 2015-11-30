#!/usr/bin/env python

import requests
import json

class Person:
    def __init__(self, firstname, lastname, email, city, street, matnr, sex):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.city = city
        self.street = street
        self.matnr = matnr
        self.sex = sex
        self.events = [{}]

    # event is a dict with course, id, date and time
    def add_event(self, course_name, course_id, date, time):
        event = {"course_name": course_name, "course_id": course_id, "date": date, "time": time}
        self.events.push_back(event)

    def send_sign_up(self, event):
        with requests.Session() as s:
            r = s.get("http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_"+event["course_name"]+".html")

            # Get BS_Code from the site
            bs_code_pos = r.content.find("BS_Code")
            bs_code = r.content[bs_code_pos+16:bs_code_pos+48] 
            print bs_code
            
            # click on the button "Buchen"
            data = {
                "BS_Code":str(bs_code),
                "BS_Kursid_"+event["course_id"]:"buchen"
            }

            header = {
                "Referer":"http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_"+event["course_name"]+".html"
            }

            r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

            # get the fid checksum
            fid_pos = r.content.find("fid")
            fid = r.content[fid_pos+12:fid_pos+52]
            print fid

            # choose a date
            data = {
                "BS_TERMIN_"+event["date"]:"buchen",
                "fid":str(fid)
            }

            header = {
                "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi"
            }

            r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

            # fill the textboxes
            data = {
                "Termin":event["data"],
                "email":self.email,
                "fid":str(fid),
                "matnr":self.matnr,
                "name":self.lastname,
                "ort":self.city,
                "sex":self.sex,
                "statusorig":"S-RWTH",
                "strasse":self.street,
                "tnbed":"1",
                "vorname":self.firstname
            }

            r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

            print r.content

    def do_it(self):
        self.send_sign_up(self, self.events[0])

def create_person(file):
    with open(file) as data_file:
        data = json.load(data_file)

    person = Person(data["firstname"], data["lastname"], data["email"], data["city"], data["street"], data["matnr"], data["sex"])
    for event in data["events"]:
        person.add_event(event["course"], event["id"], event["date"], event["time"]


if(__name__=="__main__"):
    persons = []
    with open("config.ini") as ini_file:
        for file in ini_file.readlines():
            persons.push_back(create_person(file)

    persons[0].do_it()
