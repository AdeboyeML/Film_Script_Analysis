NRC Valence, Arousal, and Dominance (VAD) Lexicon 
Version 1.0
30 August 2018
Copyright (C) 2018 National Research Council Canada (NRC)
************************************************************


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





Creator: Saif M. Mohammad

Paper associated with this lexicon:

Obtaining Reliable Human Ratings of Valence, Arousal, and Dominance for 20,000 English Words.
Saif M. Mohammad. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, Melbourne, Australia, July 2018.



************************************************************
GENERAL DESCRIPTION
************************************************************

Words play a central role in language and thought. Several influential factor analysis studies have shown that
the primary dimensions of word meaning are valence, arousal, and dominance (VAD). 
- valence is the positive--negative or pleasure--displeasure dimension; 
- arousal is the excited--calm or active--passive dimension; and 
- dominance is the powerful--weak or 'have control'--'have no control' dimension.

The NRC Valence, Arousal, and Dominance (VAD) Lexicon includes a list of more than 20,000 English words and
their valence, arousal, and dominance scores.  For a given word and a dimension (V/A/D), the scores range from
0 (lowest V/A/D) to 1 (highest V/A/D).  The lexicon with its fine-grained real-valued scores was created by
manual annotation using best--worst scaling.  The lexicon is markedly larger than any of the existing VAD
lexicons. We also show that the ratings obtained are substantially more reliable than those in existing
lexicons. (See associated paper for details.)

Despite some cultural differences, it has been shown that a majority of affective norms are stable across
languages. Thus we provide versions of the VAD lexicon in over one hundred languages by translating the
English terms using Google Translate (July 2018).

Applications: The NRC VAD Lexicon has a broad range of applications in Computational Linguistics, Psychology,
Digital Humanities, Computational Social Sciences, and beyond. Notably it can be used to:
- study how people use words to convey emotions.
- study how different genders and personality traits impact how we view the world around us.
- study how emotions are conveyed through literature, stories, and characters.
- obtain features for machine learning systems in sentiment, emotion, and other affect-related tasks and 
  to create emotion-aware word embeddings and emotion-aware sentence representations.
- evaluate automatic methods of determining V, A, and D (using NRC VAD entries as gold/reference scores).
- study the interplay between the basic emotion model and the VAD model of emotions.
- study the role of high VAD words in high emotion intensity sentences, tweets, snippets from literature.

An Interactive Visualization of the NRC VAD Lexicon is available here: 
http://saifmohammad.com/WebPages/nrc-vad.html#Viz

Companion lexicons -- the NRC Emotion Lexicon and the NRC Emotion Intensity Lexicon are available here:
http://saifmohammad.com/WebPages/lexicons.html

This study was approved by the NRC Research Ethics Board (NRC-REB) under protocol number 2017-98. REB review
seeks to ensure that research projects involving humans as participants meet Canadian standards of ethics.



************************************************************
FILE FORMAT
************************************************************

1. NRC-VAD-Lexicon.txt: This is the main lexicon file with entries for 20,0007 English words. It has four columns
(separated by tabs):
- Word: The English word for which V, A, and D scores are provided. The words are listed in alphabetic order.
- Valence: valence score of the word
- Arousal: arousal score of the word
- Dominance: dominance score of the word

2. The directory 'OneFilePerDimension' has the same information as in NRC-VAD-Lexicon.txt, but in multiple files
-- one for each dimension: 
- v-scores: Includes valence scores. The words are sorted in decreasing order of valence.
- a-scores: Includes arousal scores. The words are sorted in decreasing order of arousal.
- d-scores: Includes dominance scores. The words are sorted in decreasing order of dominance.

3. NRC-VAD-Lexicon-ForVariousLanguages.txt: This files has the same first four columns as the NRC-VAD-Lexicon.txt.  
Additionally, it has columns pertaining to over 100 languages. Each of these columns
lists the translations of the English words into the corresponding language. For example, the column
Japanese-ja contains the Japanese translations of the English words. ('ja' is the ISO-639-1 Code for
Japanese.) The translations were obtained using Google Translate in July 2018. Occasionally, Google Translate
fails to provide a translation. In such cases, the file shows "NO TRANSLATION" instead of the translation.

4. The directory 'OneFilePerLanguage' has the same information as in NRC-VAD-Lexicon-ForVariousLanguages.txt,
but in multiple files -- one for each language.  Each of these files has five columns. The first column is for
the English words. The second column is the translation of the English words to a different language -- the
language corresponding to the file name. The third, fourth, and fifth columns are for valence, arousal, and
dominance scores.  So if one is interested only in the Japanese version of the NRC VAD Lexicon, then they can
simply use Japanese-ja-NRC-VAD-Lexicon.txt.

5. VAD-ACL2018.pdf: The research paper describing the NRC VAD Lexicon.

You can view the lexicon files using most text editors, Microsoft Excel, etc. You might have to make sure that
the viewer supports characters from various languages, i.e., set the encoding option in the viewer to UTF-8, etc.
For example, to view in excel, follow these steps:
- open excel
- click on File -> Import
- select file type as 'Text file' 
- select the lexicon file to import in the dialog box that opens up
- select 'File Origin' type as 'Unicode (UTF-8)'
- click 'Finish'

Paper_NRC_VAD_Lexicon.pdf will require a suitable pdf reader such as Acrobat or Preview.


************************************************************
More Information
************************************************************

Details of the NRC VAD Lexicon are available in this paper:

Obtaining Reliable Human Ratings of Valence, Arousal, and Dominance for 20,000 English Words.  Saif M.
Mohammad. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics,
Melbourne, Australia, July 2018.

Please cite the paper if you use it or when referring to the lexicon. A copy of the paper is included in this 
package (Paper_NRC_VAD_Lexicon.pdf).
 
