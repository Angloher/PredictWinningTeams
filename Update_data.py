import numpy as np
import sys
import os
import urllib


class Downloader:
    def __init__(self):
        self.loc = "/home/daniel/Personal/PredictWinningTeams/Datasets" 
        self.leagues=[('Portoguese_league',(1,1),'P',0),('Turkish_league',(1,1),'T',0),('Eredivisie',(1,1),'N',0),('Belgian_league',(1,1),'B',0),('French_league',(1,2),'F',0),('Premier_league',(1,5),'E',1),('Bundesliga',(1,2),'D',0),('La_Liga',(1,2),'SP',0),('Scotish_league',(1,4),'SC',1),('SerieA',(1,2),'I',0),('Greek_league',(1,1),'G',0)]
        self.url_handle='https://www.football-data.co.uk/mmz4281/'
        

    def adjust_handle(self,j,league_handle,i):
        if league_handle=='E' and j==5:
            return 'C'
        else:
            return j-i

    def load_all_data(self):
        self.download_data(self.leagues,range(1993,2019))

    def update_season(self):
        self.download_data(self.leagues,[2019])

    def download_data(self, leagues, seasons):
        for season in seasons:
            for league,divisions,league_handle,adjust_name in leagues:
                for j in range(divisions[0],divisions[1]+1):
                    DIR = os.path.join(self.loc,league)
                    if not os.path.exists(DIR):
                        os.makedirs(DIR)
                    DIR = os.path.join(DIR,str(j))
                    if not os.path.exists(DIR):
                        os.makedirs(DIR)
                    try:
                        urllib.request.urlretrieve(url_handle+str(season)[-2:]+str(season+1)[-2:]+'/'+league_handle+str(adjust_handle(j,league_handle,adjust_name))+'.csv',os.path.join(DIR,'{}-{}.csv'.format(season,season+1)))
                        print('Download Successfull for {} in season {}'.format(league_handle,season))
                    except:
                        print('No Data for {} in season {}'.format(league_handle,season))
                    

def main():
    Loader=Downloader()
    if sys.argv[1] == 'update':
        Loader.update_season()
    elif sys.argv[1] == 'download':
        Loader.load_all_data()
    else:
        print('Wrong argument use update or download')

if __name__ == "__main__":
    main()




