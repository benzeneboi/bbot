from dataclasses import dataclass, field, asdict
from abc import ABC

""" class BaseWebAction:
    def __init__(self, url, params):
        self._url = url
        self._params = params """


@dataclass
class BaseAPI(ABC):
    url: str = field(init=False)
    #params: dict = field(init=False)

    def __post_init__(self):
        pass

    @property
    def params(self):
        return asdict(self)


class Gettable(BaseAPI):
    pass


class Postable(BaseAPI):
    pass
