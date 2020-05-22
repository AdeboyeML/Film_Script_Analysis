

import cufflinks as cf
from collections import Counter


import random
import secrets

# nltk
from nltk.corpus import names
from nltk import tokenize
import nltk
from nltk.tokenize import word_tokenize


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





class gender:
    
    def __init__(self, movie_characters, moviename):

        self.movie = moviename
        self.characters = movie_characters
        
    def gender_types(self, color):
        
        characters = [x.lower() for x in self.characters]
        
        #Gender identification
        nltk.download('names')
        labeled_names = ([(name, 'male') for name in names.words('male.txt')] + \
                         [(name, 'female') for name in names.words('female.txt')])
        random.shuffle(labeled_names)
        
        def gender_features(word):
            return {'suffix1': word[-1:].lower(), 'suffix2': word[-2:].lower(), 
                    "first_letter" : word[0].lower(),"last_letter" : word[-1].lower()}
        
        train_names = labeled_names[500:]
        test_names = labeled_names[:500]
        train_set = [(gender_features(n), gender) for (n, gender) in train_names]
        test_set = [(gender_features(n), gender) for (n, gender) in test_names]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        
        def gender_id(major_characters):
            
            female = {}
            male = {}
            for word in major_characters:
                gender = classifier.classify(gender_features(word))
                if gender == 'male':
                    male[word] = gender
                else:
                    female[word] = gender
                    
            return female, male
        
        female_xters, male_xters = gender_id(characters)
        female_xters = list(female_xters.keys())
        male_xters = list(male_xters.keys())
        
        gender_dict = {}
        gender_dict['Male'] = len(male_xters)
        gender_dict['Female'] = len(female_xters)
        df_gend = pd.DataFrame(gender_dict.items(), columns = ['gender', 'size'])
        
        ##Plot Gender Distribution
        fig = px.pie(df_gend, values='size', names='gender', 
                     title='Gender Distribution in ' + self.movie + ' movie', 
                     hover_data= df_gend.columns, color_discrete_sequence=color)
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.show()
        
        return df_gend