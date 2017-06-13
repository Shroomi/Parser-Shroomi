# Parser
## Paser is used to analyze the syntactic structure of a given sentence.

1. first step: Input/Output and sentence objects `(IOSen.py)`
	- class Sentence: one sentence is an object of Sentence class with form, lemma, part of speech, head and rel attributes
	- class Reader: read file 'wsj_train.conll06' to get a list called sentences consisting of Sentence objects
	- class Writer: write sentences back out to a new file 'wsj_write_back' to make sure the two files are identical