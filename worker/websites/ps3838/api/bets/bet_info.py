from websites.ps3838.api.base_webaction import Gettable
from websites.ps3838.api.types import *
from dataclasses import dataclass


@dataclass
class Running(Gettable):
    url: str = "https://api.ps3838.com/v3/bets"
    bet_list: Union[Literal["ALL"], None] = None
    bet_statuses: Union[Literal["ACCEPTED"], None] = None
    from_date: Union[str, None] = None
    to_date: Union[str, None] = None
    sort_dir: Literal["ASC"] = None
    page_size: int = 1000
    from_record: int = 0
    bet_ids: Union[list[int], None] = None
    urids: Union[list[int], None] = None
