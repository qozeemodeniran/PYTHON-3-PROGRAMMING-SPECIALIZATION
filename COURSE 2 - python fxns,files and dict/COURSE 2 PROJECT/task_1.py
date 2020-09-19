s = ''
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    
    for c in punctuation_chars:
        s = s.replace(c, '')
    return s

    