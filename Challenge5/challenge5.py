from more_itertools import locate

results=""
with open('test') as f:
    C = int(f.readline())
    
    for j in range(1,C+1):
        line_text = f.readline().rstrip()
        
        """list_of_twos = list(locate(line_text, lambda a: a == '2')) #to get all the positions where there is a 2
        list_of_twos = map(lambda x: len(line_text)-1-x, list_of_twos)
        #print(list(list_of_twos))
        list_of_twos = list(map(lambda x: x % 3 == 1 , list_of_twos)) #two obtain if the position of the two is one of the called tuentistic: 20, 20000, 20000000, 20000000000
        
        if True in list_of_twos:
            results += f"Case #{j}: {line_text}\n"
        else:"""
        line_number = int(line_text)
        zero_two_twenty = list(range(0,20))
        no_possible_tuentistic = zero_two_twenty + [30,31,32,33,34,35,36,37,38,39,59]
        if line_number in no_possible_tuentistic:
            results += f"Case #{j}: IMPOSSIBLE\n"
        else:
            results += f"Case #{j}: {int(line_number/20)}\n"



text_file = open("Output.txt", "w")
text_file.write(results)
text_file.close()
