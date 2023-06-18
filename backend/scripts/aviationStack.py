import requests
import json

params = {
  'access_key': '4e3572cc3f3cd85159ea8f7d0d4cb877',
#   'flight_date': '2023-06-18'
  'dep_iata': 'DEL'
}



f = open(r'.\..\datasets\aviationStack-api-test.json', 'w')
api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
api_response = api_result.json()
json.dump(api_response, f)
f.close()

print(api_response)



for flight in api_response['data']:
    if (flight['live']['is_ground'] is False):
        print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
            flight['airline']['name'],
            flight['flight']['iata'],
            flight['departure']['airport'],
            flight['departure']['iata'],
            flight['arrival']['airport'],
            flight['arrival']['iata']))