
diction = {"%": "%25", "0":"%30","1":"%31","2":"%32","3":"%33","4":"%34","5":"%35","6":"%36","7":"%37","8":"%38","9":"%39", "A": "%41", "B": "%42", "C":"%43", "D":"%44","E":"%45", "F":"%46"}
input_str=input("Input str")
string = ""
for i in range(len(input_str)):
    try:
        string += diction[input_str[i]]
    except:
        string += input_str[i]
print(string)