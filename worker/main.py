import utils
import time
import websites
from websites import *



if __name__ == '__main__':
    utils.load_env(".env")
    creds = utils.get_credentials("PS3838_USERNAME", "PS3838_PASSWORD")
    ps = PS3API(creds)
    #print(creds)
    print(ps.get(ps3Leagues(sport_id=4)))
    print(ps.get(ps3GetBalance()))
    print(ps3Leagues(sport_id=4))
    """ while True:
        data = ann.get_data()
        found_bets = ann.find_bets_within_window(data)
        if found_bets:
            bets = utils.convert_ann_sport_to_ps_sport(found_bets)
            ps.get()
        time.sleep(120) """ 
