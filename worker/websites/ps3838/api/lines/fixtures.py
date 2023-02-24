from websites.ps3838.api.base_webaction import Gettable
from websites.ps3838.api.types import *
from dataclasses import dataclass

@dataclass
class Normal(Gettable):
    url: str = "https://api.ps3838.com/v3/fixtures"
    sport_id: sport_id_t = None
    league_ids: league_ids_t = None
    event_ids: event_ids_t = None

