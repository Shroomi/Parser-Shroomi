class Sentence:
	def __init__(self):
		self.form = []
		self.lemma = []
		self.pos = []
		self.head = []
		self.rel = []

	def append_word(self, form, lemma, pos, head, rel):
		self.form.append(form)
		self.lemma.append(lemma)
		self.pos.append(pos)
		self.head.append(head)
		self.rel.append(rel)

	def print_sentence(self):
		count = 0
		for form, lemma, pos, head, rel in zip(self.form, self.lemma, self.pos, self.head, self.rel):
			count += 1
			print "Words %d-------------" %count
			print ' | '.join([form, lemma, pos, head, rel])

import csv
path = 'wsj_train.conll06'
sentences = []
with open(path, 'r') as f:
	lines = csv.reader(f, delimiter='\t')
	sent = Sentence()
	for line in lines:
		if len(line) is 0:
			sentences.append(sent)
			sent = Sentence()
			continue
		sent.append_word(line[1], line[2], line[3], line[6], line[7])

		#print sent.print_sentence()

#print sentences[46].print_sentence()