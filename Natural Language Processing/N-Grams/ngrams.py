#!/usr/bin/env python3
import re
import sys
from random import choice
from collections import defaultdict
from abbreviations import abbr

bos = "__BOS__"
eos = "__EOS__"

threegrams = defaultdict(lambda: [])
twograms   = defaultdict(lambda: [])
wordlist   = []

sentence_pat = re.compile(r"[.?!][ \n\t]")
word_pat     = re.compile(r"[A-Za-z]+")

def getfile(fname):
    all = ""
    with open(fname, 'r') as fd:
        for line in fd:
            s = line.replace("\n"," ")
            all += s
    return all

def parse_sentence(s):
    global wordlist, twograms, threegrams

    prev  = bos
    pprev = bos
    for w in word_pat.finditer(s):
        x,y = w.span()
        k = s[x:y]

        wordlist.append(k)
        twograms[prev].append(k)
        threegrams[(pprev,prev)].append(k)

        pprev,prev = prev,k

    wordlist.append(eos)
    twograms[prev].append(eos)

def abfilter(s):
    for k in abbr:
        s = re.sub(k, abbr[k], s)
    return s

def randsentence1():
    while True:
        k = choice(wordlist)
        if k == eos:
            break
        print(k, end=' ')
    print('.')

def randsentence2():
    k = bos
    while k != eos:
        k = choice(twograms[k])
        if k == eos:
            print('.')
        else:
            print(k, end=' ')

def randsentence3():
    k1,k2 = bos,bos
    while True:
        a = threegrams[(k1,k2)]
        if len(a) == 0:
            print('.')
            return
        k3 = choice(a)
        if k3 == eos:
            print('.')
            break
        else:
            print(k3, end=' ')
        k1,k2 = k2,k3

if __name__ == "__main__":

    dict = {}

    doc = getfile(sys.argv[1])
    doc = abfilter(doc)
    doc = re.sub('"','',doc)             

    n = 0
    for x in sentence_pat.split(doc):
        parse_sentence(x)

    keylist = list(twograms.keys())
    keylist.sort(key=lambda x: len(twograms[x]))

     

    print('\n5 sentences from 1-grams:\n')
    for i in range(5):
        print(i+1)
        randsentence1()

    print('\n5 sentences from 2-grams:\n')
    for i in range(5):
        print(i+1)
        randsentence2()

    print('\n5 sentences from 3-grams:\n')
    for i in range(5):
        print(i+1)
        randsentence3()
