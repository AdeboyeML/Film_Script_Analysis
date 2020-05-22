SemEval-2016 Arabic Twitter Lexicon
Version 1.0
12 April 2016
Copyright (C) 2016 National Research Council Canada (NRC)


************************************************************
Contact: 
************************************************************


Technical enquiries

Saif M. Mohammad (Senior Research Officer at NRC and creator of these lexicons)
Saif.Mohammad@nrc-cnrc.gc.ca 

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





Creators: Svetlana Kiritchenko, Saif M. Mohammad, and Mohammad Salameh

Paper associated with this lexicon:

Svetlana Kiritchenko, Saif M. Mohammad and Mohammad Salameh (2016) SemEval-2016 Task 7: Determining Sentiment Intensity of English and Arabic Phrases. Proceedings of the International Workshop on Semantic Evaluation (SemEval-2016), San Diego, California, 2016.



***************************************
General Description
***************************************

SemEval-2016 Arabic Twitter Lexicon is a list of single words and simple two-word negated expressions and their associations with positive and negative sentiment. The terms are drawn from Arabic Twitter and include both standard and dialectal Arabic, Romanized words, misspellings, hashtags, and other categories frequently used in Twitter. The negated expressions are in the form of 'negator w', where 'negator' is a negation trigger from a list of 16 common Arabic negation words. The complete list of the negation triggers is included into this distribution.

The sentiment associations were obtained manually through crowdsourcing using the Best-Worst Scaling annotation technique.


***************************************
SemEval-2016
***************************************

This lexicon was used in SemEval-2016 shared task on Determining Sentiment Intensity of English and Arabic Phrases (Task 7) -- Arabic Twitter Set (http://alt.qcri.org/semeval2016/task7/). The sentiment association scores were converted into the range 0..1 for the SemEval competition. 



***************************************
File Format
***************************************

The file is in UTF8 encoding. Each line in the file has the following format:

<sentiment score><tab><term>

where
<sentiment score> is a real number between -1 and 1 indicating the degree of association of the term with positive sentiment;
<term> is a single word or a multi-word phrase.

There are 1,366 terms: 1,168 single words and 198 phrases.


***************************************
More Information
***************************************

Details on the process of creating the lexicon can be found in:

Svetlana Kiritchenko, Saif M. Mohammad and Mohammad Salameh (2016) SemEval-2016 Task 7: Determining Sentiment Intensity of English and Arabic Phrases. Proceedings of the International Workshop on Semantic Evaluation (SemEval-2016), San Diego, California, 2016.




