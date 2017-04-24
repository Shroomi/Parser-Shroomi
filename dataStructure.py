import re

def dataStructure():
	file = open('predata.txt')
	line = file.readline()
	sentences = []
	sentence = []

	while line:
		if line != '\n':
			sentence.append(re.split(r'[\n\t\_\s]+', line))
		else:
			sentences.append(sentence)
			sentence = []

		line = file.readline()

	#print sentences
	file.close()

	#print sentences
	for sen in range(len(sentences)):
		for word in range(len(sentences[sen])):
			#print sentences[sen][word][3]
			sentences[sen][word].pop()
			head = sentences[sen][word][3]
			if head.isdigit(): 
				sentences[sen][word][3] = int(head) - 1

	#print sentences

dataStructure()