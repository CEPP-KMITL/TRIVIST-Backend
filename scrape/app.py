import sched, time
from twint.TwintClass import TwintSearch
from requests.ThaiRSCClass import ThaiRSCSearch
from selenium.IticFoundationClass import IticFoundationSearch

sched_object = sched.scheduler(time.time, time.sleep)

API_ENDPOINT = "http://node-app:3000/api/v1/incidentsRaw/postIncident"
username_target = ["js100radio", "Traffic_1197", "fm91trafficpro", "praramcommand"]
search_string = ["รถชน", "ไฟไหม้", "อุบัติเหตุ", "ชนกัน",
                 "เพลิงไหม้", "ชนกับ", "ไฟไหม้", "เสียหลัก", "พุ่งชน"
                ]

username_target = ["js100radio"]
search_string = ["อุบัติเหตุ",]

print("START AUTO Scrape")
# scraping = TwintSearch(sched_object, 10, username_target, search_string)
ThaiRSCSearch(sched_object, 3600, 0, 'http://www.thairsc.com/th/', 'BigAccidentAll.aspx?l=th')

# IticFoundationSearch()

sched_object.run()

# Twitter ✅
# https://live.iticfoundation.org/# ❌
# www.thairsc.com/th/ ✅
# longdo api ❌



