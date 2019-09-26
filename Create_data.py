import numpy as np
import pandas as pd
from datetime import datetime as dt
import itertools
import os
import datetime
import csv

class Feature_extractor:
    def __init__(self):
        self.loc = "/home/daniel/Personal/PredictWinningTeams/Datasets"
        self.leagues=[('Eredivisie',(1,1)),
            ('French_league',(1,2)),
            ('Premier_league',(1,5)),
            ('SerieA',(1,2)),
            ('La_Liga',(1,2)),
            ('Bundesliga',(1,2)),
            ('Portoguese_league',(1,1)),
            ('Turkish_league',(1,1)),
            ('Belgian_league',(1,1)),
            ('Greek_league',(1,1))]#,
                    #('Swiss_league',(1,1)),('Finish_league',(1,1)),('Austrian_league',(1,1))]
                 #('Scotish_league',(1,4)),('Chinese_league',(1,1)),('Norwegian_league',(1,1)),
                 #('Russian_league',(1,1)),('Swedish_league',(1,1)),('Brazilian_league',(1,1)),
                 #('Polish_league',(1,1)),('Romanian_league',(1,1)),('Mexican_league',(1,1)),
                 #('Japanese_league',(1,1)),('Danish_league',(1,1))]#]
    #current_season=18
    #num_last_games=20
    #num_last_year_data=6
    #current_date=(datetime.datetime.now()-datetime.timedelta(1)).strftime('%Y-%m-%d').split('-')

    def process_data(self):
        self.load_data()
        self.apply_Date_conversion()
        self.get_playing_stats()


    def load_data(self):
        self.raw_data=[]
        for league,divisions in self.leagues:
            league_data=[]
            for j in range(divisions[0],divisions[1]+1):
                division_data=[]
                DIR = os.path.join(self.loc,league,str(j))
                for i in range(1993,2019):
                    if os.path.isfile(os.path.join(DIR,'{}-{}.csv'.format(i,i+1))):
                        try:
                            division_data.append(pd.read_csv(os.path.join(DIR,'{}-{}.csv'.format(i,i+1))))
                        except:
                            print('Error in file format please manualy clean file '+os.path.join(DIR,'{}-{}.csv'.format(i,i+1)))
                league_data.append(division_data)
            self.raw_data.append(league_data)

    def parse_date(self,date):
        #print date
        if date == '':
            return None
        else:
            try:
                return dt.strptime(str(date), '%d/%m/%y').date()
            except ValueError:
                try: 
                    return dt.strptime(str(date), '%d/%m/%Y').date()
                except ValueError:
                    try:
                        return dt.strptime(str(date), '%Y-%m-%d').date()
                    except ValueError:
                        return None

    def apply_Date_conversion(self):
        for league_data in self.raw_data:
            for division_data in league_data:
                for i in range(len(division_data)):
                    #print division_data[i]
                    division_data[i].Date=division_data[i].Date.apply(self.parse_date)

    def get_playing_stats(self):
        #Gets all the statistics related to gameplay                      
        all_columns=['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','Div','HS','AS','HST','AST','HC','AC','B365H','B365D','B365A']
        self.playing_stats=[]

        for league_data in self.raw_data:
            playing_data=[]
            for division_data in league_data:
                division_stats=[]
                for i in range(len(division_data)):
                    extract_columns=[]
                    for column in all_columns:
                        if column in division_data[i].columns:
                            extract_columns.append(column)
                    division_stats.append(division_data[i][extract_columns])
                playing_data.append(division_stats)
            self.playing_stats.append(playing_data)

def main():
    Extractor=Feature_extractor()
    Extractor.process_data()
    #print(Extractor.playing_stats)

if __name__ == "__main__":
    main()