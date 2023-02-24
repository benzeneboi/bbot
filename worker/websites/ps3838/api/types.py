from typing import Literal, Union
from uuid import UUID

bet_t = Literal["SPREAD", "MONEYLINE", "TOTAL_POINTS", "TEAM_TOTAL_POINTS"]
team_t = Union[None, Literal["Team1", "Team2", "Draw"]]
side_t = Union[None, Literal["OVER", "UNDER"]]
odds_format_t = Literal["American", "DECIMAL",
                        "HongKong", "Indonesian", "Malay"]
wrs_t = Literal["WIN", "RISK"]
fill_t = Literal["NORMAL", "FILLANDKILL", "FILLMAXLIMIT"]
sport_id_t = Union[None, int]
event_id_t = sport_id_t
period_no_t = sport_id_t
line_id_t = sport_id_t
league_id_t = sport_id_t
event_ids_t = Union[None, list[int]]

urid_t = Union[None, UUID]

handicap_t = Union[None, float]
currency_t = Literal["AUD", "USD", "EUR"]
league_ids_t = Union[None, list[int]]
