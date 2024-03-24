import requests
import time
PHPSESSID = "s3fk4mclrkf63lkg9kj2if7f8b"
schoolCount = 50000
headers = {
    "Cookie":f"hideCookieConsent=true; PHPSESSID={PHPSESSID}; GCLB=CLSUrJDjkd24NRAD",
    "User-Agent":"Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type":"application/json",
}
with open("schools_info.txt", "a") as f:
    for i in range(2291,schoolCount):
        try:
            url = f"https://www.drfrost.org/api/school?sid={i}"
            r = requests.get(url=url,headers=headers)
            r.raise_for_status()
            data = r.json()
            string = f'{data["sid"]}:{data["name"]}:{data["town"]}:{data["latitude"]}:{data["longitude"]}:{data["domain"]}:{data["website"]}:{data["numstudents"]}' 
            f.write(f"{string}\n")
            print(f"{i} school scraped")
            time.sleep(0.00001)
        except:
            print(f"{i} school failed to scrape")