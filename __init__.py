from Database import session
from GatherData import GetAuctionData

import os
from dotenv import load_dotenv
base_directory = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(base_directory, ".env")
load_dotenv(env_file_path)



if __name__ == "__main__":
    temp = GetAuctionData.get_auction_data()
    GetAuctionData.insert_auction_data(temp)
