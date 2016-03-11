from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

place_codes = {'Stingray City':'g147365-d2198364','Seven Mile Beach':'g147367-d2385044','Cayman Spirits Co. Distillery':'g147366-d4729113','Eagle Beach':'g147249-d150447','Palm Beach':'g147249-d539183','Arashi Beach':'g147249-d148915','Philips Animal Garden':'g488162-d2513634','Overview ':'g147313-d148623','High Rated':'g147313-d148623','Low Rated':'g147313-d148623','High Review':'g147312-d1997485','Low Review':'g147312-d1997485','dover beach':'g666621-d4053401','Crane Beach':'g147264-d149093','Enterprise Beach':'g1183194-d555825','Anse Chastanet Beach and Reef':'g147342-d150064','Reduit Beach':'g147342-d149013','Jalousie Beach':'g147342-d149221','Bavaro Beach':'g147293-d215733','Playa Bonita':'g259440-d2006612','Sosua Beach':'g317146-d149676'}

mypath = "www.tripadvisor.com/"
#mypath = "/Users/rogeliozuniga/Google Drive/Personal_Ro/GADAT/hw_git/data_science_final_project/www.tripadvisor.com/"

captured = open('captured_reviews.csv', 'w')
captured_text = open('captured_reviews_text_only.txt', 'w')

for nextFile in listdir(mypath):
	if isfile(mypath+nextFile):
		reviewCodes = nextFile.split("-",3)
		if reviewCodes[0] == "Attraction_Review" or reviewCodes[0] == "ShowUserReviews":
			soup = BeautifulSoup(open(mypath+nextFile), 'html.parser')
			results = soup.find_all("div", "reviewSelector")
			for nextTag in results:
				ratingDateResults = nextTag.find('span','relativeDate')
				if ratingDateResults:
					reviewDate = ratingDateResults['title'].replace(',','')
				
				nextReviewTag = nextTag.find('p','partial_entry')

				if nextReviewTag and nextReviewTag.string:
					reviewText = nextReviewTag.string.encode('utf-8').strip().replace(',','').replace("\n",' ')
				else:
					reviewText = ''

				captured.write(("{0},{1},{2},{3}").format(reviewCodes[1],reviewCodes[2],reviewDate, reviewText)+"\n" )
				captured_text.write(reviewText+"\n")