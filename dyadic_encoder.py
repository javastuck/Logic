# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 22:14:49 2017

@author: Justin.Stuck
"""

import numpy as np

def encoded_val(x):
    """ :param x: the dyadic numeral encoding 
        :return: the conceptual number encoded by x
    """
    
    val = 0
    power = 0
    while x>0:
        val += (2**power)*(2-x%2)
        x = x//10
        power += 1
    return val
        

def dyadic_encoder(x):
    """ :param x: the conceptual number you want to encode
        :return: the dyadic numeral encoding
    """
    
    encoding_length = int(np.log2(x))
    encoding = int((1./9)*10**encoding_length)
    encoded_concept_val = encoded_val(encoding)
    for i in reversed(range(encoding_length)):
        if encoded_concept_val == x:
            break
        else:
            tmp_encoding = encoding + 10**i
            if encoded_val(tmp_encoding) <= x:
                encoding = tmp_encoding
    return encoding
    


if __name__ == "__main__":
    conceptual_nums = [535, 235, 914]
    for num in conceptual_nums:
        print(dyadic_encoder(num))
    concat = int(str(dyadic_encoder(235)) + str(dyadic_encoder(914)))
    print(concat)
    print(encoded_val(concat))
    