
import operator
import  pprint
import pylab
import networkx as net
import itertools
import matplotlib.cm as cmx
from matplotlib.pyplot import pause
import matplotlib.pyplot as plt

from ibm_watson import PersonalityInsightsV3
import json
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






class interaction:
    
    def __init__(self, df_movie, moviename):

        self.df_movie = df_movie
        self.movie = moviename
        
    def character_interaction(self):
        
        #Get character interaction lists
        graph_list = []
        for scene_xters in self.df_movie['Scene_Characters'].values:
            if scene_xters != None:
                sc_characters = []
                for y in scene_xters:
                    if y not in sc_characters:
                        sc_characters.append(y)
                        graph_list.append(sc_characters)
                        
        return graph_list
    
    
    def top10_character_interaction(self, characters):
        
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
        
        df_cts, df_xt = xter_count_perscene(self.df_movie, characters)
        
        #Get character interaction lists
        graph_list = []
        for scene_xters in df_xt['characters'].values:
            if scene_xters != None:
                sc_characters = []
                for y in scene_xters:
                    if y not in sc_characters:
                        sc_characters.append(y)
                        graph_list.append(sc_characters)
        return graph_list
    
    def character_interaction_plot(self, G, page_ranked_nodes):
        
        fig = plt.figure(figsize=(20,20))
        ax = fig.add_subplot(111)
        
        node_list = page_ranked_nodes.keys()
        size_list = list()
        for k in page_ranked_nodes.keys():
            size_list.append(15000*page_ranked_nodes[k])
        
        
        current_palette = sns.color_palette("muted",n_colors=G.number_of_edges())
        node_palette = sns.color_palette("muted",n_colors= len(node_list))
        
        widths=[]
        for (u,v,d) in G.edges(data=True):
            widths.append(len(G.get_edge_data(u,v)))
            
        sorted_ranks = sorted(page_ranked_nodes.items(), key=operator.itemgetter(1))
        sorted_ranks.reverse()
        
        i= 1
        ordered_chars = list()
        for k in sorted_ranks:
            ordered_chars.append(k[0])
            i+=1
            
        net.draw_networkx(G,pos=net.spring_layout(G,k=3.9,iterations=50),edge_color = current_palette, 
                          node_color = node_palette,nodelist= node_list,node_size=size_list, 
                          font_size=14,color='blue',alpha = 0.98,linewidths =2,width = widths, 
                          edge_size = 0.4,font_family = "DejaVu Sans",font_color = 'black',ax =ax)
        
        if len(page_ranked_nodes) == 10:
            plt.title('The Top 10 Characters Interaction Mapping for ' + self.movie + ' Movie',fontsize =20)
        else:
            plt.title('Character Interaction Mapping for ' + self.movie + ' Movie',fontsize =20)
        plt.show()