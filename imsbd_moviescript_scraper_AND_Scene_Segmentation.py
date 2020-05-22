
from collections import Counter

import glob
import os
import shutil
import random

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


from bs4 import  BeautifulSoup, SoupStrainer
import httplib2
import pprint
import re



#####Extract the film script URL LIst

http = httplib2.Http()
status, response = http.request('http://www.imsdb.com/all%20scripts/')
url_list = []
for link in BeautifulSoup(response, parse_only= SoupStrainer('a')):
    if link.has_attr('href'):
        url_in = link['href']
        if '/Movie Scripts/' in url_in:
            if link.has_attr('title'):
                url_in = link['title']
                url_in = url_in.replace(' ', '-')
                url_in = re.sub(r'\:', '', url_in)
                url_in = re.sub(r'-Script', '', url_in)
                url_in = 'http://www.imsdb.com/scripts/' + url_in + '.html'
                url_list.append(url_in)
                #print(url_in)
#len(url_list)



###Write the FILM SCRIPTS INTO TEXT FILES 

script_list =[]
http = httplib2.Http()
film_list= url_list
for index in range(len(film_list)):
    film_name  = film_list[index].strip('http://www.imsdb.com/scripts/')
    film_name = film_name.replace('.html','')
    film_name = film_name.replace(':', '')
    print(film_name)
    status, response = http.request(film_list[index])
    
    filename ='./imsdbfilmscripts/'+film_name+'.txt'
    for link in BeautifulSoup(response, parse_only= SoupStrainer('pre')):
        script_list = link.text
        with open(filename, "w", encoding='utf-8', errors='ignore') as f:
            for s in script_list:
                f.write(s)



##########----SEGMENTING THE FILM SCRIPTS INTO DIFFERENT SCENES SEGMENTS------#######
##########################################################################
############ EXTRACT OUT SCENES AND CHARACTERS ##########

def extract_scene_characters(filename):
    
    # read the data into a list (each row is one list element)
    with open(filename, "r", encoding='utf-8', errors='ignore') as f:
        data = [row for row in f]
    
    dat = []
    for x in data:
        x = re.sub(r'\(.*\)', '', x)
        x = re.sub(r'\-|\#\d+', '', x)
        #x = re.sub(r"[^a-zA-Z0-9.,?'\n ]+", '', x)
        x = re.sub(r"POINT OF VIEW", 'Point of view', x)
        x = re.sub(r"TEXT", 'Text', x)
        x = re.sub(r"NEXT", 'Next', x)
        dat.append(x.replace('\t', ' ').lstrip(" "))
    
    scenes = []
    for l in dat:
        match = re.search(r'(((INT\.|EXT\.)\s[A-Z]+.*)|((INT\.|EXT\.)\s+[A-Z]+.*)|((INT\.|EXT\.)\s[A-Z]+)|((INT\.|EXT\.)\s[0-9]+.*)|\
        ((INT\./EXT\.|EXT\./INT\.)\s[A-Z]+.*)|((INT\.|EXT\.)\s[0-9]+)|((INT\./EXT\.|EXT\./INT\.)\s[0-9]+.*)|(INT\.\s+.*|EXT\.\s+.*)\
        |((INT\.|EXT\.)\s[A-Z]+\W+.+)|((INT|EXT)\s[A-Z]+.*)|((INT|EXT)\s+[A-Z]+.*)|((INT|EXT)\s[A-Z]+)|((INT|EXT)\s[0-9]+.*)\
        |((INT/EXT|EXT/INT)\s[A-Z]+.*)|((INT|EXT)\s[0-9]+)|((INT/EXT|EXT/INT)\s[0-9]+.*)|((I/E\.|E/I\.)\s+[A-Z].*)\
        |((INT|EXT)\s[A-Z]+\W+.+)|((I/E\.|E/I\.)\s+.*))\n', l)
        if match:
            scenes.append(match.group(1))
    #scenes = [x.strip(" ") for x in scenes]
            
   
        
    characters = []
    for x in dat:
        xters = re.findall(r'(^[A-Z]+[A-Z]+\n)|(^[A-Z]+[A-Z]+\s+\n)|(^[A-Z]+\.\s+[A-Z]+\n)|(^[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\s\n)\
        |(^[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\n)|(^[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\n)|(^[A-Z]+[A-Z]+\'S\s+[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\n)\
        |(^[A-Z]+[A-Z]+\'S\s+[A-Z]+[A-Z]+\n)|(^[A-Z]+[A-Z]+\'S\s+[A-Z]+[A-Z]+\s+\n)|(^MR\s+[A-Z]+[A-Z]+|MRS\s+[A-Z]+[A-Z]+\n)\
        |(^[A-Z]+[A-Z]+\s+\&\s+[A-Z]+[A-Z]+\n)|(^MR\s+[A-Z]+[A-Z]+|MRS\s+[A-Z]+[A-Z]+\s+\n)', x)
        characters.append(xters)
        
    characters = [x for x in characters if x != []]
    refined_characters = []
    for c in characters:
        cc = [tuple(filter(None, i)) for i in c]
        refined_characters.append(cc)
    refined_xters = [x[0][0] for x in refined_characters]
    
    best_ = ['BEST DIRECTOR', 'BEST ADAPTED SCREENPLAY', 'BROADCASTING STATUS', 'BEST COSTUME DESIGN', 'TWENTIETH CENTURY FOX', 'BEST ORIGINAL SCORE', 'BEST ACTOR', 'BEST SUPPORTING ACTOR', 'BEST CINEMATOGRAPHY', 'BEST PRODUCTION DESIGN', 'BEST FILM EDITING', 'BEST SOUND MIXING', 'BEST SOUND EDITING', 'BEST VISUAL EFFECTS']
    transitions = ['RAPID CUT TO:', 'TITLE CARD', 'FINAL SHOOTING SCRIPT', 'CUT TO BLACK', 'CUT TO:', 'SUBTITLE:', 'SMASH TO:', 'BACK TO:', 'FADE OUT:', 'END', 'CUT BACK:', 'CUT BACK', 'DISSOLVE TO:', 'CONTINUED', 'RAPID CUT', 'RAPID CUT TO', 'FADE TO:', \
                   'FADE IN:', 'FADE OUT:', 'FADES TO BLACK', 'FADE TO', 'CUT TO', 'FADE TO BLACK', 'FADE UP:', 'BEAT', 'CONTINUED:', 'FADE IN', \
                   'TO:', 'CLOSE-UP','WIDE ANGLE', 'WIDE ON LANDING', 'THE END', 'FADE OUT','CONTINUED:', 'TITLE:', 'FADE IN','DISSOLVE TO','CUT-TO','CUT TO', 'CUT TO BLACK',\
                   'INTERCUT', 'INSERT','CLOSE UP', 'CLOSE', 'ON THE ROOF', 'BLACK', 'BACK IN SILENCE', 'TIMECUT', 'BACK TO SCENE',\
                   'REVISED', 'PERIOD', 'PROLOGUE', 'TITLE', 'SPLITSCREEN.', 'BLACK.',\
                   'FADE OUT', 'CUT HARD TO:', 'OMITTED', 'DISSOLVE', 'WIDE SHOT', 'NEW ANGLE']
    movie_characters = []
    for x in refined_xters:
        x = re.sub(r'INT\..*|EXT\..*', '', x)
        x = re.sub(r'ANGLE.*', '', x)
        trans = re.compile("({})+".format("|".join(re.escape(c) for c in transitions)))
        x = trans.sub(r'', x)
        best = re.compile("({})+".format("|".join(re.escape(c) for c in best_)))
        x = best.sub(r'', x)
        movie_characters.append(x.replace('\n', '').strip())
    movie_characters = [x.strip() for x in movie_characters if x]
    
    return scenes, movie_characters




#######################################################################
######## CLEAN THE FILM SCRIPT NOT THOROUGHLY THOUGH ##############

def clean_text(filename):
    """
    Applies some pre-processing on the given text.
    """
    with open(filename, "r", encoding='utf-8', errors='ignore') as r:
        text = [row for row in r]
        
    #REMOVE TRANSITIONS OR CAMERA ANGLES
    transitions = ['SMASH CUT TO:', 'FINAL SHOOTING SCRIPT', 'CUT TO BLACK', 'SMASH TO:', 'RAPID CUT TO:', 'BACK TO:', 'BLACK SCREEN', 'FADE OUT TO WHITE LIGHT', 'CUT TO:', 'CUT BACK:', 'CUT BACK', 'DISSOLVE TO:', 'CONTINUED', 'RAPID CUT', 'RAPID CUT TO', 'FADE TO:', \
                   'FADE IN:', 'FADES TO BLACK', 'FADE TO', 'CUT TO', 'FADE UP:', 'BEAT', 'AFTERNOON', 'EVENING', 'CONTINUED:', 'FADE IN', \
                   'TO:', 'CLOSE-UP','WIDE ANGLE','CONTINUED:', 'TITLE:', 'FADE IN','DISSOLVE TO','CUT-TO','CUT TO', 'CUT TO BLACK',\
                   'INTERCUT', 'INSERT', 'CLOSE UP', 'TITLE CARD', 'PAUSE', 'SOUND', 'SONG CONTINUES OVER', 'BACK TO SCENE',\
                   'CUT', 'WATCH', 'CU WATCH', 'BLACK', 'BACK IN SILENCE', 'SUBTITLE:', 'CLOSE', 'ON THE ROOF','CUT HARD TO:',\
                   'THE SCREEN', 'TITLE', 'PROLOGUE', 'SPLITSCREEN.', 'OMITTED', 'BLACK.',\
                   'FADE OUT:', 'FADE OUT.', 'FADE OUT', 'DISSOLVE', 'NEW ANGLE', 'WIDE SHOT']
    # remove directors or the film production company
    best_ = ['BEST DIRECTOR', 'BEST ADAPTED SCREENPLAY', 'SENTENCE', 'BROADCASTING STATUS', 'BEST COSTUME DESIGN', 'TWENTIETH CENTURY FOX', 'BEST ORIGINAL SCORE', 'BEST ACTOR', 'BEST SUPPORTING ACTOR', 'BEST CINEMATOGRAPHY', 'BEST PRODUCTION DESIGN', 'BEST FILM EDITING', 'BEST SOUND MIXING', 'BEST SOUND EDITING', 'BEST VISUAL EFFECTS']
    #text = re.sub('\d+', '', text)
    tex = []
    for x in text:
        tx = x.replace('\t', ' ').lstrip(" ")
        tx = re.sub(r'^\d+\n', r'', tx)
        tx = re.sub(r'\(.*\)', r'', tx)
        tx = re.sub(r'\#\d+', r'', tx)
        #tx = tx.replace('\n', '')
        #tx = re.sub(r'\d+', r'', tx)
        tx = re.sub(r'(((INT\.|EXT\.)\s[A-Z]+.*)|((INT\.|EXT\.)\s+[A-Z]+.*)|((INT\.|EXT\.)\s[A-Z]+)|((INT\.|EXT\.)\s[0-9]+.*)|\
        ((INT\./EXT\.|EXT\./INT\.)\s[A-Z]+.*)|((INT\.|EXT\.)\s[0-9]+)|((INT\./EXT\.|EXT\./INT\.)\s[0-9]+.*)|(INT\.\s+.*|EXT\.\s+.*)\
        |((INT\.|EXT\.)\s+[A-Z]+\W+.+)|((INT|EXT)\s+[A-Z]+.*)|((INT|EXT)\s+[A-Z]+.*)|((INT|EXT)\s[A-Z]+)|((INT|EXT)\s[0-9]+.*)|\
        ((INT/EXT|EXT/INT)\s+[A-Z]+.*)|((INT|EXT)\s+[0-9]+)|((INT/EXT|EXT/INT)\s+[0-9]+.*)|((I/E\.|E/I\.)\s+[A-Z].*)\
        |((INT|EXT)\s+[A-Z]+\W+.+)|((I/E\.|E/I\.)\s+.*))', 'SCC', tx)
        tx = re.sub(r'(^\d+\w+\.\s\n)|(^\d+\.\s\n)|(^\d+\.\n)', r'', tx)
        tx = re.sub(r'^\W+', r'', tx)
        tx = re.sub(r'^\d+\.', r'', tx)
        tx = re.sub(r'^\d+/\d+/\d+', r'', tx)
        tx = re.sub(r'ANGLE.*', '', tx)
        tx = re.sub(r'(\'m|\’m)', r' am', tx)
        tx = re.sub(r'(\'ll|\’l)', r' will', tx)
        tx = re.sub(r'(\'re|\’re)', r' are', tx)
        tx = re.sub(r'(\'d|\’d)', r' had', tx)
        tx = re.sub(r'(\'ve|\’ve)', r' have', tx)
        tx = re.sub(r'SEQ\.\s+\d+', r'', tx)
        #tx = re.sub(r'Final\s+\d+\.', r'', tx)
        tx = re.sub(r'Goldenrod\s+\-\s+\d+\.\d+\.\d+\s+\d+\.', r'', tx)
        tx = re.sub(r'(^\d+\s+\d+\s+\d+\s+\-\sRev\.\s\d+/\d+/\d+\s+\d+[A-Z])|(^\d+\s+\d+\s+\d+\s+\-\sRev\.\s\d+/\d+/\d+\s+\d+)', '', tx)
        tx = re.sub(r'([A-Z]+[A-Z]+\sREV\s\d+\-\d+\-\d+\s\d+\.)|([A-Z]+[A-Z]+\sREV\s\d+\-\d+\-\d+\s\d+[A-Z]\.)|(DBL\.\s[A-Z]+[A-Z]+\sREV\s\d+\-\d+\-\d+\s\d+\.)', '', tx)
        #tx = re.sub(r'^TITLE:\n', '', tx)
        #end = re.compile(r'THE END.*|FADE OUT.*', re.MULTILINE)
        #tx = end.sub(r'', tx)
        trans = re.compile("({})+".format("|".join(re.escape(c) for c in transitions)))
        tx = trans.sub(r'', tx)
        #tx = re.sub(r'[A-Z]+\'S', '', tx)
        #tx = tx.replace('[^a-zA-Z]', '')
        #tx = tx.replace('', '')
        #tx = tx.strip()
        #tx = re.sub(r'\d+', r'', tx)
        tx = re.sub(r"[^a-zA-Z0-9.,?'&\n ]+", '', tx)
        #tx = re.sub(r'\W+', ' ', tx)
        tex.append(tx)
    txt = "".join([s for s in tex if s.strip()])
    txt = re.sub(r'\nTHE END\n(.|\n)*', '', txt)
    
    return txt


######################################################################
######## EXTRACT CHARACTER'S DIALOGUE, SCENE CONTENT AND SCENE ACTION ################

def characters_dialogue_action(text, scenes, movie_characters):
    
    scene_action = []
    scene_xters = []
    scene_dialogue = []
    xters_list = []
    xters_dialogue = []
    
    scene_data = text.split('SCC')[1:]
    
#     scs = re.compile("({})+".format("|".join(re.escape(c) for c in scenes))).split(text)[1:]
#     scene_data = [x for x in scs if x not in scenes]

    
    for x in scene_data:
        scene_text = re.compile('(\n[A-Z]+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\s+\n)|(\n[A-Z]+\.\s+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\s+\n)\
        |(\n[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\n)|(\nMR\s+[A-Z]+[A-Z]+|MRS\s+[A-Z]+[A-Z]+\n)\
        |(\n[A-Z]+[A-Z]+\'S\s+[A-Z]+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\'S\s+[A-Z]+[A-Z]+\s+\n)|(\nMR\s+[A-Z]+[A-Z]+|MRS\s+[A-Z]+[A-Z]+\s+\n)\
        |(\n[A-Z]+[A-Z]+\s+\&\s+[A-Z]+[A-Z]+\n)').split(x)
        scene_text = [x for x in scene_text if x != None]
        xter_split = re.findall('(\n[A-Z]+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\s+\n)|(\n[A-Z]+\.\s+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\s+\n)\
        |(\n[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\'S\s+[A-Z]+[A-Z]+\s+[A-Z]+[A-Z]+\n)\
        |(\n[A-Z]+[A-Z]+\'S\s+[A-Z]+[A-Z]+\n)|(\n[A-Z]+[A-Z]+\'S\s+[A-Z]+[A-Z]+\s+\n)|(\nMR\s+[A-Z]+[A-Z]+|MRS\s+[A-Z]+[A-Z]+\s+\n)\
        |(\n[A-Z]+[A-Z]+\s+\&\s+[A-Z]+[A-Z]+\n)|(\nMR\s+[A-Z]+[A-Z]+|MRS\s+[A-Z]+[A-Z]+\n)', x)
        split_ = []
        for c in xter_split:
            cc = tuple(filter(None, c))
            split_.append(cc)
        xters_ = [x[0] for x in split_]
        sc_xters = []
        for r in xters_:
            tr = r.replace('\n', '').strip()
            if tr in movie_characters:
                sc_xters.append(r)
        if scene_text[0] not in sc_xters:
            scene_action.append(scene_text[0])
        else:
            scene_action.append(None)
        if len(sc_xters) >= 1:
            dialogue = []
            xhrs = []
            for z in range(0, len(scene_text),1):
                if scene_text[z] in sc_xters:
                    xters_list.append(scene_text[z])
                    xhrs.append(scene_text[z])
                    xters_dialogue.append(scene_text[z+1])
                    dialogue.append(scene_text[z+1])
                    xters_list = [re.sub(r'\n', r' ', y).strip() for y in xters_list]
                    xhrs = [re.sub(r'\n', r' ', y).strip() for y in xhrs]
                    xters_dialogue = [re.sub(r'\n', r' ', y) for y in xters_dialogue]
                    dialogue = [re.sub(r'\n', r' ', y) for y in dialogue]
            scene_dialogue.append(dialogue)
            scene_xters.append(xhrs)
        else:
            scene_dialogue.append(None)
            scene_xters.append(None)
    
    scene_data = [re.sub(r'\n', r' ', x) for x in scene_data]
    scene_action = [re.sub(r'\n', r' ', x).strip() for x in scene_action]
        
    data_tuples = list(zip(scenes, scene_action, scene_xters, scene_dialogue, scene_data))
    df_scene = pd.DataFrame(data_tuples, columns=['Scene_Names','Scene_action', 'Scene_Characters', 'Scene_Dialogue', 'Contents'])
    
    data_tuples2 = list(zip(xters_list, xters_dialogue))
    df_dialogue = pd.DataFrame(data_tuples2, columns=['characters','Character_dialogue'])
    df_xters = pd.DataFrame(movie_characters, columns = ['characters'])
    
    return df_scene, df_xters, df_dialogue




###################################################################
##### STORE THE SEGMENTED RESULTS INTO .PKL ######

films = []
dest = 'Films_not_analyzed/'
for f in glob.glob('./imsdbfilmscripts\*'):  
    film_name = re.sub(r'.txt|\./imsdbfilmscripts\\', '', f)
    films.append(film_name)
    sc, movie_xters = extract_scene_characters(f)
    if len(sc) > 1:
        sc_text = clean_text(f)
        df_sc, df_xtrs, df_dia = characters_dialogue_action(sc_text, sc, movie_xters)
        df_sc.to_pickle('Films/' + film_name + '.pkl')
        df_xtrs.to_pickle('Characters/' + film_name + '.pkl')
        df_dia.to_pickle('Dialogues/' + film_name + '.pkl')
        print(film_name + ' IS GOING TO BE ANALYZED \n')
    else:
        shutil.copy(f, dest)
        print(film_name + ' IS NOT GOING TO BE ANALYZED \n')