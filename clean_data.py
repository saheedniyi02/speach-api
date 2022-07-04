import re
from nltk.tokenize import TweetTokenizer




tokenizer=TweetTokenizer(preserve_case=True)
def remove_hashsymbols(text):
    '''Function to remove the hashtag symbol from the text'''
    pattern = re.compile(r'#')
    text = ' '.join(text)
    clean_text = re.sub(pattern,'',text)
    return tokenizer.tokenize(clean_text) 
    
    

def rem_digits(text):
    '''Function to remove the digits from the list of strings'''
    no_digits = []
    for word in text:
        no_digits.append(re.sub(r'\d','',word))
    return ' '.join(no_digits)   
    
    
def rem_nonalpha(text):
    text = [word for word in text if word.isalpha()]
    return text
    
#clean_text:
def clean_text(text):	
    #remove all the user handles --> strings starting with @
    text=re.sub(r'@\w+','',text)
    text=re.sub(r'http\S+','',text)
    text = tokenizer.tokenize(text)
    text=remove_hashsymbols(text)
    text=rem_digits(text)
    text = tokenizer.tokenize(text)
    text=rem_nonalpha(text)
    text=" ".join(text)
    return text