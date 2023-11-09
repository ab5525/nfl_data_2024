import pandas as pd
import numpy as np

def find_play_type(plays_df,phrase:str = 'fumbl',disp=False):
    matches = []
    for i in plays_df['playDescription'].unique():
        if phrase in i.lower():
            if disp:
                print(i)
            matches.append(i)
    if len(matches) == 0:
        print('No matches found')
    else:
        print('Number of matches for {}: {}'.format(phrase,len(matches)))
        
    return matches


#adapted from kaggle.com
def reverse_play_direction(df):
        result_df = df.copy(deep=True)
        result_df["o"] = result_df["o"].apply(lambda o: 360 - o)
        result_df["o"] = result_df["o"].replace(360, 0)
        
        result_df["dir"] = result_df["dir"].apply(lambda dir: 360 - dir)
        result_df["dir"] = result_df["dir"].replace(360, 0)
        
        result_df["x"] = result_df["x"].apply(lambda x: 120 - x)
        
        result_df["y"] = result_df["y"].apply(lambda y: 160/3 - y)
        
        return result_df