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

#Define a function to call the Spark API for Rooms and output the response in json.
def show_rooms(your_header):    
	show_rooms_url = spark_url + 'rooms'
	rooms = requests.get(show_rooms_url, headers=your_header)	
	return rooms.json()

#Call base_headers function to set as my_header variable.
my_header = base_headers()
#Call show_rooms function with arg of my_header set previously.  Set as my_rooms.
my_rooms = show_rooms(my_header)
#Output the response from the GET as JSON, Pretty Print of course.
print(json.dumps(my_rooms, indent=4, separators=(',', ': ')))
print()
print()
"""
#Now, let's create a room using the same concepts.
#Define a function to post a new room.
def create_basic_room(your_header,room_name):
    basic_room_url = spark_url + 'rooms'
    basic_room_body = { "title" : room_name }
    post_basic_room = requests.post(basic_room_url, data=json.dumps(basic_room_body), headers=your_header)
    return post_basic_room.json()

#Call the function.  We can use the previously set headers as those haven't changed.
new_room = create_basic_room(my_header,"Test Python Room #1")
print(json.dumps(new_room, indent=4, separators=(',', ': ')))
"""