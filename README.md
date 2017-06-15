# Parser
## Paser is used to analyze the syntactic structure of a given sentence.

1. *First Step*: Input/Output and sentence objects `[IOSen.py]`
	- class Sentence: one sentence is an object of Sentence class with form, lemma, part of speech, head and rel attributes
	- class Reader: read file `[wsj_train.conll06]` to get a list called sentences consisting of Sentence objects
	- class Writer: write sentences back out to a new file `[wsj_write_back]` to make sure the two files are identical

2. *Second Step*: Decoder and Oracle(transition-based) `[Decoder.py]`
	- class State: initialize dependency of words(arc_gold) and update the state of stack, buffer and transition for each step(not used but might be useful in the future)
	- class Transition: execute oracle to get parsing process

3. *Third Step*: Basic feature extraction `[FeatureExtraction.py]`
	- function get_feature: for each step, get feature from stack and buffer(feature: form of buffer[0], pos of buffer[0], form of stack[-1], pos of stack[-1], pos of buffer[1], pos of stack[-2], the head form of stack[-1], pos of the left most dependency of stack[-1], relation of the right most dependency of stack[-1])
	- function store_feature: store all features in form of dictionary
	- function get_feature_vector: get feature vectors for each step
	*write training feature vectors in the file `[feature_vector]`*
	*write trainging labels in the file `[label]`*