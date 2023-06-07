import nltk
nltk.download('punkt')
import re, string

custom_stopwords = ['ek','hai','tyo','nai','k', 'ko', 'ma', 'la','lai', 'le', 'ka', 'ko', 'ho','ehh','hmm','ha','hajur','ta','haha' , 'vayo','timi','tapai','uni','usko','usle','unle','ake','yrr','oh' ,'ohh', 'hun', 'ta', 'ra','po','pani','yesle','ni','hamro','tw','tmle','tmlai','tmele','yo','chhan','xa','pni','chha','timro','timi','maile','ma' ,'honi','hota']

def clean_sent(sent):

    #if isinstance(sent, str):
        # If a single text input is provided, convert it to a list
        #sent = [sent]
    words = nltk.word_tokenize(sent)
    
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    words = [re_punc.sub('' ,word) for word in words]
    
    re_printable = re.compile('[^%s]' %re.escape(string.printable))
    words = [re_printable.sub('',word)for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word)>1]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word not in custom_stopwords]
    words = [word[:-4] + 'xa' if word.endswith('chha') else word for word in words]
    words = [word[:-5] + 'xan' if word.endswith('chhan') else word for word in words]
    words = [word[:-5] + 'xau' if word.endswith('chhau') else word for word in words]
    words = [word[:-2] + 'xa' if word.endswith('ch') else word for word in words]
    words = [word[:-5] + 'xaina' if word.endswith('chain') else word for word in words]
    words = [word[:-7] + 'xaina' if word.endswith('chhaina') else word for word in words]
    words = [word[:-6] + 'xaina' if word.endswith('chaina') else word for word in words]
    

 
    
    #words = [wn.lemmatize(word ,pos='v') for word in words]
    
    words = [word[:-4] if (word.endswith('haru') and len(word) > 4) else word for word in words]
    words = [word[:-2] if (word.endswith('ko') and len(word) > 2) else word for word in words]
    words = [word[:-3] if (word.endswith('lai') and len(word) >3) else word for word in words]
    words = [word[:-2] if word.endswith('ko') and len (word)> 2 else word for word in words]
    words = [word[:-4] if word.endswith('hos') and len (word)> 3 else word for word in words]
    words = [word[:-4] if word.endswith('sake')and len (word)> 4 else word for word in words]
    words = [word[:-4] if word.endswith('paxi')and len (word)> 4 else word for word in words]
    words = [word[:-5] if word.endswith('kheri') and len (word)> 5 else word for word in words]
    words = [word[:-2] if word.endswith('ma') and len (word)> 2 else word for word in words]
    words = [word[:-5] if word.endswith('hunxa') and len (word)> 5 else word for word in words]
    words = [word[:-5] if word.endswith('hunxu')and len (word)> 5 else word for word in words]
    words = [word[:-2] if word.endswith('xu')and len (word)> 2 else word for word in words]
    words = [word[:-2] if word.endswith('xa')and len (word)> 2 else word for word in words]
    words = [word[:-4] if word.endswith('vayo')and len (word)> 4 else word for word in words]
    words = [word[:-2] if word.endswith('le')and len (word)> 2 else word for word in words]
    #words =[word[:-len(suffix)] if (word.endswith(suffix) and len(word) > len(suffix)) else word for word in words for suffix in common_suffixes]
    
    words = set(words)
    
    return  " ".join(words)
