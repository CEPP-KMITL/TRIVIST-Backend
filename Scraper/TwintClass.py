import twint
import sched
import datetime
from os import path
import os
import json

class TwintSearch:

    def __init__(self, sched_object: sched, delay: int, username_targets: list, search_strings: list):
        self.sched_object = sched_object
        self.__delay = delay
        self.username_targets = username_targets

        self.last_since = self.format_twint_time_now(self)
        self.sched_numbers = 0

        if len(search_strings) == 0:
            search_strings = [""]
        self.search_strings = search_strings

        if not self.__is_valid():
            raise TypeError(
                "This TwintSearch Object Is Not Properly Instantiated")
        else:
            self.add_schedule()
        print("Current Date When This Class Is Instantiated : " + self.last_since)

    def __is_valid(self):
        if self.__delay < 1 :# or self.API_ENDPOINT == "" or self.API_ENDPOINT is None:
            return False
        return True

    def add_schedule(self):
        for username in self.username_targets:
            for tag in self.search_strings:
                priority = self.username_targets.index(username) + 1
                self.sched_object.enter(self.__delay, priority, self.run_twint, (
                    self.sched_object, self.sched_numbers, username, tag, priority,
                    self.last_since,))

    def run_twint(self, sched_object: sched, round_identifier: int, username_target: str, search_string: str,
                  twint_priority: int, since_time: str):
        round_identifier = round_identifier + 1
        new_since_time = self.format_twint_time_now(self)
        print("Next Search Will Be Conduct From : " + new_since_time)
        sched_object.enter(self.__delay, twint_priority, self.run_twint,
                           (sched_object, round_identifier, username_target,
                            search_string, twint_priority, new_since_time,))
        # print("Twint Schedule Number : " + str(round_identifier) + " - " + "Search Since : " + str(
        #     since_time) + " - " + "Search For : " + str(search_string) + " - " + "From : " + str(
        #     username_target) + " - " + "With Priority : " + str(
        #     twint_priority))
        self.search_twint(username_target, search_string, str(
            username_target) + ".json", since_time)
        self.process_file(str(username_target), str(search_string))

    def search_twint(self, username_target: str, search_target: str, output_target: str, since_time: str):
        # Configure
        search_engine = twint.Config()
        search_engine.Username = username_target
        if search_target != "":
            search_engine.Search = search_target
        search_engine.Output = output_target
        search_engine.Store_json = True
        search_engine.Links = "include"
        search_engine.Since = since_time
        search_engine.Custom["tweet"] = ["id", "created_at", "username", "date", "time",
                                         "timezone", "name", "place", "tweet", "urls", "photos", "hashtags", "link", "geo"]
        # Run
        twint.run.Search(search_engine)
        print()

    def process_file(self, target_file_name: str, search_string: str):
        full_file_name = target_file_name + ".json"
        process_file_name = target_file_name + "_processing.json"
        if not path.exists(process_file_name):
            # print("Cannot Detect Processing File, Trying To Looking For Raw File : " + process_file_name)
            if path.exists(full_file_name):
                # print("Detect Raw File : " + full_file_name)
                os.rename(full_file_name, process_file_name)
                # print("Change File Name To Processing : " + process_file_name)
            # else:
                # print("Cannot Detect Raw File, Skip Processing : " + full_file_name)
        if path.exists(process_file_name):
            # print("Detect Processing File, Start Processing : " + process_file_name)
            extract_data = []
            with open(process_file_name, encoding="utf8") as process_file:
                for line in process_file:
                    extract_data.append(json.loads(line))
            for single_data in extract_data:
                if search_string != "":
                    search_keyword = {
                        "search_keyword": search_string
                    }
                else:
                    search_keyword = {
                        "search_keyword": None
                    }
                username = {"from": "TWITTER"}
                body = {"body": {"info": single_data,
                                 "packaging_timestamp": self.format_twint_time_now(self)}}

                dict_pack = username | search_keyword | body

                print(dict_pack)
                package_json = json.dumps(
                    dict_pack, ensure_ascii=False).encode('UTF-8')
                # print("Package JSON = " + package_json.decode('utf8'))
                # self.post_api(self.API_ENDPOINT, dict_pack)
            os.remove(process_file_name)
            print("Processing File Complete, Delete Processing File : " +
                  process_file_name)

    # def post_api(self, API_ENDPOINT: str, post_data):
    #     r = requests.post(url=API_ENDPOINT, json=post_data)
    #     print("Sent POST API")
    #     print(r.text)

    @staticmethod
    def format_twint_time_now(self):
        python_time_now = (str(datetime.datetime.now()).split())[0]
        return python_time_now 