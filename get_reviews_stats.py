from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

place_codes = {
'g147365-d2198364':['Stingray City'],
'g147367-d2385044':['Seven Mile Beach'],
'g147366-d4729113':['Cayman Spirits Co Distillery'],
'g147249-d150447':['Eagle Beach'],
'g147249-d539183':['Palm Beach'],
'g147249-d148915':['Arashi Beach'],
'g488162-d2513634':['Philips Animal Garden'],
'g147313-d148623':['High Rated'],
'g147313-d148623':['Low Rated'],
'g147312-d1997485':['High Review'],
'g147312-d1997485':['Low Review'],
'g666621-d4053401':['Dover Beach'],
'g147264-d149093':['Crane Beach'],
'g1183194-d555825':['Enterprise Beach'],
'g147342-d150064':['Anse Chastanet Beach and Reef'],
'g147342-d149013':['Reduit Beach'],
'g147342-d149221':['Jalousie Beach'],
'g147293-d215733':['Bavaro Beach'],
'g259440-d2006612':['Playa Bonita'],
'g317146-d149676':['Sosua Beach']}

mypath = "www.tripadvisor.com/"

captured_stats = open('captured_stats.csv', 'w')

for nextFile in listdir(mypath):
	if isfile(mypath+nextFile):
		reviewCodes = nextFile.split("-")
		if len(reviewCodes) > 3 and place_codes.get(reviewCodes[1]+"-"+reviewCodes[2]) and reviewCodes[3] =='Reviews':
			nextKey = reviewCodes[1]+"-"+reviewCodes[2]
			soup = BeautifulSoup(open(mypath+nextFile), 'html.parser')
			results = soup.find_all("h3", "reviews_header")
			reviewCountList = str(results).split(">")
			reviewCount = int(reviewCountList[1].split("Reviews")[0].replace(",",""))
			place_codes[nextKey].append(reviewCount)
			captured_stats.write(("{0},{1},{2}").format(place_codes.get(nextKey)[0],nextKey, reviewCount)+"\n" )