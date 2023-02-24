from websites.ps3838.api.base_webaction import Postable
from websites.ps3838.api.types import *
from dataclasses import dataclass


@dataclass
class Straight(Postable):
    url: str = "https://api.ps3838.com/v2/bets/place"
    odds_format: odds_format_t = "DECIMAL"
    urid: urid_t = None  # = generate_uuid()
    accept_better_line: bool = False
    stake: float = 0.0  # = 0.0
    win_risk_stake: wrs_t = "WIN"  # = None
    line_id: line_id_t = None  # = None
    alt_line_id: Union[int, None] = None
    pitcher1_must_start: Union[bool, None] = None  # = None
    pitcher2_must_start: Union[bool, None] = None  # = None
    fill_type: fill_t = "NORMAL"
    sport_id: sport_id_t = None
    event_id: event_id_t = None
    period_number: period_no_t = None
    bet_type: bet_t = "MONEYLINE"
    team: team_t = None
    side: side_t = None
    handicap: handicap_t = None
