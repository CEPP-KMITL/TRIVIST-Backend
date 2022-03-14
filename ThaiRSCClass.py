from bs4 import BeautifulSoup
import requests
import sched

class ThaiRSCSearch:

    def __init__(self, sched_object: sched, delay: int, last_qid: int, main_url: str, page_url: str):
        self.sched_object = sched_object
        self.__delay = delay

        self.last_qid = last_qid
        self.main_url = main_url
        self.page_url = page_url
        # "http://www.thairsc.com/th/BigAccDetail.aspx"

        if not self.__is_valid():
            raise TypeError(
                "This ThaiRSCSearch Object Is Not Properly Instantiated")
        else:
            self.add_schedule()
        print("Current Date When This Class Is Instantiated : qid =", self.last_qid)

    def __is_valid(self):
        if self.__delay < 1 :# or self.API_ENDPOINT == "" or self.API_ENDPOINT is None:
            return False
        return True

    def add_schedule(self):
        priority = 1
        self.sched_object.enter(1, priority, self.run_scraping, (priority, self.last_qid))

    def run_scraping(self, priority: int, last_qid: int):
        # Scrape the main page to find the last event(accident)
        uri = self.main_url + self.page_url
        res = requests.get(uri)
        res.encoding = "utf-8"
        # print(res)

        # if res.status_code == 200:
        #     print("Succesful")
        # elif res.status_code == 404:
        #     print("Error 404 page not found")
        # else:
        #     print("Not both 200 and 404")

        soup = BeautifulSoup(res.content, 'html.parser')
        # print(soup.prettify())

        # courses = soup.find_all('section', id="section")

        # Find Anchor tag that contain url of event
        courses = soup.find('a', class_="text-detail")
        print("Last event arrival at " + self.main_url + courses["href"] +'\n')
        
        # Get last event's qid
        new_last_uri = courses["href"]
        new_last_qid = new_last_uri.split('=')[1].split('&')[0]

        # Add new schedule
        self.sched_object.enter(self.__delay, priority, self.run_scraping, (
                    self.sched_object, priority,
                    new_last_qid))

        # Get path without qid
        path_before_qid, path_after_qid = new_last_uri.split(new_last_qid)

        print()
        for qid in range(int(new_last_qid), last_qid, -1):
            # Add qid into path url
            uri = self.main_url + path_before_qid + str(qid) + path_after_qid
            print(uri)

            # Scrape event page
            res = requests.get(uri)
            res.encoding = "utf-8"
            
            soup = BeautifulSoup(res.content, 'html.parser')

            # Find data
            event = soup.find('section', id="section")

            title = event.find('span', id="ContentPlaceHolder1_lb_title").text
            datetime = event.find('span', id="ContentPlaceHolder1_lb_datetime").text
            detail = str(event.find('span', class_="detail")).replace('<br/>', '\n')
            print(title)
            print(datetime)

            # Already can't scrape event
            if title == "":
                print('STOP')
                break