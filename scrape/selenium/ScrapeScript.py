import time
from .script_template import ScriptTemplate

class ScrapeScript(ScriptTemplate):
    def __init__(self, url, pre_script_xpath_target, actual_script_xpath_target, post_script_xpath_target):
        super().__init__(url=url, pre_script_xpath_target=pre_script_xpath_target,
                         actual_script_xpath_target=actual_script_xpath_target, post_script_xpath_target=post_script_xpath_target)

    def post_script(self, xpath_target, name):
        time.sleep(2)

        raw_data = self.get_element(xpath_target[0])
        print(raw_data)