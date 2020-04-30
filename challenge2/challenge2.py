import operator



results=""
with open('test') as f:
    C = int(f.readline())
    
    i = 1
    for j in range(C):
        scores = {}
        N = int(f.readline())
        for _ in range(N):
            line = f.readline()
            aux= line.split(" ")
            score_aux_1 = scores.get(aux[0],0)
            score_aux_2 = scores.get(aux[1],0)
           
            if int(aux[2]) == 1:
                scores.update({aux[0]:score_aux_1+1})
            else:
                scores.update({aux[1]:score_aux_2+1})

        results += f"Case #{i}: {max(scores.items(), key=operator.itemgetter(1))[0]}\n"
        i += 1

text_file = open("Output.txt", "w")
text_file.write(results)
text_file.close()
