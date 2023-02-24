from websites.ps3838.api.base_webaction import Gettable
from websites.ps3838.api.types import *
from dataclasses import dataclass

@dataclass
class GetBalance(Gettable):
    url: str = "https://api.ps3838.com/v1/client/balance"