import cufflinks as cf
from collections import Counter


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



class scene_info_plots:
    
    def __init__(self, df_movie, moviename):

        self.df_movie = df_movie
        self.movie = moviename
        
    def extract_scene_locations(self):
        
        sc_times = ['THE Next AFTERNOON', 'THE Next NIGHT', 'THE Next EVENING', 'CONTINUOUS ACTION DAY', '(WEEKS LATER)', \
                    '(WEEKS LATER', 'A LITTLE LATER', 'LATER THAT MORNING', 'SHORT TIME LATER', \
                    'EARLY MORNING', 'TIMELESS', 'PREDAWN', 'PREDUSK'\
                    'LATER THAT AFTERNOON', 'LATER THAT NIGHT', 'WEEKS LATER', 'CONTINOUS ACTION', 'ACTION DAY', 'A SHORT TIME LATER' \
                    'LATER THAT DAY', 'LATER THAT EVENING', 'DAYS LATER', 'NIGHT LATER' 'THAT DAY', 'THAT NIGHT', 'THE Next MORNING', \
                    'MOMENTS LATER', 'MINUTES LATER', 'Next AFTERNOON', 'Next MORNING', 'Next EVENING', 'CONTINUOUS ACTION DAY' \
                    'SECONDS LATER', 'LATER THAT DAY', 'LATER THAT NIGHT', 'LATE NIGHT', 'EARLY DAY', 'SAME TIME', 'SAME DAY', \
                    'SAME NIGHT', 'MOVING', 'CONTINUOUS', 'SAME', 'EVENING', 'Next DAY', 'Next NIGHT', 'THE Next DAY', 'THE NEXT DAY', \
                    'MORNING', 'SUNSET', 'SUNRISE', 'DAWN', 'LATER', 'DUSK', 'AFTERNOON', 'ESTABLISHING', \
                    'TIME', 'DAYS', 'NIGHTS', 'DAY', 'NIGHT', 'EXT./INT.', 'INT./EXT.', 'INT/EXT', 'EXT/INT', 'INT.', 'EXT.', \
                    'INT', 'EXT', 'I/E.', 'E/I.', 'MOMENTS', 'THAT', 'Next', '(LATE)', '(LATE', 'SHORT', 'ACTION', 'EARLY']
        
        scene_locations = []
        
        for x in self.df_movie.Scene_Names:
            loc = re.compile("({})+".format("|".join(re.escape(c) for c in sc_times)))
            tx = loc.sub(r'', x)
            tx = re.sub(r'\d+|\w+\d+', '', tx)
            scene_locations.append(tx.strip())
            locs_ct = dict(Counter(scene_locations).most_common())
            
        df_scene_locations = pd.DataFrame(locs_ct.items(), columns = ['Scene Locations', 'Scene counts']).sort_values(by = 'Scene counts')
        
        fig = px.bar(df_scene_locations, x= 'Scene counts', y= 'Scene Locations', orientation = 'h',
                     hover_data=df_scene_locations.columns, color='Scene counts', 
                     labels={'Scene counts':'<b> Scene Counts <b>'}, width=1000, height= 2000, 
                     color_continuous_scale=px.colors.cyclical.HSV)
        
        fig.update_layout(title='<b> Scene Locations in the ' + self.movie + ' Movie & Number of times they appeared <b>', xaxis_title='<b> Scene appearance <b>', 
                          yaxis_title='<b> Locations <b>')
        
        iplot(fig)
        
    def pie_plots(self):
        
        sc_loc = ['INT', 'EXT']
        sc_day_night = ['DAY', 'NIGHT']
        
        def extract_scene_extras(df, sc_xtra):
            scene_extras = []
            sc_extras = []
            for x in df.Scene_Names:
                x = re.sub(r'\.', '', x)
                loc = re.compile("({})+".format("|".join(re.escape(c) for c in sc_xtra)))
                tx = loc.findall(x)
                if tx:
                    scene_extras.append(tx)
                else:
                    scene_extras.append('Not Indicated')
            for x in scene_extras:
                if type(x) == list:
                    for y in x:
                        sc_extras.append(y)
                else:
                    sc_extras.append(x)
            sc_locs_ct = dict(Counter(sc_extras).most_common())
            df_extras = pd.DataFrame(sc_locs_ct.items(), columns = ['Scene Categories', 'size'])
            return df_extras
        
        scene_locs = extract_scene_extras(self.df_movie, sc_loc)
        scenes_day_night = extract_scene_extras(self.df_movie, sc_day_night)
        
        ##Plot the Scenes locs (INT & EXT)
        fig = px.pie(scene_locs, values='size', names='Scene Categories', title='Percent of Indoor (INT) and Outdoor (EXT) Scene locations in ' + self.movie + ' Movie',
                     hover_data=scene_locs.columns, color_discrete_sequence=px.colors.sequential.Plasma)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.show()
        
        ###Plot the Time of Occurences
        fig = px.pie(scenes_day_night, values='size', names='Scene Categories', title='Scenes by Time of Day Occurences in ' + self.movie + ' Movie',
                     hover_data=scene_locs.columns, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.show()
        
        ##Plot Dialogs percent in the movie
        def plot_scene_dialog(df, filmname):
            sc_dialog = []
            for x in df.Scene_Dialogue:
                if x:
                    sc_dialog.append('Scenes with Dialog')
                else:
                    sc_dialog.append('Scene without Dialog')
            sc_dialog_ct = dict(Counter(sc_dialog).most_common())
            df_dialog = pd.DataFrame(sc_dialog_ct.items(), columns = ['Dialogues', 'size'])
            fig = px.pie(df_dialog, values='size', names='Dialogues', title='Percent of scenes with or without Dialogues in ' + filmname + ' Movie', 
                         hover_data=df_dialog.columns, color_discrete_sequence=px.colors.sequential.Hot)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.show()
            
        plot_scene_dialog(self.df_movie, self.movie)