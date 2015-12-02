#!/usr/bin/env python
import requests

bs_code = "47A4FC9FF7C27040683E7AA094578360"
course_name = "Handball"
course_id = "99588"

data = {
    "BS_Code":bs_code,
    "BS_Kursid_" + course_id:"buchen",
}

header = {
    "Referer":"http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_" + course_name + ".html",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.4.0",
    "Host":"buchung.hsz.rwth-aachen.de",
    "Accept-Language":"en-GB,en;q=0.5",
    "DNT":"1",
}

r = requests.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)
print r.content
