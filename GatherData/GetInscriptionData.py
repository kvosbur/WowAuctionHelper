from bs4 import BeautifulSoup
import requests

response = requests.get("https://wow.gamepedia.com/Battle_for_Azeroth_inscription_techniques")

response.raise_for_status()
page = response.text

bs = BeautifulSoup(page, "html.parser")
tables = bs.find_all("table", "sortable")


