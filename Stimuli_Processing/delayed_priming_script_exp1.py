# -*- coding: utf-8 -*-
"""
Python Version: 3.7

This program alternates primes, targets, and nonce words for a delayed priming
experiment with 5-7 item in between pairs

The specific variables work for my experiment - see coming updates for more 
generic script
"""

import pandas

colnames = ['target', 'list_A', 'list_B', 'list_C', 'list_D']
nonce_colname = ['nonce']
content = pandas.read_csv('list_contents.csv', names = colnames)
    #note last row must contain variable 'DUMMY'
nonce = pandas.read_csv('nonce.csv', names = nonce_colname)


target_item_list = content.target.tolist()
prime_item_list_A = content.list_A.tolist()
prime_item_list_B = content.list_B.tolist()
prime_item_list_C = content.list_C.tolist()
prime_item_list_D = content.list_D.tolist()
nonce = nonce.nonce.tolist()

prime_lists = [prime_item_list_A] #, prime_item_list_B, prime_item_list_C, prime_item_list_D]

big_range = ((len(target_item_list)-1) * 2) - 1
little_range = (len(target_item_list)-1) - 1
list_count = 0

for list in prime_lists:
    list_count += 1
    print(f"LIST START{list_count}")
    count = 0
    odd_count = -1
    even_count = 1 
    nonce_count = 0
    filler_count = 0
    modulo = 11
    item = ''
    
    # to ensure primes and targets offset by 2
    print(f"{list[0]}\n{nonce[-1]}\n{nonce[-2]}") 
    print(f"{list[1]}\n{nonce[-3]}\n{nonce[-4]}") 
    
    for i in range(big_range): #39
        count += 1
               
        # to alternate primes, targets, and nonce items
        if count % 2 == 0:
            even_count += 1
            tag_count = even_count
            tag_end = "\n" + nonce[nonce_count]
            nonce_count += 1
            item = list[even_count]
        else:
            odd_count += 1
            tag_count = odd_count
            tag_end = "\n" + nonce[nonce_count]
            nonce_count += 1
            item = target_item_list[odd_count]
        
        # to include extra nonce words to get variation in P-T distance
        if count % 5 == 0 and count % 3 != 0:
            print(nonce[nonce_count])
            nonce_count += 2
        
        if count % 7 == 0:
            print(nonce[nonce_count])
            nonce_count += 1
        
        # to include real word fillers instead of nonce words
        if tag_count % modulo == 0:
            tag_end = "\n FILLER HERE PLEASE"
            filler_count += 1
        
        # to print it all out properly
        if tag_count < little_range: #19
            print(f"{item}{tag_end}") # fuller version: (f"{count}{tag_count}{item}{tag_end}")
        elif tag_count == little_range: #19
            if count % 2 != 0:
                print(f"{nonce[nonce_count]} \n{nonce[nonce_count+1]}")
                print(f"{item}{tag_end}")
            elif count % 2 == 0:
                print(f"{item}{tag_end}")
        
        