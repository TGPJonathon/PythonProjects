import json
from difflib import get_close_matches

data = json.load(open("Project1\data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? enter Y is yes, N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query"
    else:
        return "The word doesn't exist. Please check your spelling"

word = input("Enter the Word You're Looking For: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)