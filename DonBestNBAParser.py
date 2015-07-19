from bs4 import BeautifulSoup
import logging
import re

class DonBestNBAParser:

    def __init__(self,**kwargs):

        if 'logger' in kwargs:
            self.logger = kwargs['logger']
        else:
            self.logger = logging.getLogger(__name__)

    def odds(self,content,game_date=None):

        try:
            soup = BeautifulSoup(content,"lxml")
            tbl = soup.find("div", {"id": "oddsHolder"}).find("table")
            games = []

            headers = ["rot_away", "rot_home", "opening_line", "opening_over_under", "away_team", "home_team", "time", "away_score", "home_score", "status", "status2", "Westgate_line", "Westgate_over_under", "Mirage_line", "Mirage_over_under", "Station_line", "Station_over_under", "Pinnacle_line", "Pinnacle_over_under", "SIA_line", "SIA_over_under", "SBG_line", "SBG_over_under", "BetUS_line", "BetUS_over_under", "BetPhoenix_line", "BetPhoenix_over_under", "EasyStreet_line", "EasyStreet_over_under", "Bodog_line", "Bodog_over_under", "Jazz_line", "Jazz_over_under", "Sportsbet_line", "Sportsbet_over_under", "BookMaker_line", "BookMaker_over_under", "DSI_line", "DSI_over_under", "BetJamaica_line", "BetJamaica_over_under"]

            for tr in tbl.findAll("tr", {"class": re.compile(r'statistics_table_')}):
                values = []
                for td in tr.findAll("td"):
                    for val in td.findAll(text=True):
                        values.append(val)
            
                game = dict(zip(headers, values))
                games.append(game)

        except:
            self.logger.exception('odds failed')

    # ship it
    return games

if __name__ == "__main__":
  pass
