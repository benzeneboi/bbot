from websites.ps3838.api.base_webaction import Gettable
from websites.ps3838.api.types import *
from dataclasses import dataclass


@dataclass
class Straight(Gettable):
    """
            :return format
                {
                "sportId": 0,
                "last": 0,
                "leagues": [
                    {
                    "id": 0,
                    "events": [
                        {
                        "id": 0,
                        "awayScore": 0,
                        "homeScore": 0,
                        "awayRedCards": 0,
                        "homeRedCards": 0,
                        "periods": [
                            {
                            "lineId": 0,
                            "number": 0,
                            "cutoff": "2019-08-24T14:15:22Z",
                            "status": 1,
                            "maxSpread": 0,
                            "maxMoneyline": 0,
                            "maxTotal": 0,
                            "maxTeamTotal": 0,
                            "moneylineUpdatedAt": "2019-08-24T14:15:22Z",
                            "spreadUpdatedAt": "2019-08-24T14:15:22Z",
                            "totalUpdatedAt": "2019-08-24T14:15:22Z",
                            "teamTotalUpdatedAt": "2019-08-24T14:15:22Z",
                            "spreads": [
                                {
                                "altLineId": 0,
                                "hdp": 0,
                                "home": 0,
                                "away": 0,
                                "max": 0
                                }
                            ],
                            "moneyline": {
                                "home": 0,
                                "away": 0,
                                "draw": 0
                            },
                            "totals": [
                                {
                                "altLineId": 0,
                                "points": 0,
                                "over": 0,
                                "under": 0,
                                "max": 0
                                }
                            ],
                            "teamTotal": {
                                "home": {
                                "points": 0,
                                "over": 0,
                                "under": 0
                                },
                                "away": {
                                "points": 0,
                                "over": 0,
                                "under": 0
                                }
                            },
                            "awayScore": 0,
                            "homeScore": 0,
                            "awayRedCards": 0,
                            "homeRedCards": 0
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            """
    url: str = "https://api.ps3838.com/v3/odds"
    sport_id: sport_id_t = None,
    league_ids: league_ids_t = None,
    odds_format: odds_format_t = "DECIMAL",
    since = None,
    is_live = None,
    event_ids: event_ids_t = None,
    to_currency_code: currency_t = "AUD"
