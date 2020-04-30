#For this problem we only need to check who wins each round
#If Player 0 don't win Player 1 Then
#It can occurs than Player 0 and Player 1 have a draw
#Lastly if none of this cases happens then Player 0 loose.

win = {'R':'S','S':'P','P':'R'}
with open('Input.txt') as f:
    N = f.readline()
    result = ""
    numberCase = 1
    
    for line in f:
        player = line.replace(" ", "")
        if win[player[0]] == player[1]:
            result += f"Case #{numberCase}: {player[0]}\n"
        elif player[0] == player[1]:
            result += f"Case #{numberCase}: -\n"
        else: 
            result += f"Case #{numberCase}: {player[1]}\n"
        numberCase += 1


output = open("Output.txt", "w")
output.write(result)
output.close()
