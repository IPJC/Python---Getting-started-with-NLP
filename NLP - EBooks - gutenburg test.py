#From https://www.nltk.org/book/ch03.html

import nltk, re, pprint
import nltk
nltk.download('punkt') #needed to specifically download this project
nltk.download('stopwords') #needed to specifically download this project
from nltk import word_tokenize,sent_tokenize
from urllib import request
#3.1
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
type(raw) #<class 'str'>
len(raw)  #1176893
raw[:75] #'The Project Gutenberg EBook of Crime and Punishment, by Fyodor Dostoevsky\r\n'

tokens = word_tokenize(raw)
type(tokens) #<class 'list'>
len(tokens) #254354
first_ten = tokens[:10] #['The', 'Project', 'Gutenberg', 'EBook', 'of', 'Crime', 'and', 'Punishment', ',', 'by']

text = nltk.Text(tokens) #creating an NLTK text from this list, we can carry out all of the other linguistic processing we saw in 1., along with the regular list operations like slicing:

startcontentsplice = raw.find("PART I")
endcontentsplice = raw.rfind("END OF THE PROJECT GUTENBERG EBOOK CRIME")
raw = raw[5575:1158053]
#raw.find("PART I")
#RAW TEXT
print(type(raw))
print(len(raw))
print(raw[:75])
#TOKENS
#print(tokens)
print(type(tokens))
print(len(tokens))
print(first_ten)
#NLTK Text from the token list
print(type(text))
print(text[1024:1062])
print(text.collocations())
#SLICE CONTENT
print(startcontentsplice) #I CAN FIND THE CORRECT STARTING INDEX 5575
print(endcontentsplice) #CANT FIND END INDEX, KEEP GETTING -1!!!!!! Check the text, different end statement than txtbook, 1158053
print(raw.find("PART I"))
