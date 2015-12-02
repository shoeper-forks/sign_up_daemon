#!/usr/bin/env python

import requests
import sys
import time
import logging
import httplib

#          0        1           2           3           4          5       6     7     8      9     10
# argv = [..., course_name, course_id, course_date, firstname, lastname, matnr, sex, email, city, street]

def send_sign_up():
    fid = "0f9edf623c84df2103add3a2589671c7c75e5d96"
    with requests.Session() as s:
        header = {
        "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.4.0",
        "Host":"buchung.hsz.rwth-aachen.de",
        "Accept-Language":"en-GB,en;q=0.5",
        "DNT":"1",
        }
        
        # fill the textboxes
        data = {
            "Termin":"2016-01-20",
            "email":"Jannik-B-19@gmx.de",
            "fid":fid,
            "matnr":"334815",
            "name":"Becher",
            "ort":"52070 Aachen",
            "sex":"M",
            "statusorig":"S-RWTH",
            "strasse":"Thomashofstr. 31",
            "tnbed":"1",
            "vorname":"Jannik",
            "pw_pwd_"+fid:"",
            "pw_email":"",
            "telefon":"",
            "mitnr":"",
        }

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)
        
        print header
        # binding reserve

        data = {
            "Termin":"2016-01-20",
            "email":"Jannik-B-19@gmx.de",
            "fid":fid,
            "matnr":"334815",
            "name":"Becher",
            "ort":"52070 Aachen",
            "sex":"M",
            "statusorig":"S-RWTH",
            "strasse":"Thomashofstr. 31",
            "tnbed":"1",
            "vorname":"Jannik",
            "Phase":"final",
            "preis_anz":"0,00 EUR",
            "pw_newpw_"+fid:"",
        }


        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        print r.text


        print r.status_code
        print r.history
        if(r.status_code == 302):
            print sys.argv[4] + " " +  sys.argv[5] + " is signed up sucessfully!"
            return False
        else:
            print sys.argv[4] + " " +  sys.argv[5] + " is not signed up yet."
            return True

if(__name__=="__main__"):
    while(send_sign_up()):
        time.sleep(30)
