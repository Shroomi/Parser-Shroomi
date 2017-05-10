# Parser
## Paser is used to analyze the syntactic structure of a given sentence.

- first step: I create the data structure from original data

        data structure: sentences = [sentence1[word1[form, lemma,...],word2[],word3[],...],sentence2[],sentence3[],...]

        !!!Modified:
        Use OOP data structure in functions append_word, print_word(in oracle_parsing.py)
- second step: I write functions: init_configuration, can_left_arc, can_right_arc, oracle_parsing(in oracle_parsing.py)
			   to manage Arc Standard Parser