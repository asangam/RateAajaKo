from flask import Flask, render_template, request
import requests
import bs4

app = Flask(__name__)
@app.route('/')
def index():
    siteNK='https://www.nepalikaam.com'
    siteNR='https://www.namasteremittance.com.au'
    siteNME='https://nepalmoneyexpress.com.au/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    } # defining a user agent so the sript will not be blocked from executing by security headers


    resNK = requests.get(siteNK)
    resNR = requests.get(siteNR,headers=headers)
    resNME = requests.get(siteNME,headers=headers)


    #type(res)

    resNK.text
    resNR.text
    resNME.text


    soupNK = bs4.BeautifulSoup(resNK.text,'html.parser')
    soupNR = bs4.BeautifulSoup(resNR.text,'html.parser')
    soupNME = bs4.BeautifulSoup(resNME.text,'html.parser')



    #type(soup)

    dataNK = soupNK.select('h5')
    dataNR = soupNR.findAll('span', {'class': 'blinking'})

    # data = displays all the data within the h5 and class of blinking in NR

    unformatted = dataNK[0].getText().lstrip().rstrip()

    spaceData = unformatted.replace("\r\n","").replace("as","").replace("of","").replace("(","").replace(")","")

    finalRate = spaceData[0:20]

    a = []
    for word in finalRate.split():
            try:
                a.append(float(word))
            except ValueError:
                pass
    
    formattedNK = a[0]

    #day = spaceData[142:168]


    formattedNR = dataNR[0].getText()

    # Because NME displays custom tag hence retrieving the value from the xml kinda attribute
    for rate in soupNME.find_all("home"):
        formattedNME=(rate["exchange_rate"])

    return render_template('index.html',**locals())

@app.route('/',methods=['POST'])
def send():

    siteNK='https://www.nepalikaam.com'
    siteNR='https://www.namasteremittance.com.au'
    siteNME='https://nepalmoneyexpress.com.au/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    } # defining a user agent so the sript will not be blocked from executing by security headers


    resNK = requests.get(siteNK)
    resNR = requests.get(siteNR,headers=headers)
    resNME = requests.get(siteNME,headers=headers)


    #type(res)

    resNK.text
    resNR.text
    resNME.text


    soupNK = bs4.BeautifulSoup(resNK.text,'html.parser')
    soupNR = bs4.BeautifulSoup(resNR.text,'html.parser')
    soupNME = bs4.BeautifulSoup(resNME.text,'html.parser')



    #type(soup)

    dataNK = soupNK.select('h5')
    dataNR = soupNR.findAll('span', {'class': 'blinking'})

    # data = displays all the data within the h5 and class of blinking in NR

    unformatted = dataNK[0].getText().lstrip().rstrip()

    spaceData = unformatted.replace("\r\n","").replace("as","").replace("of","").replace("(","").replace(")","")

    finalRate = spaceData[0:20]

    a = []
    for word in finalRate.split():
            try:
                a.append(float(word))
            except ValueError:
                pass
    
    formattedNK = a[0]

    #day = spaceData[142:168]


    formattedNR = dataNR[0].getText()

    # Because NME displays custom tag hence retrieving the value from the xml kinda attribute
    for rate in soupNME.find_all("home"):
        formattedNME=(rate["exchange_rate"])
    a=3
    if request.method == 'POST':
        NKC= int(request.form['aud'])
        nkSum=str(formattedNK * NKC)
        return  render_template('index.html',a=3,NKC=NKC,nkSum=nkSum,formattedNR=formattedNR,formattedNK=formattedNK,formattedNME=formattedNME)





if __name__ == '__main__':
    app.debug = True
    app.run()