import requests

fid = "5423t4g25"
header = {
    "Referer":"https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0"
}

data = {
    "Termin":"2015-12-02",
    "email":"",
    "fid":fid,
    "matnr":"",
    "name":"Zimmermann",
    "ort":"52070 Aachen",
    "sex":"M",
    "statusorig":"S-RWTH",
    "strasse":"Thomashofstr. 31",
    "tnbed":"1",
    "vorname":"Anthony",
    "Phase":"final",
    "preis_anz":"0,00 EUR",
    "pw_newpw_"+fid:""
}
time.sleep(2)
r = requests.post("https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi", data = data, headers = header)


