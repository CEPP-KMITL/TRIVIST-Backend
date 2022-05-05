from .ScrapeScript import ScrapeScript

class IticFoundationSearch():
    def __init__(self):
        self.set_up()

    def set_up(self):
        url_tasks = {
            "pre_script": [],
            "real_script": [],
            "post_script": [
                '/html/body/div[3]/div[1]/div[2]'
            ],
            "urls": [
                "https://live.iticfoundation.org/#"
            ]
        }

        driver = ScrapeScript
        browser = driver(
            url=url_tasks['urls'].pop(),
            pre_script_xpath_target=url_tasks['pre_script'],
            actual_script_xpath_target=url_tasks['real_script'],
            post_script_xpath_target=url_tasks['post_script']
        )

        browser.scrape_all_tab()
        browser.tear_down()

