import requests
from bs4 import BeautifulSoup
from csv import writer
import numpy as np
import pandas as pd

def scrapping(*args):


    p = []
    t = []
    c = []
    ca = []
    d=[]
    text = ""

    pages = np.arange(600, 1000, 1)
    for page in pages:
        url = "https://www.avito.ma/fr/maroc/t%C3%A9l%C3%A9phones-%C3%A0_vendre?o=" + str(page)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        all = soup.find_all('div', class_='oan6tk-0')  # bedelt had class kanet endq ghalta

        # with open('tesdssaw.csv', 'w', encoding='utf8', newline='') as f:
        #   thewriter = writer(f)
        #  header = ['price', 'type', 'city']
        # thewriter.writerow(header)
        for lol in all:
            link = lol.find('a', {'class': 'oan6tk-1 fFOxTQ'}).attrs['href']
            ## hadi katik lien direct bla parsing mea avito
            result = requests.get(link)
            if (result.status_code == 200):

                soup2 = BeautifulSoup(result.content, 'html.parser')
                descriptions = soup2.find_all('div',class_='sc-1g3sn3w-0')
                for description in descriptions:
                    if description.find('p', class_="sc-1x0vz2r-0 bGMGAj") == None:
                        price = None
                    else:
                        price = description.find('p', class_="sc-1x0vz2r-0 bGMGAj").text.strip()


                    if description.find('h1', class_="sc-1x0vz2r-0 glWiuP") == None:
                        type = None
                    else:
                        type = description.find('h1', class_="sc-1x0vz2r-0 glWiuP").text.strip()

                    if description.find('span', class_="sc-1x0vz2r-0 gCIGeB") == None:
                        city = None
                    else:
                        city=description.findAll('span', class_="sc-1x0vz2r-0 gCIGeB")
                        ci=city[0].text

                    if description.find('span', class_="sc-1x0vz2r-0 gCIGeB") == None:
                        date = None
                    else:
                        date=description.findAll('span', class_="sc-1x0vz2r-0 gCIGeB")
                        dt=date[1].text




                    # if description.find('span', class_="iVDpDk") == None:
                    #     cap = None
                    # else:
                    caps = description.find_all('span', class_="iVDpDk")
                    for cap in caps:
                        text += cap.text.strip() + ","


                    p.append(price)
                    t.append(type)
                    c.append(ci)
                    d.append(dt)
                    ca.append(text)
                    text = ""


            else:
                pass



    filee = pd.DataFrame({"price": p, "type": t, "city": c,"date": d, "capa": ca})
    # print (filee)
    filee.to_csv(r'\Users\Dell\Documents\scraping\phones2.csv')


    # info = [price, type, city]
    # print(info)

    # thewriter.writerow(info)