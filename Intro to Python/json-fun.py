#Look Familiar?
games = {"PS4":["Horizon: Zero Dawn","Persona 5","Nier: Automata"],"XBox One":["Gears of War 4","Halo 5","ReCore"],"Nintendo Switch":["Breath of the Wild","Mario Kart 8","Snipperclips"]}
best_game = games["Nintendo Switch"][0]
print(best_game)
print()

#And just to drive the point home.
jsons = {"response":[{"key1":"value1","key2":"value2"},{"key3":"value3","key4":"value4"}]}
print(jsons["response"][1]["key4"])
print()
"""
#Now we can use loops to parse through large datasets.
artists = {"music":[{"rock":{"classic":"Led Zepplin","indie":"Jimmy Eat World","metal":"Metallica"},"country":{"classic":"Hank Williams","rock":"Garth Brooks"},"pop":{"rock":"Maroon 5","R&B":"Rihanna"}}]}

print(artists["music"][0]["country"]["classic"])
print()
for genre in artists["music"][0]["rock"]:
    print(genre, artists["music"][0]["rock"][genre])
"""