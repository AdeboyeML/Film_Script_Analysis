
import cufflinks as cf
from collections import Counter

import glob
import os
import shutil
import random
import secrets


# nltk
from nltk.corpus import names
from nltk import tokenize
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize
from nltk.stem.snowball import SnowballStemmer

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
'exec(%matplotlib inline)'

# plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.express as px




class scene_dialogues:
    
    def __init__(self, df_movie, moviename):

        self.df_movie = df_movie
        self.movie = moviename
        
    def xter_count_perscene(self, characters):
        
        sc_xters = []
        sc_dia = []
        
        for x in range(0, len(self.df_movie), 1):
            sc_xtrs = []
            sc_di = []
            
            if self.df_movie['Scene_Characters'][x] != None:
                for y in range(0, len(self.df_movie['Scene_Characters'][x]), 1):
                    if type(characters) == list:
                        kk = re.compile("({})+".format("|".join(re.escape(c) for c in characters)))
                        xters = kk.findall(self.df_movie['Scene_Characters'][x][y])
                    else:
                        xters = re.findall(characters, self.df_movie['Scene_Characters'][x][y])
                    if xters:
                        dialogue = self.df_movie['Scene_Dialogue'][x][y]
                        sc_xtrs.append(xters)
                        sc_di.append(dialogue)
                sc_xtrs = [''.join(el) for el in sc_xtrs]
                sc_xters.append(sc_xtrs)
                sc_dia.append(sc_di)
                #print(xters, '\n', dialogue)
            else:
                sc_xters.append(None)
                sc_dia.append(None)
                
        #Count the appearance of 1, 2 or more characters per scene
        sc_cts = []
        for x in range(0,len(sc_xters),1):
            xtrs = dict(Counter(sc_xters[x]).most_common())
            sc_cts.append(xtrs)
            
        #Create a dataframe of their appearance
        df_counts = pd.DataFrame(sc_cts)
        
        #drop items not in the characters we want
        ct_columns = df_counts.columns.tolist()
        drop_items = [x for x in ct_columns if x not in characters]
        for x in drop_items:
            df_counts.drop([x], axis = 1, inplace = True)
        df_counts.dropna(inplace = True)
        
        df_scene_dialogue = pd.DataFrame(list(zip(sc_xters, sc_dia)), columns = ['characters', 'dialogues'])
        return df_counts, df_scene_dialogue
    
    def scene_dialogue_plot (self, df):
        
        #convert column names into strings
        content = ""
        if len(df.columns) == 1:
            content = ''.join(df.columns)
        else:
            content = ' and '.join(df.columns)
        
        ##plot the numbers of dialogue for a specific character or more characters per scene across the movie script
        fig = df.iplot(asFigure = True, kind = 'bar')
        
        fig.update_layout(title='<b> Appearances of ' + content + ' dialogues per scene across ' + self.movie + ' Movie <b>', 
                          xaxis_title='<b> Scenes <b>', yaxis_title = '<b> Amount of Dialogue <b>', width = 1000)
        fig.update_xaxes(dtick=10)
        iplot(fig)
        
    def character_appearances(self, movie_characters):
        
        scene_number = []
        xters = []
        sc_num = 0
        for x in range(len(self.df_movie)):
            sc_num += 1
            for y in movie_characters:
                if self.df_movie['Scene_Characters'][x]:
                    if y in self.df_movie['Scene_Characters'][x]:
                        xters.append(y)
                        scene_number.append(sc_num)
        df_app = pd.DataFrame(list(zip(xters, scene_number)), columns = ['characters', 'Scene Numbers'])
        
        fig = px.strip()
        fig['layout']['yaxis']['autorange'] = "reversed"
        fig = px.strip(data_frame = df_app, x = 'Scene Numbers', y = 'characters', 
                       hover_data=df_app.columns, color='characters', labels={'characters':'<b> Scene Characters <b>'},
                       width=1000, height= 800)
        #fig['layout']['yaxis']['autorange'] = "reversed"
        fig.update_layout(title='<b> Appearances of characters ordered by their first appearance, in the ' + self.movie + ' movie <b>', xaxis_title='<b> Scene Numbers <b>', 
                          yaxis_title='<b> Scene Characters <b>')
        iplot(fig)
        
        return df_app