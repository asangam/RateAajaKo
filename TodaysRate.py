import requests
import bs4

siteNK='https://www.nepalikaam.com'
siteNR='https://www.namasteremittance.com.au'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
} # defining a user agent so the sript will not be blocked from executing by security headers


resNK = requests.get(siteNK)
resNR = requests.get(siteNR,headers=headers)


#type(res)

resNK.text
resNR.text


soupNK = bs4.BeautifulSoup(resNK.text,'html.parser')
soupNR = bs4.BeautifulSoup(resNR.text,'html.parser')


#type(soup)

dataNK = soupNK.select('h5')
dataNR = soupNR.findAll('span', {'class': 'blinking'})

# data = displays all the data within the h5 and class of blinking in NR

unformatted = dataNK[0].getText().lstrip().rstrip()

spaceData = unformatted.replace("\r\n","").replace("as","").replace("of","").replace("(","").replace(")","")

finalRate = spaceData[0:20]

day = spaceData[142:168]


formattedNR = dataNR[0].getText()

print("NK Services " + finalRate+" "+day + " -> $10 Charge")
print("Namaste Remittance " + formattedNR + " -> $5 Charge")
