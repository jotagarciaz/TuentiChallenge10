import re
import operator

terms = {}
results=""
with open('pg17013.txt','r') as f:
    text = f.read()
    results = text.lower()
    results = re.sub(r'[^abcdefghijklmnñopqrstuvwxyzáéíóúü]',' ',results)
    matches = re.finditer(r"[abcdefghijklmnñopqrstuvwxyzáéíóúü]{3,} *\n*",results)

    results = ""
    for match in matches:
        results += match.group()
    #results = re.sub(r' +',' ',results)

    #falta ordenar por unicode en caso de empate
    
    for term in results.split(" "):
        frecuency = terms.get(term,0)
        terms.update({term:frecuency+1})
    
    terms_dict = {k: v for k, v in sorted(terms.items(), key=lambda item: (-item[1],item[0]))}
    terms_list = sorted(terms.items(), key=lambda item: (-item[1],item[0]))
    
    results = ""
    for term in terms_list:
        results += f"{term[0]}, {term[1]}\n"
 
    results=""
    with open('test','r') as test:
        C = int(test.readline())
        for i in range(1,C+1):
            line = test.readline().rstrip()
            
            if line.isnumeric():
                results += f"Case #{i}: {terms_list[int(line)][0]} {terms_list[int(line)][1]}\n"
            else:
                results += f"Case #{i}: {terms_dict[str(line)]} #{terms_list.index((str(line),terms_dict[str(line)]))}\n"

text_file = open("Output.txt", "w")
text_file.write(results)
text_file.close()
