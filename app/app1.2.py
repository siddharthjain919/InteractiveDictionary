import json
from difflib import get_close_matches


data= json.load(open("dictionary\data.json"))

def find(word):
    word= word.lower()  
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()] 
    elif word.upper() in data:
        return data[word.upper()]      
    elif len(get_close_matches(word, data.keys(), cutoff= 0.8)) >0:
        yn= input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if yn =="Y" or "y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn=="N" or "n":
            return "The word doesn't exist."    
        else:
            return "Invalid input."    
    else:
        return "The word doesn't exist. Kindly double check it."    
    
word = input("Enter the word: ")  

defination= find(word)

if type(defination) == list:
    for item in defination:
        print(item)
else :
    print(defination)        

