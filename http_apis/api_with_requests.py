import json

import requests
from pprint import pprint

# pc_req = requests.get("https://api.postcodes.io/postcodes/SE12 0NB")

# print(pc_req, type(pc_req))
#
# print(pc_req.status_code)

# if pc_req.status_code == 200:
#     # print(dict(pc_req.headers))
#     print(pc_req.content)
#     postcode = json.loads(pc_req.content)
#     print(postcode)
#     postcode = pc_req.json()
#     print(type(postcode))
#     result = postcode['result']
#     print(result['admin_district'])
#     print(result['eastings'], result['northings'])


headers = {'Content-Type': 'application/json'}
body = {'postcodes': ['PR3 OSG', 'M45 6TN', 'EX165BL']}

pc_req = requests.post(
    url="https://api.postcodes.io/postcodes/",
    headers=headers,
    data=json.dumps(body)
    )
print(pc_req)
pcs = pc_req.json()['result']

for pc_data in pcs:
    result = pc_data['result']
    print(result['postcode'])
    print(result['admin_ward'])
    print(result['easting'], result['northing'])
