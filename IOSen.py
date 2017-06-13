#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 18:10:08 2017

@author: mengruding
"""
import csv

class Sentence:
    def __init__(self):
        self.form = []
        self.lemma = []
        self.pos = []
        self.head = []
        self.rel = []
        
    #establish data structure
    def append_word(self, form, lemma, pos, head, rel):
        self.form.append(form)
        self.lemma.append(lemma)
        self.pos.append(pos)
        self.head.append(head)
        self.rel.append(rel)
        
class Reader:
    def __init__(self, path):
        self.path = path
        self.sentences = []
    
    def read_next(self, line, sentence):
        sentence.append_word(line[1], line[2], line[3], line[6], line[7])
    
    def has_next(self):
        print ('open file: '+self.path)
        with open(self.path) as f:
            lines = csv.reader(f, delimiter='\t')
            sentence = Sentence()
            print ('read sentences...')
            for line in lines:
                if len(line) is 0:
                    self.sentences.append(sentence)
                    sentence = Sentence()
                    continue
                self.read_next(line, sentence)
        return self.sentences

class Writer:
    def __init__(self, path, sentences):
        self.path = path
        self.sentences = sentences
    
    def write(self):
        print ('write sentences in the file: '+self.path+'...')
        f = open(self.path, 'w')
        for i in range(len(self.sentences)):
            for j in range(len(self.sentences[i].form)):
                temp = self.sentences[i]
                line = [temp.form[j],temp.lemma[j],temp.pos[j],temp.head[j],temp.rel[j]]
                f.write(str(line) + '\n')
            f.write('\n')
        print ('write sentences successfully!')
        f.close()