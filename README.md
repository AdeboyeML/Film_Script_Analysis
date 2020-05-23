[//]: # (Image References)

[image1]: ./film_script_template.jpg "Sample Output"


# Film_Script_Analysis

The aim of this project is to provide detailed insights into different movies analyzed **focusing on the characters, their dialogues, scene locations, emotional and sentiment analysis of the whole movie and the individual characters, character's interaction with one another and finally gender distribution in the each of the movie analyzed.**

![Sample Output][image1]

## Highlights

- ***1000+ movie scripts were scraped from IMSDB Database and segmented into SCENE LOCATIONS/NAMES, SCENE ACTIONS, SCENE CHARACTERS AND SCENE DIALOGUES.

- ***20 Movies Script Visualizations (based on in-depth analysis) were done, these scripts were Randomly chosen from the 1000+ movie script I segmented to TEST the authenticity of the Movie Script Analytical Algorithm***

***- Highly recommended for visualization:***  The graphs/plots for the 20 Movie Scripts can be viewed using this link: 

- **[A Prayer Before Dawn ](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/A-Prayer-Before-Dawn_Movie_Analysis.ipynb),**

- **[Alien vs Predator](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Alien_vs_Predator_Movie_Analysis.ipynb),**

- **[American Pie](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/American-Pie_Movie_Analysis.ipynb),**

- **[Antz](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Antz_Movie_Analysis.ipynb),**

- **[Badlands](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Badlands_Movie_Analysis.ipynb),**

- **[Blue Velvet](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Blue_Velvet_Movie_Analysis.ipynb),**

- **[Bourne Identity](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Bourne_Identity_Movie_Analysis.ipynb),**

- **[Code of Silence](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Code_of_Silence_Movie_Analysis.ipynb),**

- **[Guardian of the galaxy Volume 2](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Guardian_of_the_galaxy_vol2_Movie_analysis.ipynb),**

- **[Indiana Jones IV](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Indiana_Jones_IV_Movie_Analysis.ipynb),**

- **[Inventing the Abbots](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Inventing_the_Abbots_Movie_Analysis.ipynb),**

- **[John Q](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/John_Q_Movie_Analysis.ipynb),**

- **[Little Athens](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Little_Athens_Movie_Analysis.ipynb),**

- **[Machine Gun Preacher](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Machine_Gun_Preacher_Movie_Analysis.ipynb),**

- **[Man on fire](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Man_on_fire_Movie_Analysis.ipynb),**

- **[Platoon](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Platoon_Movie_Analysis.ipynb),**

- **[Sleepy Hollow](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Sleepy_Hollow_Movie_Analysis.ipynb),**

- **[Social Network](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Social_Network_Movie_Analysis.ipynb),**

- **[Star wars (The Empire Strikes Back)](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Star-Wars-The-Empire-Strikes-Back_Movie_Analysis.ipynb),**

- **[Wild Wild West](https://nbviewer.jupyter.org/github/AdeboyeML/Film_Script_Analysis/blob/e2fec93a9fa163b49893788b46cecac29c51078a/Wild_Wild_West_Movie_Analysis.ipynb),**


This is because the plotly graphs cannot be viewed in github.



# To actualize this project, the following objectives were executed sequentially:

1. Web scraping of the movie scripts (Over 1000+ movies were scraped from IMSDB website)


2. Movies segmentation into Scenes --> **Scene Location, Scene Action/Description, Scene Dialogues, Scene Characters (All the movies scraped were segmented except those that do not follow the "Screenplay format i.e. INT / EXT)"**


3. Character extraction and appearances plot ---> Here, characters were plotted based on how many times they appeared and spoke in each scene and across the movie.


4. Character Interaction Mapping --> We mapped out the connection between all the characters in the movie and also the interaction between the Top 10 characters in the movie.


5. Here, we looked at the **Most mentioned character based on the Scene dialogues and also the characters each character mention the most in their conversation.**


6. Similar to Number 5., Here looked at who a specific character talks with the most in the Movie.


7. **Emotional and Sentiment Analysis across the whole movie and for each individual character**, However for this project we limited it to only the Top 10 characters. ---> This gives us the character's emotion when he/she appears in the movie.


8. Additional Scene Informations --> Exact Scene Locations, Scenes with dialogs and no dialogs, Scenes that occurred during the Day or in the Night, Scenes location based on Outdoor or Indoor appearances.


9. Gender Distribution in the movie.







***python modules for this project:***

`imsbd_moviescript_scraper_AND_Scene_Segmentation.py`,  -- scraped html text from IMSDB database and segmented Movie into scenes, 

`dialogue_appearance.py` --- dialogue appearances,

`characters_extract.py` --- extract characters and visualize the number of times they appeared,

`xter_interaction.py`   ---- visualize character intercation mapping,

`characters_mt.py`  --- character mentions, 

`emotions.py`  --- Emotional arcs and sentiment analysis on movie and the script,

`movie_info.py` --- Movie information e.g scene location, time of day ccurences for each scenes,

`gend_distribution_plot.py`  --- Gender distribution.






Tools: Python libraries: pandas, numpy, Regular expression (Regex)--> Regex the major Engine for text cleaning and Movie Scene Segmentation, plotly, nltk, seaborn, networkx
