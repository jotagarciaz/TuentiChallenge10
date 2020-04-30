# In this case we have to return the winner of a number of matches N
# We will have also a number of group of matches C, like a kind of tournament
# So for resolve this, we will have a dictionary scores with the players' numbers as a key and the number of victories as a value
# if we receive 1 in the third parameter of a line, then player of the first parameter wins else player of the second parameter wins.

import operator

results=""

with open('Input.txt') as f:
    C = int(f.readline())
    
    i = 1
    for j in range(C):
        scores = {}
        N = int(f.readline())
        
        for _ in range(N):
            line = f.readline()
            
            playersAndScore = line.split(" ")
           
            
            player1 = playersAndScore[0]
            player2 = playersAndScore[1]
            wins = int(playersAndScore[2])

            score_player1 = scores.get(player1,0)
            score_player2 = scores.get(player2,0)

            if wins == 1:
                # number of victories incresed in 1 for the player 1
                scores.update({player1:score_player1+1})
            else:
                # number of victories incresed in 1 for the player 2
                scores.update({player2:score_player2+1})
        
        # return the max score in the dictionary
        results += f"Case #{i}: {max(scores.items(), key=operator.itemgetter(1))[0]}\n"
        i += 1

text_file = open("Output.txt", "w")
text_file.write(results)
text_file.close()
