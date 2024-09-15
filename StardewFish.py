import requests
from bs4 import BeautifulSoup

def remove_strings_with_substring(strings, substring):
	return [s for s in strings if substring not in s]

DataList = []

URL = "https://stardewvalleywiki.com/Fish"
page = requests.get(URL)

website = BeautifulSoup(page.content, "html.parser")
table = website.find_all('table', class_="wikitable sortable roundedborder")

for result in table:
	tablebody = result.find('tbody')
	FishList = tablebody.text.split("\n")
	FishList = list(filter(None, FishList))
	DataList.extend(FishList)

DataList = remove_strings_with_substring(DataList, "data")
DataList = remove_strings_with_substring(DataList, "\t")

i = 0
while i < 14:
	DataList.pop(0)
	i += 1

Fish = input("What fish would you like info for? ").title()

if Fish in DataList:
	Index = DataList.index(Fish)
else:
	print("That's not a fish!")

if Fish == 'Midnight Squid' or Fish == 'Spook Fish' or Fish == 'Blobfish':
	print("These fish can be caught in the submarine ride at the Night Market during Winter 15-17, while the market is open (5pm – 2am). They can also be caught during any weather and at any time by using Magic Bait in the southwest corner of The Beach.")

elif Fish == 'Lobster' or Fish == 'Clam' or Fish == 'Crayfish' or Fish == 'Crab' or Fish == 'Cockle' or Fish == 'Mussel' or Fish == 'Shrimp' or Fish == 'Snail' or Fish == 'Periwinkle' or Fish == 'Oyster':
	print("Those are from crabpots.")

elif Fish == 'Seaweed' or Fish == 'Green Algae' or Fish == 'White Algae' or Fish == 'Maki Roll' or Fish == 'Quality Fertilizer' or Fish == 'Sashimi':
	print("That's not a fish!")

else:
	print("")
	print("Found in: " + DataList[Index + 14])
	print("Time: " + DataList[Index + 15])

	season = DataList[Index + 16]
	seasonList = []
	if 'Spring' in season:
		seasonList.append('Spring')
	if 'Summer' in season:
		seasonList.append('Summer')
	if 'Fall' in season:
		seasonList.append('Fall')
	if 'Winter with Rain Totem' in season:
		seasonList.append('Winter with Rain Totem')
	elif 'Winter' in season:
		seasonList.append('Winter')
	if 'All Seasons on Ginger Island' in season:
		seasonList.append('All Seasons on Ginger Island')
	elif 'All Seasons' in season:
		seasonList.append('All Seasons')

	print("Season: ", end="")
	for item in seasonList:
		print(item, end="")
		if len(seasonList) >= seasonList.index(item) + 2:
			print(", ", end="")
		else:
			print("")

	weather = DataList[Index + 17]
	weatherList = []
	if 'Any' in weather:
		weatherList.append('Any')
	if 'Rain' in weather:
		weatherList.append('Rain')
	if 'Sun' in weather:
		weatherList.append('Sun')
	if 'Wind' in weather:
		weatherList.append('Wind')

	print("Weather: ", end="")
	for item in weatherList:
		print(item, end="")
		if len(weatherList) >= weatherList.index(item) + 2:
			print(", ", end="")
		else:
			print("")

	print("")
	print("Sell prices for Normal, Iron, Gold, & Iridium Quality respectively: " + DataList[Index + 2] + ", " + DataList[Index + 3] + ", " + DataList[Index + 4] + ", " + DataList[Index + 5])
	print("Sell prices with the 25% buff: " + DataList[Index + 6] + ", " + DataList[Index + 7] + ", " + DataList[Index + 8] + ", " + DataList[Index + 9])
	print("Sell prices with the 50% buff: " + DataList[Index + 10] + ", " + DataList[Index + 11] + ", " + DataList[Index + 12] + ", " + DataList[Index + 13])