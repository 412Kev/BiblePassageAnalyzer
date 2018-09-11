import csv
from Passage import *
from textblob import TextBlob
import operator
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
import os

# 01001001 --> Start Gen 1:1
# 66023013 --> End Rev 23:19
	# 18 -> Wisdom
	# 23 -> Prophets
	# 40 -> Gospels
	# 45 -> Pauline Epistles
	# 58 -> General Epistles

START = 1001001
END   = 6001001

# Create passage
mypassageASV = Passage(START, END, 'web')

# Main objects
text = mypassageASV.text
blob = TextBlob(text)
words = blob.word_counts
sentences = blob.sentences
tags = blob.tags

# Count Words
unique = len(words)
total = 0
for v in words.values():
	total += v

# *****THIS METHOD CAN BE GREATLY IMPROVED*****
def getSyllables(words):
	syllables = 0
	V = ['a','e','i','o','u','y']
	for w in words:
		s = 0
		word = w
		k = words[w]
		vowels = sum([1 for i in word if i in V])
		s += vowels
		if word.endswith('e'):
			s = s - 1
		if 'au' in word:
			s = s - 1
		if 'oy' in word:
			s = s - 1		
		if 'iou' in word:
			s = s - 1
		syllables += (s*k)
	return syllables

syllables = getSyllables(words)

#----------- Get Polarizing Sentences and Sentence count
num_sentences = len(sentences)

# Sort Sentences by polarity
def Key1(item):
	return item.polarity
sentences = sorted(sentences, key=Key1)

# Get top 3 polar and bottom 3 polar
bottom_polar = sentences[0:3]
top_polar = sentences[(num_sentences - 3):num_sentences]

# Remove any that have score of 0.0
for i in range(3):
	if top_polar[i].polarity == 0.0 :
		top_polar[i] = ''
	if bottom_polar[i].polarity == 0.0 :
		bottom_polar[i] = ''

#-------------- Get Top Words
# Is this sort n^2 
# Is there simplier way to sort
words = sorted(words.items(), key=lambda x: x[1])
words = [ i for i in words if (i[0] != 'the' and i[0] != 'of' and i[0] != 'and' 
	and i[0] != 'is' and i[0] != 'but' and i[0] != 'for' and i[0] != 'a' and 
i[0] != 'are' and i[0] != 'by' and i[0] != 'to' and i[0] != 'that' and i[0] != 'in' 
and i[0] != 'who' and i[0] != 'be' and i[0] != 'as' and i[0] != 'it' and i[0] != 'ye'
and i[0] != 'which' and i[0] != 'was' and i[0] != 'unto' and i[0] != 'will' and i[0] != 'has'
and i[0] != 'his' and i[0] != 'him' and i[0] != 'on')]


plt.figure(figsize=(20,10))
wordcloud = WordCloud(background_color = 'white', mode = 'RGB', width = 2000, height = 1000).generate(text)
plt.title("Bible WordCloud")
plt.imshow(wordcloud)
plt.axis("off")

top10 = []
for i in range(10):
	top10.append(words.pop())

FK_score = 206.835 - 1.015*(total/len(sentences)) - 84.6*(syllables/total)

os.makedirs('./Results/')
os.chdir('Results')

f = open("results.txt", "w")
f.write("--- Results of Passage Analysis ---")
f.write('\n')
f.write('\nTop words :')
n = 1
for word in top10:
	sen = '\n' + str(n) + ')   ' + str(word[0]) + '        ' + str(word[1])
	f.write(sen)
	n += 1
f.write('\n')
f.write('\n')


f.write('Stats :')
f.write('\n     total words:  ' + str(total))
f.write('\n     unique words:  ' + str(unique))
f.write('\n     Readability Score:  ' + str(FK_score))
f.write('\n     [0 -> college level, 100 -> basic]')
f.write('\n     Total sentences: ' + str(len(sentences)))


f.write('\n\nPolarizing Sentences :')
f.write('\nTop Polar')
for sent in top_polar:
	x = '\n     ' + str(sent)
	f.write('\n' + str(sent.polarity))
	f.write(x)


f.write('\n\n\nBottom Polar')
for sent in bottom_polar:
	x = '\n     ' + str(sent)
	f.write('\n' + str(sent.polarity))
	f.write(x)

plt.savefig('wordcloud.png')



