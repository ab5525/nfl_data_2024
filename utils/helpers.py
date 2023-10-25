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