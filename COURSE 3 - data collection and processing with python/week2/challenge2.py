# -*- coding: utf-8 -*-
"""
2. Below, we have provided a list of strings called abbrevs. 
Use map to produce a new list called abbrevs_upper that contains all 
the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", 
"jam"]

"""

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", 
"jam"]

def transformer(big):
    return big.upper()
abbrevs_upper = map(transformer, abbrevs)
