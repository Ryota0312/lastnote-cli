from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
import time
import yaml
import datetime

class LastNote:
    def __init__(self, settings):
        options = ChromeOptions()
        options.add_argument('--headless')
        self.settings = settings
        self.driver = Chrome(self.settings["CHROME_DRIVER_PATH"], options=options)

    def quit(self):
        self.driver.quit()

    def login(self):
        self.driver.get('http://lastnote.swlab.cs.okayama-u.ac.jp/gate/login')

        login_name = self.driver.find_element_by_id("login_name")
        login_name.send_keys(self.settings["LOGIN_NAME"])
        password = self.driver.find_element_by_id("password")
        password.send_keys(self.settings["PASSWORD"])

        time.sleep(1)

        # ログインボタンをクリック
        login_button = self.driver.find_element_by_id("main").find_element_by_name("commit")
        login_button.click()

    # 部屋予約
    def room_reserve(self, start, term, room, event):
        self.driver.get('http://lastnote.swlab.cs.okayama-u.ac.jp/room_reservation/new?day=' + str(start.day) + '&month=' + str(start.month) + '&year=' + str(start.year))
        self.driver.find_element_by_id("room_reservation_start_time_4i").send_keys(start.hour)
        self.driver.find_element_by_id("room_reservation_start_time_5i").send_keys(start.minute)
        self.driver.find_element_by_id("utility_time").send_keys(term)
        self.driver.find_element_by_id("room_reservation_name").send_keys(event)
        self.driver.find_element_by_id("room_reservation_room_id").send_keys(room)
        submit = self.driver.find_element_by_id("create_submit")
        submit.click()
