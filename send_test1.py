#!/usr/bin/env python

import requests
import sys
import time

#          0        1           2           3           4          5       6     7     8      9     10
# argv = [..., course_name, course_id, course_date, firstname, lastname, matnr, sex, email, city, street]

def send_sign_up():
    with requests.Session() as s:
        r = s.get("http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_"+sys.argv[1]+".html")

        # Get BS_Code from the site
        bs_code_pos = r.content.find("BS_Code")
        bs_code = r.content[bs_code_pos+16:bs_code_pos+48] 
        
        # click on the button "Buchen"
        data = {
            "BS_Code":str(bs_code),
            "BS_Kursid_"+sys.argv[2]:"buchen"
        }

        header = {
            "Referer":"http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_"+sys.argv[1]+".html"
        }

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        # get the fid checksum
        fid_pos = r.content.find("fid")
        fid = r.content[fid_pos+12:fid_pos+52]
        print fid

        # choose a date
        data = {
            "BS_Termin_"+sys.argv[3]:"buchen",
            "fid":str(fid)
        }

        header = {
            "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi"
        }
        

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

if(__name__=="__main__"):
    send_sign_up()
