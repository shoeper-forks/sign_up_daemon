#!/usr/bin/env python

import requests

def send_sign_up(personal_data):
    with requests.Session() as s:
        r = s.get("http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/"+personal_data["kurs_name"])

        # Get BS_Code from the site
        bs_code_pos = r.content.find("BS_Code")
        bs_code = r.content[bs_code_pos+16:bs_code_pos+48] 
        print bs_code
        
        # click on the button "Buchen"
        data = {
            "BS_Code":str(bs_code),
            "BS_Kursid_"+personal_data["kurs_id"]:"buchen"
        }

        header = {
            "Referer":"http://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/"+personal_data["kurs_name"]
        }

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        # get the fid checksum
        fid_pos = r.content.find("fid")
        fid = r.content[fid_pos+12:fid_pos+52]
        print fid

        # choose a date
        data = {
            "BS_TERMIN_"+personal_data["termin"]:"buchen",
            "fid":str(fid)
        }

        header = {
            "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi"
        }

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        # fill the textboxes
        data = {
            "Termin":str(personal_data["termin"]),
            "email":str(personal_data["email"]),
            "fid":str(fid),
            "matnr":str(personal_data["matnr"]),
            "name":str(personal_data["name"]),
            "ort":str(personal_data["ort"]),
            "sex":str(personal_data["sex"]),
            "statusorig":"S-RWTH",
            "strasse":str(personal_data["strasse"]),
            "tnbed":"1",
            "vorname":str(personal_data["vorname"])
        }

        r = s.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)

        print r.content

def set_data(kurs_id, kurs_name, termin, email, matnr, name, vorname, ort, sex, strasse):
    personal_data = {"kurs_id": kurs_id, "kurs_name": kurs_name, "termin": termin, "email": email, "matnr": matnr, "name": name, "ort": ort, "sex": sex, "strasse": strasse, "vorname": vorname}
    return personal_data

if(__name__=="__main__"):
    personal_data = set_data("99582", "_Handball.html", "2015-12-02", "", "334815", "Becher", "Jannik", "52070 Aachen", "M", "Thomashofstr. 31")
    send_sign_up(personal_data)
