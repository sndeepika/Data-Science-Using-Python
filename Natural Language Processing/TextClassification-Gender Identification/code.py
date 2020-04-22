
import re
import sys
import numpy as np
from random import choice



sentence_pat = re.compile(r"[.?!;][ \n\t]")
word_pat     = re.compile(r"[A-Za-z]+")

malewordlist=[]
femalewordlist=[]
words=[]
pronouns=[ 'you','he','she', 'it', 'we', 'they', 'me', 'him', 'her', 'us','them','myself','yourself','himself','herself','itself','ourselves','yourselves','themselves',
          'oneself','your','my','their','his','her','i']
def parse_sentence(s):
    for w in word_pat.finditer(s):
        x,y = w.span()
        k = s[x:y]
        words.append(k)
    
def getfile(fname):
    all = ""
    for name in fname:
        with open(name, 'r',encoding="utf8") as fd:
            for line in fd:
                s = line.replace("\n"," ")
                all += s
    return all

def getRatio(text,count):
    pcount=0
    for word in text:
        if word in pronouns:
           pcount=pcount+1
    ratio=pcount/count
    return np.round(ratio,6)
        
if __name__ == "__main__":
    male=['boy1.txt','boy2.txt','boy3.txt','boy4.txt','boy4.txt']
    female=['girl1.txt','girl2.txt','girl3.txt','girl4.txt','girl5.txt']
    malewordlist=getfile(male)
    malewordlist = re.sub('"','',malewordlist)
    for x in sentence_pat.split(malewordlist):
        parse_sentence(x.lower())
    malewordlist=words
    male_word_count=len(malewordlist)
    male_ratio=getRatio(words,male_word_count)
    
    
    
    
    femalewordlist=getfile(female)
    femalewordlist = re.sub('"','',femalewordlist)
    for x in sentence_pat.split(femalewordlist):
        parse_sentence(x.lower())
    femalewordlist=words
    female_word_count=len(femalewordlist)
    female_ratio=getRatio(words,female_word_count)
    print(male_ratio,female_ratio)
    
    
    
    

