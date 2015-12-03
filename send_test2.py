#!/usr/bin/env python

import requests
import sys
import time

#          0        1           2           3           4          5       6     7     8      9     10
# argv = [..., course_name, course_id, course_date, firstname, lastname, matnr, sex, email, city, street]

def send_sign_up():
    with requests.Session() as s:
        fid = "094ffc46a52f14fa84a1996d19a2e2655820c13a"

        # choose a date
        data = {
            "BS_TERMIN_"+sys.argv[3]:"buchen",
            "fid":str(fid),
        }

        header = {
            "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi",
        }
        

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        # fill the textboxes
        data = {
            "Termin":sys.argv[3],
            "email":sys.argv[8],
            "fid":str(fid),
            "matnr":sys.argv[6],
            "name":sys.argv[5],
            "ort":sys.argv[9],
            "sex":sys.argv[7],
            "statusorig":"S-RWTH",
            "strasse":sys.argv[10],
            "tnbed":"1",
            "vorname":sys.argv[4],
            "pw_pwd_"+fid:"",
            "pw_email":"",
            "telefon":"",
            "mitnr":"",
        }

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)
        
        # binding reserve
        data = {
            "Termin":sys.argv[3],
            "email":sys.argv[8],
            "fid":str(fid),
            "matnr":sys.argv[6],
            "name":sys.argv[5],
            "ort":sys.argv[9],
            "sex":sys.argv[7],
            "statusorig":"S-RWTH",
            "strasse":sys.argv[10],
            "tnbed":"1",
            "vorname":sys.argv[4],
            "Phase":"final",
            "preis_anz":"0,00 EUR",
            "pw_newpw_"+fid:"",
        }

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        print r.text


        print r.status_code
        print r.history
        if(r.status_code == requests.codes.found):
            print sys.argv[4] + " " +  sys.argv[5] + " is signed up sucessfully!"
            return False
        else:
            print sys.argv[4] + " " +  sys.argv[5] + " is not signed up yet."
            return True

if(__name__=="__main__"):
    while(send_sign_up()):
        time.sleep(30)
