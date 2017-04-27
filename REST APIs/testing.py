import json
import requests

#Set access token for authorization.
token = 'NWNlY2YyZjYtMTllOC00MjQyLTlhNWMtOTg0OTFmM2MyOWU3MTA3YmY4NWYtMzEw'
#Set base Spark URL as this does not change.
spark_url = 'https://api.ciscospark.com/v1/'

def base_headers():         
	auth_header = 'Bearer ' + token
	base_header = {'Authorization': auth_header, 'Content-Type': 'application/json; charset=utf-8'}
	return base_header

my_header = base_headers()