import nltk, re, pprint
import nltk
nltk.download('punkt') #needed to specifically download this project
from nltk import word_tokenize,sent_tokenize
from urllib import request

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
raw_type = type(raw) #<class 'str'>
raw_len = len(raw)  #789417
raw[:75] #'The Project Gutenberg eBook of Pride and Prejudice, by Jane Austen'

tokens = word_tokenize(raw)
token_type = type(tokens) #<class 'list'>
token_len = len(tokens) #146129
first_ten_tokens = tokens[:10] #['\ufeffThe', 'Project', 'Gutenberg', 'eBook', 'of', 'Pride', 'and', 'Prejudice', ',', 'by']

text = nltk.Text(tokens) #creating an NLTK text from this list, we can carry out all of the other linguistic processing we saw in 1., along with the regular list operations like slicing:
text_type = type(text)
startcontentsplice = raw.find("It is a truth universally acknowledged, ") #1989
endcontentsplice = raw.rfind("END OF THE PROJECT GUTENBERG EBOOK") #770659
content = raw[1989:770659]
contentstart = content.find("It is a truth universally acknowledged, ")


#RAW TEXT
print('The raw type is: ', raw_type)
print('The raw length is: ', raw_len)
print('The first 75 characters of raw are: ', raw[:75])
#TOKENS
#print(tokens)
print('The token type is: ', token_type)
print('The token length is: ', token_len)
print('The first_ten_tokens are: ', first_ten_tokens)
#NLTK Text from the token list
print('The text type is: ', text_type)
print('The random slice of text is: ', text[1024:1062])
print('These are text collocations: ', text.collocations())
#SLICE CONTENT
print('The content start index is: ', startcontentsplice) #I CAN FIND THE CORRECT STARTING INDEX 5575
print('The content start index is: ', endcontentsplice) #CANT FIND END INDEX, KEEP GETTING -1!!!!!! Check the text, different end statement than txtbook, 1158053
print('The content start index is: ', contentstart)
