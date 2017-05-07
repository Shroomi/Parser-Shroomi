class Sentence:
	def __init__(self):
		self.form = []
		self.lemma = []
		self.pos = []
		self.head = []
		self.rel = []
		self.stack = []
		self.buffer = []
		self.arc_gold = {}

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
			print ("Words %d-------------" %count)
			print (' | '.join([form, lemma, pos, head, rel]))
    
	def init_configuration(self):
		self.stack = [0]
		self.buffer = list(range(1, len(self.form)+1))
		self.arc_gold = {}
		for i in range(len(self.form)):
			if int(self.head[i]) not in self.arc_gold:
				self.arc_gold[int(self.head[i])] = [i + 1]
			else:
				self.arc_gold[int(self.head[i])].append(i + 1)
		print ('-'*60)
		print ('Gold Arc is:', self.arc_gold)  
		print ('The init buffer is:', self.buffer)
		print ('The init stack is:', self.stack)
        
	def can_left_arc(self):
		if self.buffer[0] in self.arc_gold and self.stack[-1] in self.arc_gold[self.buffer[0]]:
			return True
		else:
			return False
        
	def can_right_arc(self):
		s1 = set()
		if self.buffer[0] in self.arc_gold:
			s1 = set(self.arc_gold[self.buffer[0]])
		s2 = set(self.buffer) 
		if self.stack[-1] in self.arc_gold and self.buffer[0] in self.arc_gold[self.stack[-1]] and len(s1.intersection(s2)) == 0:
			return True
		else:
			return False
        
	def oracle_parsing(self):
		self.trans = []
		self.init_configuration()
		while len(self.buffer) != 0:
			if len(self.stack) != 0 and self.can_left_arc():
				self.trans.append('left_arc')
				print (str(self.buffer[0]) + '->' + str(self.stack[-1]))
				self.stack.pop()
			elif len(self.stack) != 0 and self.can_right_arc():
				self.trans.append('right_arc')
				print (str(self.stack[-1]) + '->' + str(self.buffer[0]))
				self.buffer.pop(0)
				self.buffer.insert(0, self.stack.pop())
			else:
				self.trans.append('shift')
				self.stack.append(self.buffer.pop(0))
		print ('The direction of transition: ', self.trans)
		print ('-'*60)

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
for sen in sentences:
	count += 1
	print ('The %d sentence:' % count)
	sen.oracle_parsing()