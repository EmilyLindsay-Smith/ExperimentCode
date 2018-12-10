# -*- coding: utf-8 -*-
"""
Python Version: 3.7

This program alternates primes, targets, and nonce words for a delayed priming
experiment with 5-7 item in between pairs

The specific variables work for my experiment - see coming updates for more 
generic script
"""

import pandas

colnames = ['target', 'list_A', 'list_B']
nonce_colname = ['nonce']
content = pandas.read_csv('list_contents2.csv', names = colnames)
nonce = pandas.read_csv('nonce2.csv', names = nonce_colname)


target_item_list = content.target.tolist()
prime_item_list_A = content.list_A.tolist()
prime_item_list_B = content.list_B.tolist()
nonce = nonce.nonce.tolist()

prime_lists = [prime_item_list_A, prime_item_list_B]

list_count = 0

big_range = ((len(target_item_list)-1) * 2) - 1
little_range = (len(target_item_list)-1) - 1

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
    etype = ''
    # to ensure primes and targets offset by 2
    print(f"{list[0]}\n{nonce[-1]}\n{nonce[-2]}") 
    print(f"{list[1]}\n{nonce[-3]}\n{nonce[-4]}") 
    
    for i in range(big_range):
        count += 1
               
        # to alternate primes, targets, and nonce items
        # to produce labels (pair1-T) rather than items (shirk),
        # (1) uncomment the #A lines
        # (2) comment out the line directly above each one
        if count % 2 == 0:
            even_count += 1
            tag_count = even_count
            tag_end = "\n" + nonce[nonce_count]
            nonce_count += 1
            item = list[even_count]
            etype = 'P'
        else:
            odd_count += 1
            tag_count = odd_count
            tag_end = "\n" + nonce[nonce_count]
            nonce_count += 1
            item = target_item_list[odd_count]
            etype = 'T'
        
        # to include extra nonce words to get variation in P-T distance
        if count % 5 == 0 and count % 3 != 0:
           print(nonce[nonce_count])
           #A print("nonce")
           nonce_count += 2
        
        if count % 7 == 0:
            print("nonce")
            #A print(nonce[nonce_count])
            nonce_count += 1
        
        # to include real word fillers instead of nonce words
        if tag_count % modulo == 0:
            tag_end = "\n FILLER HERE PLEASE"
            filler_count += 1
        
        # to print it all out properly
        if tag_count < little_range  :
            print(f"{item}{tag_end}") # fuller version: (f"{count}{tag_count}{item}{tag_end}")
            #A print(f"pair{tag_count}-{etype}\nnonce")
        elif tag_count == little_range :
            if count % 2 != 0:
                print(f"{nonce[nonce_count]} \n{nonce[nonce_count+1]}")
                #A print("nonce \nnonce")
                print(f"{item}{tag_end}")
                #A print(f"pair{tag_count}-{etype}\nnonce")                
            elif count % 2 == 0:
                print(f"{item}{tag_end}")
                #A print(f"pair{tag_count}-{etype}\nnonce")
                
        
        