import wowapi
import json
import Models
from Models import auction

client_id = "38b0218c1fb24e4599b60c358b01964d"
client_secret = "tMzdyGzfOE01bCzc6yccCd186MK26TWG"

realm_id = 1171

apiObj = wowapi.WowApi(client_id, client_secret)

'''
b = apiObj.get_auctions(region="us", namespace="dynamic-us", connected_realm_id=realm_id)


temp = auction.get_auction_from_dict(b)

print(len(temp.auctions))
'''


c = apiObj.get_profession_index(region="us", namespace="static-us", locale="en_US")

with open("temp.txt", "w") as f:
    f.write(str(c))
print(c)
