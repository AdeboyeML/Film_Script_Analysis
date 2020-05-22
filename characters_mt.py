
import cufflinks as cf
from collections import Counter


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

# plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.express as px


class character_mentions:
    
    def __init__(self, df_movie, movie_characters, moviename):

        self.df_movie = df_movie
        self.movie = moviename
        self.characters = movie_characters
        
    def most_mentioned(self):
        
        def cap_sentence(s):
            return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)
        
        #Convert uppercase xters to words with just capitalizing the first letter
        character_cap = [cap_sentence(x.lower()) for x in self.characters]
        #combine both uppercase xters and the ones with just first letter in upper case
        character_cap = character_cap + self.characters
        
        xters_dialogue = []
        
        for x in self.df_movie.Scene_Dialogue:
            x = re.sub(r"\'s|\'S|\[|\]", '', str(x))
            loc = re.compile("({})+".format("|".join(re.escape(c) for c in character_cap)))
            tx = loc.findall(x)
            tx = [cap_sentence(y.lower()) for y in tx]
            xters_dialogue.append(tx)
            
        dialogues_xters = [y for x in xters_dialogue for y in x]
        character_mentions = dict(Counter(dialogues_xters).most_common())
        df_xters_mentions = pd.DataFrame(character_mentions.items(), columns = ['Characters', 'Number of Mentions']).sort_values(by = 'Number of Mentions')
        
        fig = px.bar(df_xters_mentions, x= 'Number of Mentions', y= 'Characters', orientation = 'h', 
                     hover_data=df_xters_mentions.columns, color='Number of Mentions', 
                     labels={'Number of Mentions':'<b> Number of Mentions <b>'}, width=1000, height= 800, 
                     color_continuous_scale=px.colors.cyclical.Edge)
        
        fig.update_layout(title='<b> Most mentioned characters in the ' + self.movie + ' movie based on the scene dialogues<b>', xaxis_title='<b> Number of Mentions <b>', 
                          yaxis_title='<b> Characters <b>')
        
        iplot(fig)
        
        return character_mentions
    
    def top_xters_mentions(self, character_mention, num_of_characters):
        
        def cap_sentence(s):
            return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)
        
        #Convert uppercase xters to words with just capitalizing the first letter
        character_cap = [cap_sentence(x.lower()) for x in self.characters]
        #combine both uppercase xters and the ones with just first letter in upper case
        character_cap = character_cap + self.characters
        
        xters = [keys for keys in character_mention]
        top_xters = xters[:num_of_characters]
        most_mentions = []
        xters_dialogue = []
        
        for x in self.df_movie.Scene_Dialogue:
            x = re.sub(r"\'s|\'S|\[|\]", '', str(x))
            loc = re.compile("({})+".format("|".join(re.escape(c) for c in character_cap)))
            tx = loc.findall(x)
            tx = [cap_sentence(y.lower()) for y in tx]
            xters_dialogue.append(tx)
            
        for scene_mentions in xters_dialogue:
            mentions = []
            for xter in scene_mentions:
                if xter in top_xters:
                    mentions.append(xter)
            most_mentions.append(mentions)
            
        most_mentions_ct = [dict(Counter(x).most_common()) for x in most_mentions]
        df_most_mentions = pd.DataFrame(most_mentions_ct)
        fig = df_most_mentions.iplot(asFigure = True, kind = 'bar')
        fig.update_layout(title='<b> Appearance of the ' + str(num_of_characters) + ' most-mentioned characters in Scene Dialogues across ' + self.movie + ' Movie <b>', 
                          xaxis_title='<b> Scenes <b>', legend_title_text='<b> ' + str(num_of_characters) + ' Most-talked about Xters <b>', 
                          yaxis_title = '<b> Number of mentions <b>', width = 1000)
        fig.update_xaxes(dtick=10)
        iplot(fig)
        
        
    def talk_about_xters(self, df, name):
        
        def cap_sentence(s):
            return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)
        
        character_cap = [cap_sentence(x.lower()) for x in self.characters]
        character_cap = character_cap + self.characters
        character_cap = [re.sub(name, '', x, flags = re.IGNORECASE) for x in character_cap]
        character_cap = [x for x in character_cap if x]
        #print(character_cap)
        xter_mentions = []
        for x in df.loc[df['characters'] == name]['Character_dialogue']:
            x = re.sub(r"\'s|\'S|\[|\]", '', str(x))
            loc = re.compile("({})+".format("|".join(re.escape(c) for c in character_cap)))
            tx = loc.findall(x)
            tx = [cap_sentence(y.lower()) for y in tx]
            xter_mentions.append(tx)
        xter_mentions = [y for x in xter_mentions for y in x]
        mt_ct = dict(Counter(xter_mentions).most_common())
        df_mentions = pd.DataFrame(mt_ct.items(), columns = ['Characters', 'Number of Mentions']).sort_values(by = 'Number of Mentions')
        if len(df_mentions) <= 5:
            height = 300
        else:
            height = 600
        fig = px.bar(df_mentions, x= 'Number of Mentions', y= 'Characters', orientation = 'h', 
                     hover_data=df_mentions.columns, color='Number of Mentions', 
                     labels={'Number of Mentions':'<b> Number of Mentions <b>'}, width=900, height= height, 
                     color_continuous_scale=px.colors.cyclical.Edge)
        
        fig.update_layout(title='<b> Characters that ' + name + ' mentioned / talked-about the most in the ' + self.movie + ' Movie <b>', xaxis_title='<b> Number of Mentions <b>', 
                          yaxis_title='<b> Characters <b>')
        
        iplot(fig)
        
        return df_mentions
    
    
    def most_talked_with(self, name):
        
        def xter_count_perscene(df, characters):
            
            sc_xters = []
            sc_dia = []
            
            for x in range(0, len(df), 1):
                sc_xtrs = []
                sc_di = []
                
                if df['Scene_Characters'][x] != None:
                    for y in range(0, len(df['Scene_Characters'][x]), 1):
                        if type(characters) == list:
                            kk = re.compile("({})+".format("|".join(re.escape(c) for c in characters)))
                            xters = kk.findall(df['Scene_Characters'][x][y])
                        else:
                            xters = re.findall(characters, df['Scene_Characters'][x][y])
                        if xters:
                            dialogue = df['Scene_Dialogue'][x][y]
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
        
        talked_with_xters = {}
        main_xter = []
        other_xter = []
        for x in self.characters:
            if x == name:
                main_xter.append(x)
            else:
                other_xter.append(x)
                
        for x in other_xter:
            xter = []
            xter.append(x)
            for y in main_xter:
                xter.append(y)
                df_xter_ct, df_xter_xt = xter_count_perscene(self.df_movie, xter)
                if len(df_xter_ct) == 0:
                    talked_with_xters[x] = None
                else:
                    talked_with_xters[x] = len(df_xter_ct)
                    
        df_talked_with = pd.DataFrame(talked_with_xters.items(), columns = ['Characters', 'counts']).sort_values(by = 'counts')
        df_talked_with.dropna(inplace = True)
        
        fig = px.bar(df_talked_with, x= 'counts', y= 'Characters', orientation = 'h', 
                     hover_data=df_talked_with.columns, color='counts', 
                     labels={'counts':'<b> Counts <b>'}, width=1000, height= 700, 
                     color_continuous_scale=px.colors.diverging.PRGn)
        
        fig.update_layout(title='<b> Characters ' + name + ' interacted / talked with in ' + self.movie + ' movie <b>', xaxis_title='<b> Amount of Consversations <b>', 
                          yaxis_title='<b> Characters <b>')
        
        iplot(fig)
        
        return df_talked_with