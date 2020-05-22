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
import matplotlib.pyplot as plt

# plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.express as px



class emotions_sentiments:
    
    def __init__(self, df_movie, moviename):

        self.df_movie = df_movie
        self.movie = moviename
        
    def film_sentiment(self, colour):
        
        analyzer = SentimentIntensityAnalyzer()
        sc_sent = {}
        
        for x in range(0, len(self.df_movie), 1):
            
            scene = re.sub(r"[^a-zA-Z0-9.? ]+", '', self.df_movie.Contents[x])
            scene_sentence = tokenize.sent_tokenize(scene)
            sentiments = {'compound': 0.0, 'neg': 0.0, 'neu': 0.0, 'pos': 0.0}
            for sentence in scene_sentence:
                vs = analyzer.polarity_scores(sentence)
                sentiments['compound'] += vs['compound']
                sentiments['neg'] += vs['neg']
                sentiments['neu'] += vs['neu']
                sentiments['pos'] += vs['pos']
                
            sentiments['compound'] = sentiments['compound'] / float(len(scene_sentence))
            sentiments['neg'] = sentiments['neg'] / float(len(scene_sentence))
            sentiments['neu'] = sentiments['neu'] / float(len(scene_sentence))
            sentiments['pos'] = sentiments['pos'] / float(len(scene_sentence))
            dic = 'scene_' + str(x)
            sc_sent[dic] = sentiments
            
        #Extract the compound, negative, neutral and positive sentiments for each Scene
        sents = [sc_sent[keys] for keys in sc_sent]
        
        df_sentiment = pd.DataFrame(sents)
        df_zero = pd.DataFrame(0, df_sentiment.index, columns = ['Zero'])
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_sentiment.index, y=df_sentiment['compound'], mode='lines', name='Average Sentiment', 
                                 line=dict(color=colour)))
        
        fig.add_trace(go.Scatter(x=df_zero.index, y=df_zero['Zero'], mode='lines', name = 'Zero line', 
                                 line=dict(color='crimson', dash='dot')))
        
        fig.update_layout(title='<b> Sentiment across the ' + self.movie + ' Movie <b>', 
                          xaxis_title='<b> Scenes <b>', yaxis_title='<b> Average Sentiments <b>', showlegend=True)
        fig.show()
        
        return df_sentiment
    
    
    def film_emotional_arc(self):
        
        def cap_sentence(s):
            return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)
        
        df_contents = self.df_movie[['Scene_Names', 'Contents']]
        df_emotions = pd.read_csv('./emotions/NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt',
                                  names=["word", "emotion", "association"], sep='\t')
        df_emotion_word = df_emotions.pivot(index='word', columns='emotion', values='association').reset_index()
        emotions = df_emotion_word.columns.drop('word').tolist() ##Emotions annotated based on the NRC Sentiment Lexicons
        df_emo = pd.DataFrame(0, df_contents.index, columns = emotions)
        stemmer = SnowballStemmer("english")
        for x in range(0, len(df_contents), 1):
            scene_conts = re.sub(r"[^a-zA-Z0-9 ]+", '', df_contents.Contents[x])
            doc = word_tokenize(scene_conts)
            #print(doc, '\n\n')
            for word in doc:
                word = stemmer.stem(word.lower())
                emotion_score = df_emotion_word[df_emotion_word.word == word]
                if not emotion_score.empty:
                    for emotion in emotions:
                        df_emo.at[x, emotion] += emotion_score[emotion]
        
        #Concatenate contents and emotions for each context
        df_scene_emotions = pd.concat([df_contents, df_emo], axis=1)
        df_scene_emotions['word_count'] = df_scene_emotions['Contents'].apply(tokenize.word_tokenize).apply(len)
        for emotion in emotions:
            df_scene_emotions[emotion] = df_scene_emotions[emotion] / df_scene_emotions['word_count']
            
        fig = make_subplots(rows=5, cols=2, subplot_titles=(cap_sentence(emotions[0]), cap_sentence(emotions[1]), cap_sentence(emotions[2]),
                                                            cap_sentence(emotions[3]), cap_sentence(emotions[4]), cap_sentence(emotions[5]),
                                                            cap_sentence(emotions[6]), cap_sentence(emotions[7]),
                                                            cap_sentence(emotions[8]), cap_sentence(emotions[9])))
        
        row = 0
        count = 0
        for x in emotions:
            if count % 2:
                fig.add_trace(go.Scatter(x=df_scene_emotions.index, y=df_scene_emotions[x]), row = row, col = 2)
            else:
                row += 1
                fig.add_trace(go.Scatter(x=df_scene_emotions.index, y=df_scene_emotions[x]), row = row, col = 1)
            count += 1
            fig.update_xaxes(title_text= 'Scenes', dtick=20)
            fig.update_yaxes(title_text="Average Sentiment")
            
        # Edit the layout
        fig.update_layout(height=1500, width=1000, title_text="<b> Emotional arcs identified across the scenes in the " + self.movie + " movie <b>", showlegend=False)
        fig.show()
        
        return df_scene_emotions
    
    
    def emotional_arc_xter_plot(self, df, character):
        
        def cap_sentence(s):
            return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)
        
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
        
        
        ##Get the character dialogues per Scene
        df_cts, df_xt = xter_count_perscene(self.df_movie, character)
        
        ##Get the emotions
        df_emotions = pd.read_csv('./emotions/NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt', 
                                  names=["word", "emotion", "association"], sep='\t')
        
        df_emotion_word = df_emotions.pivot(index='word', columns='emotion', values='association').reset_index()
        emotions = df_emotion_word.columns.drop('word').tolist()
        df_emo = pd.DataFrame(0, df_xt.index, columns = emotions)
        stemmer = SnowballStemmer("english")
        df_xt['dialogues'] = df_xt.apply(lambda x : re.sub(r'[^a-zA-Z0-9 ]', '', str(x['dialogues'])).lower(),axis=1)
        for x in range(0, len(df_xt), 1):
            scene_contents = df_xt['dialogues'][x]
            doc = word_tokenize(scene_contents)
            #print(doc, '\n\n')
            for word in doc:
                word = stemmer.stem(word.lower())
                emotion_score = df_emotion_word[df_emotion_word.word == word]
                if not emotion_score.empty:
                    for emotion in emotions:
                        df_emo.at[x, emotion] += emotion_score[emotion]
        
        ##Concatenate the dialogue of the character and the emotions per scene
        df_xter_emotions = pd.concat([df_xt, df_emo], axis=1)
        df_xter_emotions['word_count'] = df_xter_emotions['dialogues'].apply(tokenize.word_tokenize).apply(len)
        for emotion in emotions:
            df_xter_emotions[emotion] = df_xter_emotions[emotion] / df['word_count']
            
        fig = make_subplots(rows=5, cols=2, subplot_titles=(cap_sentence(emotions[0]), cap_sentence(emotions[1]), cap_sentence(emotions[2]), 
                                                            cap_sentence(emotions[3]), cap_sentence(emotions[4]), cap_sentence(emotions[5]),
                                                            cap_sentence(emotions[6]), cap_sentence(emotions[7]),
                                                            cap_sentence(emotions[8]), cap_sentence(emotions[9])))
        
        row = 0
        count = 0
        for x in emotions:
            if count % 2:
                fig.add_trace(go.Scatter(x=df_xter_emotions.index, y=df_xter_emotions[x]), row = row, col = 2)
            else:
                row += 1
                fig.add_trace(go.Scatter(x=df_xter_emotions.index, y=df_xter_emotions[x]), row = row, col = 1)
            count += 1
            fig.update_xaxes(title_text= 'Scenes', dtick=20)
            fig.update_yaxes(title_text="Average Sentiment")
            
        # Edit the layout
        fig.update_layout(height=1500, width=1000, title_text="<b> Emotional arcs of " + character + " across the scenes in the " + self.movie + " movie <b>", showlegend=False)
        fig.show()
        
        return df_xter_emotions
    
    
    def emotional_content_plot(self, df, characters, num_of_characters):
        
        ##Capitalize each word
        def cap_sentence(s):
            return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)
        
        ##Extract Each Character's Dialogue
        xters_dialogue = {}
        
        for x in characters:
            xters_dialogue[x] = re.sub(r"[^a-zA-Z0-9 ]+", '', \
                                       str(df.loc[df.characters == x].Character_dialogue.values.tolist()))
            
        df_xters_dialogues = pd.DataFrame(xters_dialogue.items(), columns = ['characters', 'Contents'])
        
        ##Extract the Emotions
        df_emotions = pd.read_csv('./emotions/NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt',
                                  names=["word", "emotion", "association"], sep='\t')
        
        df_emotion_word = df_emotions.pivot(index='word', columns='emotion', values='association').reset_index()
        emotions = df_emotion_word.columns.drop('word').tolist()
        df_emo = pd.DataFrame(0, df_xters_dialogues.index, columns = emotions)
        stemmer = SnowballStemmer("english")
        
        for x in range(0, len(df_xters_dialogues), 1):
            scene_conts = re.sub(r"[^a-zA-Z0-9 ]+", '', df_xters_dialogues.Contents[x]).lower()
            doc = word_tokenize(scene_conts)
            #print(doc, '\n\n')
            for word in doc:
                word = stemmer.stem(word.lower())
                emotion_score = df_emotion_word[df_emotion_word.word == word]
                if not emotion_score.empty:
                    for emotion in emotions:
                        df_emo.at[x, emotion] += emotion_score[emotion]
                        
        df_scene_emotions = pd.concat([df_xters_dialogues, df_emo], axis=1)
        df_scene_emotions = df_scene_emotions.drop(['Contents'], axis = 1)
        df_scene_emotions = df_scene_emotions.T
        df_scene_emotions.columns = df_scene_emotions.iloc[0]
        df_scene_emotions.drop(df_scene_emotions.index[0], inplace = True)
        df_scene_emotions.reset_index(inplace = True)
        df_scene_emotions.rename(columns={'index': 'Emotions'}, inplace=True)
        df_scene_emotions['Emotions'] = df_scene_emotions['Emotions'].apply(cap_sentence)
        
        ##Number of characters emotional counts you want to display
        major_characters = df_scene_emotions.columns.tolist()[1:num_of_characters]
        
        fig = make_subplots(rows=5, cols=2, subplot_titles=(major_characters[0], major_characters[1], major_characters[2], major_characters[3],
                                                            major_characters[4], major_characters[5], 
                                                            major_characters[6], major_characters[7],
                                                            major_characters[8], major_characters[9]))
        
        row = 0
        count = 0
        colors = ['lightslategray', 'crimson', 'darkcyan', 'darkgoldenrod', 'cornsilk', 'turquoise', 'limegreen', \
                  'darkorchid', 'palevioletred', 'deeppink']
        
        for x in major_characters:
            if count % 2:
                fig.add_trace(go.Bar(x=df_scene_emotions['Emotions'], y=df_scene_emotions[x], marker_color=colors, name = x + ' Sentiment'),
                              row = row, col = 2)
            else:
                row += 1
                fig.add_trace(go.Bar(x=df_scene_emotions['Emotions'], y=df_scene_emotions[x], marker_color=colors, name = x + ' Sentiment'), 
                              row = row, col = 1)
            count += 1
            fig.update_yaxes(title_text="Sentiment counts")
            
        # Edit the layout
        fig.update_layout(height=1200, width=1000, 
                          title_text="<b> Emotional Sentiments of the 10 (Ten) Major Characters in the " + self.movie + " Movie <b>", showlegend= False)
        
        fig.show()
        
        return df_scene_emotions