NRC Hashtag Emotion Lexicon
Version 0.2
4 November 2013
Copyright (C) 2013 National Research Council Canada (NRC)
************************************************************


************************************************************
Contact: 
************************************************************


Technical enquiries

Saif M. Mohammad (Senior Research Officer at NRC and creator of these lexicons)Saif.Mohammad@nrc-cnrc.gc.ca 

Business enquiries

Pierre Charron (Client Relationship Leader at NRC)
Pierre.Charron@nrc-cnrc.gc.ca



Information on various lexicons is available here:
http://saifmohammad.com/WebPages/lexicons.html

You may also be interested in some of the other resources and work we have done on the analysis of emotions in text:
http://saifmohammad.com/WebPages/ResearchAreas.html
http://saifmohammad.com/WebPages/ResearchInterests.html#EmotionAnalysis



************************************************************
Terms of Use: 
************************************************************

1. The lexicons mentioned in this page can be used freely for non-commercial research and educational purposes.

2. Cite the papers associated with the lexicons in your research papers and articles that make use of them. (The papers associated with each lexicon are listed below, and also in the READMEs for individual lexicons.) 

3. In news articles and online posts on work using these lexicons, cite the appropriate lexicons. For example:
"This application/product/tool makes use of the <resource name>, created by <author(s)> at the National Research Council Canada." (The creators of each lexicon are listed below. Also, if you send us an email, we will be thrilled to know about how you have used the lexicon.) If possible hyperlink to this page: http://saifmohammad.com/WebPages/lexicons.html

4. If you use a lexicon in a product or application, then acknowledge this in the 'About' page and other relevant documentation of the application by stating the name of the resource, the authors, and NRC. For example:
"This application/product/tool makes use of the <resource name>, created by <author(s)> at the National Research Council Canada." (The creators of each lexicon are listed below. Also, if you send us an email, we will be thrilled to know about how you have used the lexicon.) If possible hyperlink to this page: http://saifmohammad.com/WebPages/lexicons.html

5. Do not redistribute the data. Direct interested parties to this page: http://saifmohammad.com/WebPages/AccessResource.htm

6. If interested in commercial use of any of these lexicons, see information here: https://shop-magasin.nrc-cnrc.gc.ca/nrcb2c/app/displayApp/(cpgnum=1&layout=7.01-7_1_71_63_73_6_9_3&uiarea=3&carea=0000000104&cpgsize=0)/.do?rf=y.

7. National Research Council Canada (NRC) disclaims any responsibility for the use of the lexicons listed here and does not provide technical support. However, the contact listed above will be happy to respond to queries and clarifications.



We will be happy to hear from you, especially if:
- you give us feedback regarding these lexicons;
- you tell us how you have (or plan to) use the lexicons;
- you are interested in having us analyze your data for sentiment, emotion, and other affectual information;
- you are interested in a collaborative research project. We also regularly hire graduate students for research internships.





Creator: Saif M. Mohammad

Papers associated with this lexicon:

Saif M. Mohammad and Svetlana Kiritchenko. Using Hashtags to Capture Fine Emotion Categories from Tweets. 
Computational Intelligence, 31(2): 301-326, 2015.

Saif M. Mohammad. #Emotional Tweets. In Proceedings of the First Joint Conference on Lexical and Computational Semantics (*Sem), June 2012, Montreal, Canada. 




************************************************************
GENERAL DESCRIPTION
************************************************************

The NRC Hashtag Emotion Lexicon is a list of words and their associations with eight emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust). The associations were computed from tweets with emotion-word hashtags such as #happy and #anger. 

The NRC Hashtag Emotion Lexicon is different from the NRC Emotion Lexicon. The Hashtag lexicon was automatically generated from tweets using emotion word hashtags. The NRC Emotion Lexicon was created by crowdsourcing and direct human annotation. 


************************************************************
DATA SOURCE
************************************************************

The NRC Hashtag Emotion Lexicon is automatically generated from the following data source: 
tweets with emotion-word hashtags collected by NRC.


************************************************************
FILE FORMAT
************************************************************

Each line has the following format:
<AffectCategory><tab><term><tab><score>

<AffectCategory> is one of eight emotions (anger, fear, anticipation, trust, surprise, sadness, joy, or disgust).

<term> is a word for which emotion associations are provided.

<score> is a value that indicates the strength of association between the <term> and the <AffectCategory>. The higher the value, the stronger is the association. Refer to the publications below for details on how the score is calculated.


************************************************************
VERSION INFORMATION
************************************************************

Version 0.2 is the latest version as of 4 November 2013. Version 0.1 was created using eight hashtags (pertaining to the eight basic emotions). Version 0.2 was created using 72 hashtags (these include the eight used in version 0.1 as well as their synonyms.) The publications mentioned below describe the creation and use of version 0.1. The use of version 0.2 in the same experiments further improves results.


************************************************************
More Information
************************************************************

Details on the process of creating the lexicon can be found in the associated papers (see above).

 
