import wowapi
import os

client_id = os.environ["Client_ID"]
client_secret = os.environ["Client_SECRET"]

realm_id = 1171

region = "us"
namespace = "static-us"
locale = "en_US"

apiObj = wowapi.WowApi(client_id, client_secret)