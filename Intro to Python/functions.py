#Basic function definition and calling it.
def function1():
    print("I'm 'function1'.\n")

function1()

#Functions can also have things (args) passed into them.
def function2(arg1,arg2):
    print("I'm 'function2' with 'arg1' of " + arg1)
    print("Oh, I forgot!  'arg2' is " + arg2)

function2("heavy","metal")
print()
"""
#Functions are great for things you do multiple times.
print("interface Gi1/1")
print("  switchport")
print("  switchport mode access")
print("  switchport access vlan 100")
print("  switchport voice vlan 200")
print("  speed 1000")
print("  duplex full")
print("  spanning-tree portfast")
print("  no shutdown")
print()
print("interface Gi1/2")
print("  switchport")
print("  switchport mode access")
print("  switchport access vlan 100")
print("  switchport voice vlan 200")
print("  speed 1000")
print("  duplex full")
print("  spanning-tree portfast")
print("  no shutdown")
print("...")
print()

#Now use the function for the same thing.
def portconfig(port):
    print("interface Gi1/" + str(port))
    print("  switchport")
    print("  switchport mode access")
    print("  switchport access vlan 100")
    print("  switchport voice vlan 200")
    print("  speed 1000")
    print("  duplex full")
    print("  spanning-tree portfast")
    print("  no shutdown")

portconfig(1)
portconfig(2)
print()

#Getting sik wit it.
for x in range(1,10):
    portconfig(x)
"""