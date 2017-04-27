#Load json and requests modules for built-in functions.
import json
import requests

#Set access token for authorization.
token = 'NWNlY2YyZjYtMTllOC00MjQyLTlhNWMtOTg0OTFmM2MyOWU3MTA3YmY4NWYtMzEw'
#Set base Spark URL as this does not change.
spark_url = 'https://api.ciscospark.com/v1/'

#Define a function to concatenate access token into Spark headers to be reused.
def base_headers():         
	auth_header = 'Bearer ' + token
	base_header = {'Authorization': auth_header, 'Content-Type': 'application/json; charset=utf-8'}
	return base_header

#Define a function to call the Spark API for Rooms, filtered to direct rooms only and output the response in json.
def show_direct_rooms(your_header):    
    rooms_url = spark_url + 'rooms'
    direct_param = "?type=direct"
    full_url = rooms_url + direct_param
    direct_rooms = requests.get(full_url, headers=your_header)	
    return direct_rooms.json()

#Call base_headers function to set as my_header variable.
my_header = base_headers()
#Call show_rooms function with arg of my_header set previously.  Set as my_rooms.
my_direct_rooms = show_direct_rooms(my_header)
#Output the response from the GET as JSON, Pretty Print of course.
#print(json.dumps(my_direct_rooms, indent=4, separators=(',', ': ')))
print()
print()

#Now let's parse through to see who we're talking with and the ID of each room.
for direct in my_direct_rooms["items"]:
    print("I'm talking to " + direct["title"] + " in room ID " + direct["id"])

"""
#We don't want our last demo cluttering things up, so let's delete that room.
#Let's define a function to get the room ID of the one we want deleted, then remove it with an API call.
def delete_room(your_header,room_name):
    #First, we have to find the ID of the room to delete.
    get_rooms_url = spark_url + 'rooms'
    rooms = requests.get(get_rooms_url, headers=your_header)
    all_rooms = rooms.json()
    for room in all_rooms['items']:
        if room["title"] == room_name:
            room_id = room["id"]
    # Now load that room id into an API call to delete.  Remember it needs to be part of the URL in this case.
    delete_room_url = spark_url + 'rooms/' + room_id
    delete_basic_room = requests.delete(delete_room_url, headers=your_header)
    print(room_name + " removed.")

#Now we can call the function with our args.
remove_room = delete_room(my_header,"Test Python Room #1")
"""