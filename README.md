# BiblePassageAnalyzer

How to use
 1) Open analyzer.py and edit it
    - change START, and END variables. This determines what passage is analyzed.
      - id is based off this pattern 01001001 [book,chapt,verse]
      - so genesis 1:1 is 01001001 and Rev 23:19 66023013
    - change NS to the number of polar sentences you want
    - change TW to the nunmber of top words you want
    - change VER to the desired versions
       - versions are web, asv, bbe, kjv, ylt
 2) Save analyzer.py
 3) Run analyzer.py
    - new folder named Results will be made with
        - results.txt
        - wordcloud.png
 
 
Point of this/Application

  This simple app analyzes a passage of the bible of your choosing. It can be useful for self study.
  
  A wordcloud.png will be created that can give you a new outlook on key words and themes.
  
  A results.txt will be created with the stats
      
      - total words
      - unique words
      - top words
         - the words 'the, of, and, is, but, for, as, that, it' etc are not included
      - number of sentences
      - Flesch–Kincaid readability score
      - Top/Bottom polarizing sentences from text
 
 This program can be good for analyzing chapters, books, several books, or the entirety of the bible.
 
 
 
 Things to fix, make better, or add
  
   - results.txt
       - add more results
           - top nouns, top verbs, top adj
   - Output more graphics in Results folder
   - Need to reformat code so program can run more smoothly
        - get UI
