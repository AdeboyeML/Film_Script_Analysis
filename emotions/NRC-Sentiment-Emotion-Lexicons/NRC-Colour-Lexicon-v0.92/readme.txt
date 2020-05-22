NRC Word-Colour Association Lexicon (NRC Colour Lexicon)
Version 0.92
21 July 2011
Copyright (C) 2011 National Research Council Canada (NRC)
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

Saif M. Mohammad. Colourful Language: Measuring Word-Colour Associations. In Proceedings of the ACL 2011 Workshop on Cognitive Modeling and Computational Linguistics (CMCL), June 2011, Portland, OR.

Saif M. Mohammad. Even the Abstract have Colour: Consensus in Word-Colour Associations. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies, June 2011, Portland, OR.



************************************************************
GENERAL DESCRIPTION
************************************************************

Many real-world concepts have associations with colours. For example, iceberg is associated with white, vegetation with green, danger with red, and so on. The NRC word-colour association lexicon is a list of
words and the colours they are most associated with. The annotations were manually done through Amazon's Mechanical Turk. 



************************************************************
FILE FORMAT
************************************************************

Each line has the following format:
<TargetWord>--<sense><tab>Colour=<colour><tab>VotesForThisColour=<VotesForThisColour><tab>TotalVotesCast=<TotalVotesCast>

<TargetWord> is a word for which the annotators provided colour associations;

<sense> is one or more comma-separated words that indicate the sense of the target word for which the annotations are provided;

<colour> is the colour most associated with the target word. It is one of eleven colours---white, black, red, green, yellow, blue, brown, pink, purple, orange, grey. If each of the annotators suggested a different colour association for the target word, then <colour> is set to None.

<VotesForThisColour> is the number of annotators who chose <colour> for the target word. It is set to None if <colour> is None.

<TotalVotesCast> is the total number of annotators who gave colour associations for the target word.


************************************************************
VERSION INFORMATION
************************************************************

Version 0.92 is the latest version as of 21 July 2011. 


************************************************************
More Information
************************************************************

Details on the process of creating the lexicon can be found in the associated papers (see above).
 

