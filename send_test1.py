#!/usr/bin/env python

import requests
import sys
import time

#          0        1           2           3           4          5       6     7     8      9     10
# argv = [..., course_name, course_id, course_date, firstname, lastname, matnr, sex, email, city, street]

def send_sign_up():
    for arg in sys.argv:
        print arg

    with requests.Session() as s:
        r = s.get("http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_"+sys.argv[1]+".html")

        # Get BS_Code from the site
        bs_code_pos = r.content.find("BS_Code")
        bs_code = r.content[bs_code_pos+16:bs_code_pos+48] 
        print bs_code
        
        # click on the button "Buchen"
        data = {
            "BS_Code":str(bs_code),
            "BS_Kursid_"+sys.argv[2]:"buchen",
        }

        header = {
            "Referer":"http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_"+sys.argv[1]+".html",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.4.0",
            "Host":"buchung.hsz.rwth-aachen.de",
            "Accept-Language":"en-GB,en;q=0.5",
            "DNT":"1",
        }

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        print r.content

        # get the fid checksum
        fid_pos = r.content.find("fid")
        fid = r.content[fid_pos+12:fid_pos+52]
        print fid

        # choose a date
        data = {
            "BS_TERMIN_"+sys.argv[3]:"buchen",
            "fid":str(fid),
        }

        header = {
            "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.4.0",
            "Host":"buchung.hsz.rwth-aachen.de",
            "Accept-Language":"en-GB,en;q=0.5",
            "DNT":"1",
        }
        

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        print r.content

        return False

if(__name__=="__main__"):
    while(send_sign_up()):
        time.sleep(30)
