#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:45:53 2017

@author: mengruding
"""

from oracle_parsing import Sentence
import csv

path = 'wsj_train.conll06'
sentences = []
count = 0
with open(path, 'r') as f:
	lines = csv.reader(f, delimiter='\t')
	sent = Sentence()
	for line in lines:
		if len(line) is 0:
			sentences.append(sent)
			sent = Sentence()
			continue
		sent.append_word(line[1], line[2], line[3], line[6], line[7])

		#print (sent.print_sentence())

#print (sentences[3].print_sentence())
#sentences[1].oracle_parsing()
#print (sentences[3].can_right_arc())
trans = []
for sen in sentences:
	count += 1
	print ('The %d sentence:' % count)
	trans.append(sen.oracle_parsing(sen.form, sen.head))