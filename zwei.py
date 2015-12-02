#!/usr/bin/env python
import requests

fid = "9125e44814cf7406e3c532fbaf3520ea51603cb6"
date = "2016-01-20"
course_id = "99588"

data = {
    "BS_TERMIN_"+date:"buchen",
    "fid":fid,
}

header = {
    "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.4.0",
    "Host":"buchung.hsz.rwth-aachen.de",
    "Accept-Language":"en-GB,en;q=0.5",
    "DNT":"1",
}

r = requests.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)
print r.content
