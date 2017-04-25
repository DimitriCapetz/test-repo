#Ranges
print("Print out 0 through 4")
for x in range(5):
    print(x)
print()

print("Print out 1 through 5")
for y in range(1,6):
    print(y)
print()
"""
#Loop for item indexes.
tup1 = ("item1","item2","item3","item4","item5")
print("ITEMS!")
for item in tup1:
    print(item)
print()

#Now, let's define a dictinary of lists.
games = {"PS4":["Horizon: Zero Dawn","Persona 5","Nier: Automata"],"XBox One":["Gears of War 4","Halo 5","ReCore"],"Nintendo Switch":["Breath of the Wild","Mario Kart 8","Snipperclips"]}
#Parsing all these manually would be annoying...
print(games["PS4"][0] + " is a Playstation 4 game.")
print(games["PS4"][1] + " is a Playstation 4 game.")
print(games["PS4"][2] + " is a Playstation 4 game.")
print("Ahhhhhhh!")
print()

#Let's simplify with a loop.
for ps4releases in games["PS4"]:
    print(ps4releases + " is a Playstation 4 game.")
print("Much better!")
print()

#Nest a loop to print them all!
for platform in games:
    for release in games[platform]:
        print(release + " is a video game.")
print()

#Now for a while loop!
switchport = 40
while switchport <= 48:
    print("interface Gi1/" + str(switchport))
    switchport = switchport + 1
print("Gi1/49 is not a valid interface!")
"""