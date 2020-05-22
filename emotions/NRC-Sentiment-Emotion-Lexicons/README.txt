NRC Sentiment and Emotion Lexicons 
April 2016
Copyright (C) 2016 National Research Council Canada (NRC)
----------------------------------------------------------------


Contact: 
-------------------------------------------------


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



Terms of Use: 
-------------------------------------------------

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



NRC Sentiment and Emotion Lexicons 
-----------------------------

The Sentiment and Emotion Lexicons is a collection of lexicons that was entirely created by the experts of the National Research Council of Canada. Developed with a wide range of applications, this lexicon collection can be used in a multitude of contexts such as sentiment analysis, product marketing, consumer behaviour and even political campaign analysis. 

The technology uses a list of words that help identify emotions, sentiment, as well as analyzing hashtags, emoticons and word-colour associations. The lexicons contain entries for English words, and can be used to analyze English texts. For some lexicons, also provided are  translations of the entries in other languages, including French, Arabic, Chinese, and Spanish.

Further details about each lexicon are available in the READMEs (provided within the folders associated with the lexicons) and in the associated papers listed in the READMEs. 


The Sentiment and Emotion Lexicons included in this distribution:
----------------------------------------------------------------

MANUALLY CREATED LEXICONS

- NRC Emotion Lexicon: association of words with eight emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) and two sentiments (negative and positive) manually annotated on Amazon's Mechanical Turk. Available in 105 different languages.
	Version: 0.92
	Number of terms: 14,182 unigrams (words), ~25,000 word senses
	Association scores: binary (associated or not)
	Creators: Saif M. Mohammad and Peter D. Turney

	Papers:

	Saif Mohammad and Peter Turney (2013). Crowdsourcing a Word-Emotion Association Lexicon. Computational Intelligence, 29 (3), 436-465, 2013.

	Saif Mohammad and Peter Turney (2010). Emotions Evoked by Common Words and Phrases: Using Mechanical Turk to Create an Emotion Lexicon, In Proceedings of the NAACL-HLT 2010 Workshop on Computational Approaches to Analysis and Generation of Emotion in Text, June 2010, LA, California.


- NRC Emotion Intensity Lexicon: association of words with eight basic emotions (anger, anticipation, disgust, fear, joy, sadness, surprise, and trust). The lexicon with its fine-grained real-valued scores was created by manual annotation using Best--Worst Scaling. Available in over 100 different languages.
	Version: 1.0
	Number of terms: ~10,000 unigrams (words)
	Association scores: real-valued
	Creator: Saif M. Mohammad

	Papers:

	Saif M. Mohammad (2018). Word Affect Intensities. In Proceedings of the 11th edition of the Language Resources and Evaluation Conference, May 2018, Miyazaki, Japan.


- NRC Valence, Arousal, and Dominance (VAD) Lexicon: a list of English words and their valence, arousal, and dominance scores. The lexicon with its fine-grained real-valued scores was created by manual annotation using Best--Worst Scaling. Available in 104 different languages.
	Version: 1.0
	Number of terms: 20,007 unigrams (words)
	Association scores: real-valued
	Creator: Saif M. Mohammad

	Papers:

	Saif M. Mohammad (2018). Obtaining Reliable Human Ratings of Valence, Arousal, and Dominance for 20,000 English Words. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, Melbourne, Australia, July 2018.


- NRC Word-Colour Association Lexicon: association of words with colours manually annotated on Amazon's Mechanical Turk.
	Version: 0.92
	Number of terms: 14,182 unigrams (words), ~25,000 word senses
	Association scores: binary (associated or not)
	Creator: Saif M. Mohammad

	Papers:

	Saif Mohammad (2011). Colourful Language: Measuring Word-Colour Associations. In Proceedings of the ACL 2011 Workshop on Cognitive Modeling and Computational Linguistics (CMCL), June 2011, Portland, OR.

	Saif Mohammad (2011). Even the Abstract have Colour: Consensus in Word-Colour Associations. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies, June 2011, Portland, OR.



SENTIMENT COMPOSITION LEXICONS

- Sentiment Composition Lexicon for Negators, Modals, and Degree Adverbs (SCL-NMA): a list of single words and multi-word phrases and their associations with positive and negative sentiment. The sentiment associations were obtained manually through crowdsourcing using the Best-Worst Scaling annotation technique.
	Version: 1.0
	Number of terms: 3,207 terms, including 1,621 single words and 1,586 phrases
	Association scores: real-valued
	Creators: Svetlana Kiritchenko and Saif M. Mohammad

	Papers:

	Svetlana Kiritchenko and Saif M. Mohammad (2016) The Effect of Negators, Modals, and Degree Adverbs on Sentiment Composition. Proceedings of the 7th Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (WASSA), San Diego, California, 2016.


- Sentiment Composition Lexicon for Opposing Polarity Phrases (SCL-OPP): a list of single words and multi-word phrases and their associations with positive and negative sentiment. The phrases consist of two or three words. Each phrase includes at least one positive word and at least one negative word. The sentiment associations were obtained manually through crowdsourcing using the Best-Worst Scaling annotation technique.
	Version: 1.0
	Number of terms: 1,178 terms, including 602 single words and 576 phrases
	Association scores: real-valued
	Creators: Svetlana Kiritchenko and Saif M. Mohammad

	Papers:

	Svetlana Kiritchenko and Saif M. Mohammad (2016) Happy Accident: A Sentiment Composition Lexicon for Opposing Polarities Phrases. Proceedings of the 10th edition of the Language Resources and Evaluation Conference (LREC), Portorož, Slovenia, 2016.

	Svetlana Kiritchenko and Saif M. Mohammad (2016) Sentiment Composition of Words with Opposing Polarities. Proceedings of the 15th Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL), San Diego, California, 2016.


- SemEval-2015 English Twitter Lexicon: a list of single words and simple two-word negated expressions and their associations with positive and negative sentiment. The terms are drawn from English Twitter and include general English words, misspellings, hashtags, and other categories frequently used in Twitter. The sentiment associations were obtained manually through crowdsourcing using the Best-Worst Scaling annotation technique.
	Version: 1.0
	Number of terms: 1,515 terms
	Association scores: real-valued
	Creators: Svetlana Kiritchenko and Saif M. Mohammad

	Papers:

	Svetlana Kiritchenko, Xiaodan Zhu and Saif Mohammad (2014). Sentiment Analysis of Short Informal Texts. Journal of Artificial Intelligence Research, volume 50, pages 723-762, August 2014.    


- SemEval-2016 Arabic Twitter Lexicon: a list of single words and simple two-word negated expressions and their associations with positive and negative sentiment. The terms are drawn from Arabic Twitter and include both standard and dialectal Arabic, Romanized words, misspellings, hashtags, and other categories frequently used in Twitter. The sentiment associations were obtained manually through crowdsourcing using the Best-Worst Scaling annotation technique.
	Version: 1.0
	Number of terms: 1,366 terms, including 1,168 single words and 198 phrases
	Association scores: real-valued
	Creators: Svetlana Kiritchenko, Saif M. Mohammad, and Mohammad Salameh
	Papers: 
	
	Svetlana Kiritchenko, Saif M. Mohammad and Mohammad Salameh (2016) SemEval-2016 Task 7: Determining Sentiment Intensity of English and Arabic Phrases. Proceedings of the International Workshop on Semantic Evaluation (SemEval-2016), San Diego, California, 2016.



AUTOMATICALLY GENERATED LEXICONS

- NRC Hashtag Emotion Lexicon: association of words with eight emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) generated automatically from tweets with emotion-word hashtags such as #happy and #anger. 
	Version: 0.2
	Number of terms: 16,862 unigrams (words)
	Association scores: real-valued
	Creator: Saif M. Mohammad

	Papers:

	Saif M. Mohammad and Svetlana Kiritchenko (2015). Using Hashtags to Capture Fine Emotion Categories from Tweets. Computational Intelligence, 31(2): 301-326, 2015.

	Saif Mohammad (2012). #Emotional Tweets. In Proceedings of the First Joint Conference on Lexical and Computational Semantics (*Sem), June 2012, Montreal, Canada.


- NRC Hashtag Sentiment Lexicon: association of words with positive (negative) sentiment generated automatically from tweets with sentiment-word hashtags such as #amazing and #terrible. 
	Version: 1.0
	Number of terms: 54,129 unigrams, 316,531 bigrams, 308,808 pairs
	Association scores: real-valued
	Creators: Saif M. Mohammad and Svetlana Kiritchenko


- NRC Hashtag Affirmative Context Sentiment Lexicon and NRC Hashtag Negated Context Sentiment Lexicon: association of words with positive (negative) sentiment in affirmative or negated contexts generated automatically from tweets with sentiment-word hashtags such as #amazing and #terrible. 
	Version: 1.0
	Number of terms: Affirmative contexts: 36,357 unigrams, 159,479 bigrams; Negated contexts: 7,592 unigrams, 23,875 bigrams
	Association scores: real-valued
	Creators: Svetlana Kiritchenko and Saif M. Mohammad


- NRC Emoticon Lexicon (a.k.a. Sentiment140 Lexicon): association of words with positive (negative) sentiment generated automatically from tweets with emoticons such as :) and :(. 
	Version: 1.0
	Number of terms: 62,468 unigrams, 677,698 bigrams, 480,010 pairs
	Association scores: real-valued
	Creators: Saif M. Mohammad and Svetlana Kiritchenko


- NRC Emoticon Affirmative Context Lexicon and NRC Emoticon  Negated Context Lexicon: association of words with positive (negative) sentiment in affirmative or negated contexts generated automatically from tweets with emoticons such as :) and :(.
	Version: 1.0
	Number of terms: Affirmative contexts: 45,255 unigrams, 240,076 bigrams; Negated contexts: 9,891 unigrams, 34,093 bigrams
	Association scores: real-valued
	Creators: Svetlana Kiritchenko and Saif M. Mohammad

	Papers for NRC Hashtag Sentiment and NRC Emoticon lexicons:

	Svetlana Kiritchenko, Xiaodan Zhu and Saif Mohammad (2014). Sentiment Analysis of Short Informal Texts. Journal of Artificial Intelligence Research, volume 50, pages 723-762, August 2014.    

	Saif M. Mohammad, Svetlana Kiritchenko, and Xiaodan Zhu (2013). NRC-Canada: Building the State-of-the-Art in Sentiment Analysis of Tweets. In Proceedings of the seventh International Workshop on Semantic Evaluation Exercises (SemEval-2013), June 2013, Atlanta, USA. 

	Xiaodan Zhu, Svetlana Kiritchenko, and Saif M. Mohammad (2014). NRC-Canada-2014: Recent Improvements in Sentiment Analysis of Tweets. In Proceedings of the eigth International Workshop on Semantic Evaluation Exercises (SemEval-2014), August 2014, Dublin, Ireland.    


