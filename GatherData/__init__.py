import wowapi
import os

client_id = os.environ["Client_ID"]
client_secret = os.environ["Client_Secret"]

realm_id = 1171
# 1369
# 158364

region = "us"
static_ns = "static-us"
dynamic_ns = "dynamic-us"
locale = "en_US"

apiObj = wowapi.WowApi(client_id, client_secret)