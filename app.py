import sched, time
from TwintClass import TwintSearch

sched_object = sched.scheduler(time.time, time.sleep)

API_ENDPOINT = "http://node-app:3000/api/v1/incidentsRaw/postIncident"
username_target = ["js100radio", "Traffic_1197", "fm91trafficpro", "praramcommand"]
search_string = ["รถชน", "ไฟไหม้", "อุบัติเหตุ", "ชนกัน",
                 "เพลิงไหม้", "ชนกับ", "ไฟไหม้", "เสียหลัก", "พุ่งชน"
                ]

username_target = ["js100radio"]
search_string = ["รถชน",]

print("START TWINT")
scraping = TwintSearch(sched_object, 10, username_target, search_string)

sched_object.run()


