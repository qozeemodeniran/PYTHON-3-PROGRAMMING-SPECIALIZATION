
s = ''
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    
    for c in punctuation_chars:
        s = s.replace(c, '')
    return s
#end of strip_punctuation(s)

def get_pos(str_pos):
	str_pos = strip_punctuation(str_pos)
	list_str_pos = str_pos.split()

	count = 0
	for words in list_str_pos:
		for pos_words in positive_words:
			if words == pos_words:
				count += 1
	return count
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())