import json

with open('dataset/lottery.json','r') as file:
    data = json.load(file)


allData = data["data"]
hashed_map = {}

for item in allData:
    parsed = str(item[9]).split() #Getting the winning lottery tickets
    for word in parsed:
        hashed_map[word] = hashed_map.get(word,0) + 1 #For everytime the word comes up increment the dictionary value by 1


sortedKeys = sorted(hashed_map.items(), key= lambda item:item[1], reverse=True) #Sort the dictionary by having the most used number in the first index

print("Five Most frequent numbers that have won the lottery")

i = 1
for key, value in sortedKeys[:5]:
    print(f"{i}. {key} has won {value} times")
    i += 1

