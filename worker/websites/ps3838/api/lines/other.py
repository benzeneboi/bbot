from dataclasses import dataclass
from websites.ps3838.api.base_webaction import Gettable
from websites.ps3838.api.types import *

@dataclass
class Sports(Gettable):
    url: str = "https://api.ps3838.com/v3/sports"

@dataclass
class Leagues(Gettable):
    url: str = "https://api.ps3838.com/v3/leagues"
    sport_id: sport_id_t = None
