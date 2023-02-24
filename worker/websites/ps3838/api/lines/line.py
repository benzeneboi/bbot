from websites.ps3838.api.base_webaction import Gettable
from websites.ps3838.api.types import *
from dataclasses import dataclass


@dataclass
class Straight(Gettable):
    url: str = "https://api.ps3838.com/v2/line",
    league_id: league_id_t = None,
    handicap = None,
    odds_format: odds_format_t = "DECIMAL",
    sport_id: sport_id_t = None,
    event_id: event_id_t = None,
    period_number: Union[None, int] = None,
    bet_type: bet_t = "MONEYLINE",
    team: Union[None, team_t] = None,
    side: Union[None, side_t] = None
