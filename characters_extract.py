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


class extract_characters:
    
    def __init__(self, df_movie, df_movie_dialogues, df_movie_xters, moviename):
        
        self.df_movie = df_movie
        self.df_movie_dialogues = df_movie_dialogues
        self.df_movie_xters = df_movie_xters
        self.movie = moviename
        
    def extract_character_plot(self):
        
        #remove unwanted words from characters
        direct_xters = self.df_movie_xters['characters'].values.tolist()
        dialog_xters = self.df_movie_dialogues['characters'].values.tolist()
        actual_xters = [x for x in direct_xters if x in dialog_xters]
        
        #count how many times each character appeared in the movie script
        character_count = dict(Counter(actual_xters).most_common())
        
        #Drop xters with JUST one appearance, because they appear to be just noise or random characters 
        character_count = {k:v for k,v in character_count.items() if v > 1}
        characters = [keys for keys in character_count]
        
        df_character_ct = pd.DataFrame(character_count.items(), columns = ['Characters', 'counts']).sort_values(by='counts')
        
        ##Plot character appearances in the movie script
        fig = px.bar(df_character_ct, x= 'counts', y= 'Characters', orientation = 'h', 
                     hover_data=df_character_ct.columns, color='counts', 
                     labels={'counts':'<b> Character Counts <b>'}, width=1000, height=1000)
        
        fig.update_layout(title='<b> Number of Times Characters appeared in the ' + self.movie + ' Movie <b>', xaxis_title='<b> Counts <b>',\
                      yaxis_title='<b> Characters <b>')
        
        iplot(fig)
        
        ##Lets check the numbers of scenes each character appeared in
        
        xter_per_scene = {}
        for word in characters:
            count = 0
            for x in range(0, len(self.df_movie), 1):
                scene_characters = self.df_movie['Scene_Characters'][x]
                if scene_characters != None:
                    if word in scene_characters:
                        count += 1
                        xter_per_scene[word] = count
                        
        ##Plot the number of scenes each character in the movie appeared in
        df_perscene = pd.DataFrame(xter_per_scene.items(), columns = ['Characters', 'Scene counts']).sort_values(by = 'Scene counts')
        fig = px.bar(df_perscene, x= 'Scene counts', y= 'Characters', orientation = 'h', 
                     hover_data=df_perscene.columns, color='Scene counts', 
                     labels={'Scene counts':'<b> Scene Counts <b>'}, width=1000, height=900,
                     color_continuous_scale=px.colors.sequential.speed)
        
        fig.update_layout(title='<b> Number of Scenes Each Character Spoke In, in the ' + self.movie + ' movie <b>', xaxis_title='<b> Scene counts <b>',
                      yaxis_title='<b> Characters <b>')
        
        iplot(fig)
        
        return characters
        