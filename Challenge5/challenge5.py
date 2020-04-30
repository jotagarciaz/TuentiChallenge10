#To execute this code first we have to install more_itertools, for it we need to execute: ` pip install more-itertools ` in a terminal
#For this challenge I will receive a number of cases (C) and numbers, that I should check if they are tuntistic or can be done by adding tuentistics.
#At last I have to return the maximun possible of elements of its Tuentistic sums.  
#I checked that the only numbers that are not tuentistics and can't be done by sums are: 
#the ones from 0 to 19, the ones from 30 to 39 and the last one Untuentistic is 59, so I only have to check if the input is or not one of those
#Also the maximun number of possible sums are the combinations of the little tuentistic numbers (from 20 to 29), so I have only to check how many times a number is divided by 20 

from more_itertools import locate


results=""
with open('Input.txt') as f:
    C = int(f.readline())
    
    for case in range(1,C+1):
        lineText = f.readline().rstrip() #get text and remove empty character
        caseNumber = int(lineText)
        zeroToTwenty = list(range(0,20)) #list that contains number from 0 to 19
        noPossiblyTuentistics = zeroToTwenty + [30,31,32,33,34,35,36,37,38,39,59] #list with all Untuentistic numbers
        
        if caseNumber in noPossiblyTuentistics:
            results += f"Case #{case}: IMPOSSIBLE\n"
        else:
            maxNumberOfElements = int(caseNumber//20)
            results += f"Case #{case}: {maxNumberOfElements}\n"



text_file = open("Output.txt", "w")
text_file.write(results)
text_file.close()
