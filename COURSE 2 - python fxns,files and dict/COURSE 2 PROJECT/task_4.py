project_data = open("project_twitter_data.csv", "r")
result_data = open("resulting_data.csv", "w")

s = ''
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    
    for c in punctuation_chars:
        s = s.replace(c, '')
    return s
#end of first function
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
#end of second function
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
#end of third function

def strip_puntuation(strWord):
	for charPunct in punctuation_chars:
		strWord = strWord.replace(charPunct,"")
	return strWord

def write_data_file(result_data):
  	result_data.write("Number of Retweets","Number of Replies","Positive Score","Negative Score","Net Score")
  	result_data.write("\n")

  	linesPTDF = project_data.readlines()
  	headerDontUsed = linesPTDF.pop(0)
  	for linesTD in linesPTDF:
  		listTD = linesTD.strip().split(',')
  		result_data.write("{},{},{},{},{}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0]) - get_neg(listTD[0]))))

  		result_data.write("\n")

write_data_file(result_data)
project_data.close()
result_data.close()

