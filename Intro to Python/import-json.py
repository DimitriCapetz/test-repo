#Use the import command to load in json functions.
import json

#This is an ugly json dataset.
artists = {"music":[{"rock":{"classic":"Led Zepplin","indie":"Jimmy Eat World","metal":"Metallica"},"country":{"classic":"Hank Williams","rock":"Garth Brooks"},"pop":{"rock":"Maroon 5","R&B":"Rihanna"}}]}
#Let's use some a json function to clean things up.
print(json.dumps(artists, indent=4, separators=(',', ': ')))