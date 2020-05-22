Sentiment Composition Lexicon for Opposing Polarity Phrases (SCL-OPP)
Version 1.0
22 June 2016
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





Creators: Svetlana Kiritchenko and Saif M. Mohammad

Papers associated with this lexicon:

Svetlana Kiritchenko and Saif M. Mohammad (2016) Happy Accident: A Sentiment Composition Lexicon for Opposing Polarities Phrases. Proceedings of the 10th edition of the Language Resources and Evaluation Conference (LREC), Portorož, Slovenia, 2016.

Svetlana Kiritchenko and Saif M. Mohammad (2016) Sentiment Composition of Words with Opposing Polarities. Proceedings of the 15th Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL), San Diego, California, 2016.




***************************************
General Description
***************************************

Sentiment Composition Lexicon for Opposing Polarity Phrases (SCL-OPP) is a list of single words and multi-word phrases and their associations with positive and negative sentiment. The phrases consist of two or three words. Each phrase includes at least one positive word and at least one negative word. The single words are taken from the set of words that are part of multi-word phrases. The words and phrases are drawn from tweets, and therefore include a small number of hashtag words and creatively spelled words.

The sentiment associations were obtained manually through crowdsourcing using the Best-Worst Scaling annotation technique.


***************************************
SemEval-2016
***************************************

Parts of this lexicon were used as development and test sets for SemEval-2016 shared task on Determining Sentiment Intensity of English and Arabic Phrases (Task 7) -- English Twitter Mixed Polarity Set (http://alt.qcri.org/semeval2016/task7/). All terms from SCL-OPP except the ones that were used in the previous competition (SemEval-2015 Task 10 Subtask E) and in other datasets of SemEval-2016 Task 7 were included. The SemEval-2016 set additionally included some same polarity phrases. In total, there were 1,269 terms. The sentiment association scores were converted into the range 0..1 for the SemEval competition. 



***************************************
File Format
***************************************

Each line in the file has the following format:

<term><tab><sentiment score><tab><POS pattern><tab><term freq>

where
<term> is a single word or a multi-word phrase; 
<sentiment score> is a real number between -1 and 1 indicating the degree of association of the term with positive sentiment;
<POS pattern> is a corresponding sequence of parts of speech (POS); 
<term freq> is the frequency of the term in the corpus of 11 million tweets.

The POS tags were determined by looking up the most common part-of-speech sequence for that term in a tweet corpus. The corpus was automatically POS tagged using the CMU Tweet NLP tool (http://www.cs.cmu.edu/~ark/TweetNLP/). For POS abbreviation, please see 
Kevin Gimpel, Nathan Schneider, Brendan O’Connor, Dipanjan Das, Daniel Mills, Jacob Eisenstein, Michael Heilman, Dani Yogatama, Jeffrey Flanigan, and Noah A. Smith. 2011. Part-of-speech tagging for Twitter: Annotation, features, and experiments. In Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL).


There are 1,178 terms: 602 single words and 576 phrases.


***************************************
More Information
***************************************

Details on the process of creating the lexicon can be found in:

Svetlana Kiritchenko and Saif M. Mohammad (2016) Happy Accident: A Sentiment Composition Lexicon for Opposing Polarities Phrases. Proceedings of the 10th edition of the Language Resources and Evaluation Conference (LREC), Portorož, Slovenia, 2016.

Svetlana Kiritchenko and Saif M. Mohammad (2016) Sentiment Composition of Words with Opposing Polarities. Proceedings of the 15th Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL), San Diego, California, 2016.




