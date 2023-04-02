import re
import datetime
import time
import requests

import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from collections import namedtuple
from dotenv import load_dotenv


load_dotenv()


def get_env_var(key):
    try:
        return os.environ[key]
    except KeyError:
        raise Exception(f"Missing {key} environment variable.")


Credentials = namedtuple("Credentials", ["username", "password"])
creds = Credentials(username=get_env_var("ANN_USERNAME"), password=get_env_var("ANN_PASSWORD"))

class ANN:

    def __init__(self, credentials):
        self.root_url = "https://actionnetwork.com"
        self.wd: WebDriver = None
        self.credentials: Credentials = credentials
        self.recent_data = None

    def start_webdriver(self, browser="chrome", uc_driver=False):
        """
        : arg[0] - browser type
            : "chrome" (default)
            : "firefox"
        : arg[1] - use undetected driver
            : True
            : False (default)
        """
        if browser == "chrome":
            self.wd = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )
        elif browser == "firefox":
            self.wd = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )

    def login(self):
        """perform login procedure on actionnetwork
            - Go to the root url
            - find Log In button and click
            - find login fields, send keys and press ENTER to log in
        """
        self.go_to(self.root_url)
        try:
            login_button = self.wd.find_element(By.CLASS_NAME, "nav__login")
        except NoSuchElementException:
            print("Already logged in or could not find log in button.")
            return
        login_button.click()
        time.sleep(2)
        input_fields = self.wd.find_elements(By.TAG_NAME, "input")
        num_fields = len(input_fields)
        if num_fields != 2:
            raise Exception("Incorrect number of input fields. Expected 2 got {num_fields}.")
        email, password = input_fields
        email.send_keys(self.credentials.username)
        time.sleep(3)
        password.send_keys(self.credentials.password + Keys.ENTER)
        time.sleep(6)

    def go_to(self, url):
        self.wd.get(url)
        time.sleep(5)

    def _get_login_elements(self):
        """Finds the credentials input fields"""
        input_fields = self.wd.find_elements(
            By.TAG_NAME, "input")
        fields = {}
        for elem in input_fields:
            if elem.get_attribute("name").lower() == "email":
                fields["username"] = elem
            elif elem.get_attribute("name").lower() == "password":
                fields["password"] = elem
        if not fields.get("username") or not fields.get("password"):
            raise Exception
        return fields

    def _convert_to_datetime(self, date, time):
        """
        : date: mm/dd
        : time: xx:xx (a/p)m

        datetime: yyyy/mm/dd,xx:xx am/pm
        """
        return datetime.datetime.strptime(date + "," + time, "%Y/%m/%d,%I:%M %p")

    def _prune(self, data):
        """Remove irrelevant data in the container and 
        convert date and time to datetime object"""
        exclude = "\d+/\d+\\n\d+:\d+|Picks?|Date|Game|Spread|Moneyline|Total"
        relevant = [elem for elem in data[1:] if not re.search(exclude, elem)]
        data = []
        if len(relevant) % 3 != 0:
            raise Exception("Unexpected number of entries in data")
        for i in range(0, len(relevant), 3):
            date, time = relevant[i], relevant[i + 1]
            team_1, team_2 = relevant[i + 2].split('\n')
            #self._convert_to_datetime(date, time)
            data.append(
                {
                    "date": relevant[i],
                    "time": relevant[i + 1], 
                    "team_1": team_1, 
                    "team_2": team_2
                })
        return data
    
    def _get_sport_types(self, data):
        """regex searches relevant urls for the game type"""
        return [re.search('/(\w+)-game', i).group(1) for i in data]

    def _get_years(self, data):
        """searches urls for the year of the match"""
        return [re.search('(\d+)/', i).group(1) for i in data]

    def get_data(self, url="https://www.actionnetwork.com/pro-systems/my-systems"):
        """
        :Args
            : url - url in question to scrape from
            : container - class_name of the container to find
            : container_tags - tag names of required elements in container i.e. div, a
            : container_tag_attributes - attribute names of container tags i.e. href
        1. finds webelement container
        2. finds all div text in the container (to extract date, time, team1, team2)
        3. finds all link text in the container (to extract sport type and year)
        4. prunes the div text data for relevant data
        5. extracts year and sport types from link text
        6. returns dictionary with relevant sport data in the format {sport, team_1, team_2, game_date_time, bet_window}
        """
        if url != self.wd.current_url:
            self.go_to(url)
        container   = self.wd.find_element(By.CLASS_NAME, "my-systems__desktop")
        link_elems  = container.find_elements(By.TAG_NAME, "a")
        divs        = container.find_elements(By.TAG_NAME, "div")
        div_text    = [div.text for div in divs]
        links       = [i.get_attribute('href') for i in link_elems]
        data        = self._prune(div_text)
        sport_types = self._get_sport_types(links)
        years       = self._get_years(links)
        for entry, sport, year in zip(data, sport_types, years):
            date = year + "/" + entry["date"]
            date_time = self._convert_to_datetime(date, entry["time"])
            del entry["date"]
            del entry["time"]
            entry.update({"game_date_time": date_time.isoformat(), "sport": sport})
        self.recent_data = data

        return data
    
    def hash_data(self, data):
        """
        Checks if data is duplicate
        """
    
    def entry_in_db(self, entry) -> bool:
        f'''
        Checks if the entry is already in the database
        query {{
            considerations() {{
                
            
            }}
        }}
        '''

    def find_bets_within_window(self, data, window=10):
        """
        After pruning and formatting the data, 
            check whether any bets should be made
        : Args
            : data - pruned and formatted data {'sport', 'team_1', 'team_2', 'game_date_time'}
            : window - the time window in minutes to check within
        """
        window = datetime.timedelta(minutes=get_env_var('BET_WINDOW'))
        for dat in data:
            curr_delta = dat['game_date_time'] - datetime.datetime.now()
            if curr_delta <= window and curr_delta > 0:
                """
                if entry is not in the database
                    Add entry to db
                    Send notfication email
                """
                if self.entry_in_db(dat):
                    continue
                self.update_database(dat)
                

    

    def monitor_data(self, refresh_time=2):
        """
        Monitors the page by scraping data every 2 minutes
        """
        while True:
            data = self.get_data()
            print(data)
            self.update_database(data)
            time.sleep(refresh_time*60) # 2 minutes

    def update_database(self, data):
        """
        Sends mutation query to graphql to update database
        """
        for dat in data:
            body = f"""
            mutation {{
                    mutateConsiderations(
                        team1: "{dat['team_1']}",
                        team2: "{dat['team_2']}",
                        sport: "{dat['sport']}",
                        gameDateTime: "{dat['game_date_time'].isoformat()}",
                        betWindow: "{datetime.time(0, get_env_var('BET_WINDOW')).isoformat()}"
                    ) {{
                        consideration {{
                        
                            team1
                            team2
                            sport
                            gameDateTime
                            currDateTime
                            betWindow
                        }}
                       
                    }}
                }}
                    """
            #print(body)
            r = requests.post(get_env_var("GRAPHQL_URI"), json={"query": body})
            print("r.content", r.content)

    def start(self):
        """sequentially calls functions `login()` and starts continuous \
        scraping -> pruning -> databse modification"""
        self.start_webdriver()
        self.login()
        self.monitor_data()

        