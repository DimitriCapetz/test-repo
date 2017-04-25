#Put a list in a list in a list!
inceplist=["item1",["subitem1",["subsubitem1","subsubitem2"],"subitem3"],"item3"]
#Now print the variable, then access various items in the lists.
print(inceplist)
print()
print("Accessing 'item3'...")
print(inceplist[2])
print()
print("Accessing 'subitem1'...")
print(inceplist[1][0])
print()
print("Accessing 'subsubitem2'...")
print(inceplist[1][1][1])
print()

#Create a list of dictionairies and access fields.
hardware=[{"switch1":"C3850","switch2":"C3650"},{"router1":"ISR4451","router2":"ISR4331"},{"firewall1":"ASA5505","firewall2":"FP4100"}]
print("Accessing 'switch2'...")
print(hardware[0]["switch2"])
print()
print("Accessing 'router1'...")
print(hardware[1]["router1"])
print()
print("Accessing 'firewall2'...")
print(hardware[2]["firewall2"])
print()
