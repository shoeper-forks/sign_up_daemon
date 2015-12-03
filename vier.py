#!/usr/bin/env python
import requests

fid = "d9d37b680645c21d223f0296d7a06acbce1d0f03"
header = {
    "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.4.0",
    "Host":"buchung.hsz.rwth-aachen.de",
    "Accept-Language":"en-GB,en;q=0.5",
    "DNT":"1",
}

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

r = requests.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)
print r.content
