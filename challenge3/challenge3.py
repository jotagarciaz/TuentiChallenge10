import re
#For this challenge we have two input Galdo's text (pg17013.txt) and some queries of words or ranks to obtain from the Galdo's text
#First we have to clean the text to leave it as a kind of standars, following the steps in the web.
#If the input is a word (W), we have to show its rank and the number of instances of that word are in the text
#If the input is a number(R), we have to get the word and the number of instances according to the rank number received.
#To be fast enough I will choose a dictionary to keep the words and its number of instances.
#I will need to reorder the dictionary at the end, to keep first the words with more instances in the text
#In case of draw in two or more words the ordew will be by alfabet.

import operator

terms = {} #dictionary that will content the words and its ranks
results=""

with open('pg17013.txt','r') as f:
    text = f.read()
    results = text.lower() #First step of the standard, all the words should be in lower case.
    results = re.sub(r'[^abcdefghijklmnñopqrstuvwxyzáéíóúü]',' ',results) #second step of the standard, consider only a, b , c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z, á, é, í, ó, ú, ü.  replacing with spaces.
    matches = re.finditer(r"[abcdefghijklmnñopqrstuvwxyzáéíóúü]{3,} *\n*",results) #third step, only words with 3 or more letters

    results = "" #Variable that will contain at the end the results of the output.txt
    for match in matches:
        results += match.group() #code neccesary to get the words with 3 or more cases
    
    
    for term in results.split(" "): #counting terms and its instances
        frecuency = terms.get(term,0)
        terms.update({term:frecuency+1})
    
    #A dictionary and a list with the same information, the terms oredered by instances and alfabet
    termsDictOrdered = {k: v for k, v in sorted(terms.items(), key=lambda item: (-item[1],item[0]))} 
    termsListOrdered = sorted(terms.items(), key=lambda item: (-item[1],item[0])) #list of tuples first element in tuple is the word the second the instances
    
 
    results=""
    with open('Input.txt','r') as test:
        C = int(test.readline()) #number of cases
        
        for i in range(1,C+1):
            line = test.readline().rstrip() #line with whitespace remove it
            if line.isnumeric(): #If the line in te input is a number then do this else do that
                R = int(line)
                word = termsListOrdered[R][0]
                instance = termsListOrdered[R][1]
                results += f"Case #{i}: {word} {instance}\n"
            else:
                W = str(line)
                instance = termsDictOrdered[W]
                indexW = termsListOrdered.index((W,instance)) 
                results += f"Case #{i}: {instance} #{indexW}\n"

text_file = open("Output.txt", "w")
text_file.write(results)
text_file.close()
