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
        self.events = []

    def __str__(self):
        return self.firstname + " " + self.lastname

    # event is a dict with course, id, date and time
    def add_event(self, course_name, course_id, date, time):
        event = {"course_name": course_name, "course_id": course_id, "date": date, "time": time}
        self.events.append(event)

    def make_cron(self):
        with open("/etc/crontab", 'a') as file:
            for event in self.events:
                hour = event["time"].split(':')[0]
                minute = event["time"].split(':')[1]
                day = event["date"].split('-')[2]
                month = event["date"].split('-')[1]
                file.write(minute + ' ' + hour + ' ' + day + ' ' + month +  ' * root ' + "./send_sign_up.py " + event["course_name"] + ' ' + event["course_id"] + ' ' + event["date"] + ' ' + self.firstname + ' ' + self.lastname + ' ' + self.matnr + ' ' + self.sex + ' ' + self.email + ' "' + self.city + '" "' + self.street + '"')


def create_person(file):
    with open(file) as data_file:
        data = json.load(data_file)

    person = Person(data["firstname"], data["lastname"], data["email"], data["city"], data["street"], data["matnr"], data["sex"])
    for event in data["events"]:
        person.add_event(event["course"], event["id"], event["date"], event["time"])
    
    return person


if(__name__=="__main__"):
    persons = []
    with open("config.ini") as ini_file:
        for file in ini_file.readlines():
            persons.append(create_person(file[:-1]))

    for person in persons:
        print person
        person.make_cron()
