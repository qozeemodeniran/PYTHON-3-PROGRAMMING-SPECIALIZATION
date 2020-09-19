
s = ''
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    
    for c in punctuation_chars:
        s = s.replace(c, '')
    return s
#end of strip_punctuation(s)

def get_neg(str_neg):
	str_neg = strip_punctuation(str_neg)
	list_str_neg = str_neg.split()

	count = 0
	for words in list_str_neg:
		for neg_words in negative_words:
			if words == neg_words:
				count += 1
	return count
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())