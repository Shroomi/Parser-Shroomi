#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:24:22 2017

@author: mengruding
"""

from IOSen import Reader, Writer

##################### read a file and returns sentence objects ################
read_path = 'wsj_train.conll06'
read_sentence = Reader(read_path)
sentences = read_sentence.has_next() #sentences is a list consisting of sentence objects
#print (sentences[0].form[0])

################### write sentences in a file to do sanity-check ##############
write_path = 'wsj_write_back'
write_sentence = Writer(write_path, sentences)
write_sentence.write()