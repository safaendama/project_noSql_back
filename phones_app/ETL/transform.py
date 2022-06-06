import requests
from bs4 import BeautifulSoup
from csv import writer
import numpy as np
import pandas as pd

def cleaning(*args):
    data=pd.read_csv(r'C:\Users\Dell\Documents\scraping\derty.csv',sep=',', delimiter=None, engine=None, encoding=None,  error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, low_memory=False )
    del data['Unnamed: 0']
    data.dropna(subset=['price'], how='all', inplace=True)
    data.dropna(subset=['type'], how='all', inplace=True)
    data.dropna(subset=['city'], how='all', inplace=True)
    data.dropna(subset=['capa'], how='all', inplace=True)
    tt =['Neuf','Bon état']
    def matcher(x):
        for i in tt:
            if i.lower() in x.lower():
                return i
        else:
            return np.nan
    data['Stat'] = data['capa'].apply(matcher)
    data[['Stat']] = data[['Stat']].fillna('Bon état')
    pp =['8 GB','16 GB','32 GB', '64 GB','128 GB', '256 GB', '512 GB']
    def matcher(x):
        for i in pp:
            if i.lower() in x.lower():
                return i
        else:
            return np.nan  
    data['Storage'] = data['capa'].apply(matcher)
    data[['Storage']] = data[['Storage']].fillna('32 GB')
    c=['Casablanca','Rabat','Marrakech','Meknès','Fès','Tanger','Agadir','Kénitra','Mohammedia','Salé','Oujda','Kénitra','Témara','Safi','Taza','El Jadida','Nador','Khouribga','Khémisset','Tétouan','Settat']
    def matcher(x):
        for i in c:
            if i.lower() in x.lower():
                return i
        else:
            return np.nan  
    data['City'] = data['city'].apply(matcher)
    data[['City']] = data[['City']].fillna('Casablanca')
    m=["iphone","samsung","alcatel","realme","huawei","oppo","googlepixel","xiaomi","Redmi","HTC","nokia","sony","lenovo","Asus","LG"]
    def matcher(x):
        for i in m:
            if i.lower() in x.lower():
                return i
        else:
            return np.nan  
    data['Brand'] = data['type'].apply(matcher)
    q=['Samsung A03 core','Samsung A12','iphone xs max','iphone xs','iphone x','iphone se','iphonese 2020','iphone 6s','iphone 6s plus','iphone 7','iphone 7 plus','iphone 8','iphone 8 plus','iphone 4','iphone 4s','iphone 4s','iphone 5','iphone 5s','iphone 5c','iphone 13 pro max','iphone 13 pro','iphone 13 mini','iphone 13','iphone 12 pro max','iphone 12 pro','iphone 12 mini','iphone 12','iphone 11 pro max','iphone 11 pro','iphone 11','samsung galaxy a01 core','samsung galaxy a015','samsung galaxy a02','samsung galaxy a02s','samsung galaxy a10s','samsung galaxy a11', 'samsung galaxy a21s','samsung galaxy a3','samsung galaxy a31','samsung galaxy a32','samsung galaxy a5','samsung galaxy a51','samsung galaxy a52','samsung galaxy a71','samsung galaxy fold','samsung galaxy j3','samsung galaxy note10','samsung galaxy note10 lite','samsung galaxy 10+','samsung galaxy note2','samsung galaxy note20','samsung galaxy 20 ultra','samsung galaxy 20ultra','samsung galaxy note3','samsung galaxy note4','samsung galaxy note8','samsung galaxy note9','samsung galaxy s20','samsung galaxy s20 ultra','samsung galaxy s3','samsung galaxy s4','samsung galaxy s5', 'samsung galaxy s6' , 'samsung galaxy s7' , 'samsung galaxy s6 edge','samsung galaxy s8+','samsung galaxy 9', 'samsung galaxy 9+','samsung galaxy z flip','samsung galaxy z flip3','samsung galaxy z fold2','samsung galaxy z fold3','samsung a01 core','samsung a015','samsung a02','samsung a02s','samsung y a10s','samsung a11', 'samsung a21s','samsung a3','samsung a31','samsung a32','samsung a5','samsung a51','samsung a52','samsung a71','samsung fold','samsung j3','samsun g note10','samsung note 10 lite','samsung 10+','samsung note 2','samsung note 20','samsung 20 ultra','samsung note 3','samsung note 4','samsung note 8','samsung note 9','samsung s20','samsung s20 ultra','samsung s3','samsung s4','samsung s5', 'samsung s6' , 'samsung s7' , 'samsung s6 edge','samsung s8+','samsung 9', 'samsung 9+','samsung z flip','samsung z flip3','samsung z fold2','samsung z fold3', 'alcatel 1','alcatel 1x','alcatel 3l','alcatel 5','alcatel 5v','alcatel a3','alcatel a5 led','alcatel idol 3','alcatel idol 4','alcatel idol 5s','alcatel one pop 4','alcatel one touch 995','alcatel one touchc 7','alcatel one touch idol alpha','alcatel one touch pixi3','alcatel one touch pixi4','alcatel one touch pop4','alcatel pixi 4','alcatel u3','alcatel u6','alcatel u5','realme 6','realme 6 pro','realme 7','realme 7 pro','realme 7i','realme c11','realme c12','realme c3','realme x3 superzoom','huawei 30e pro','huawei 40','huawei 40 pro','huawei honor','huawei honor 10x','huawei 9a','huawei honor v30','huawei honor v30 pro','huawei mate 10 pro','huawei mate 20 lite','huawei mate 20 pro','huawei mate 30','huawei mate 30 pro','huawei mate 30 rs','huawei mate xs','huawei nova 5i','huawei nova 5t','huawei nova 7','huawei 7i','huawei p','huawei p Smart','huawei p Smart Pro','huawei p10','huawei p10 Lite','huawei P20','huawei P20 Pro','huawei P30','huawei P30Lite','huawei P30 Pro','huawei P40','huawei P40 Lite','huawei P40 Pro','huawei P40 Pro+','huawei P8 Lite','huawei P9','huawei P9 Lite','huawei Y5P','huawei Y6 Pro','huawei Y6P','huawei Y6S','huawei Y7 Prime','huawei Y7a','huawei Y7a','huawei Y7p','huawei Y8p','huawei Y8s','huaweiY 9a','huawei Y9s','oppo a1','oppo a12','oppo a12s','oppo a15','oppo a15s','oppo a1k','oppo a31','oppo a3s','oppo a5','oppo a52','oppo a53','oppo a5s','oppo a7','oppo a71','oppo a72','oppo a73','oppo a75','oppo a75s','oppo a83','oppo a9','oppo a9 2020','oppo a91','oppo a92','oppo a93','oppo ax7','oppo ax7 pro','oppo f1plus','oppof17','oppof3','oppof7','oppof9 pro','oppofindx2','oppofindx2pro','oppofindx3','oppofind x3 pro','oppo joy3','oppo joy3 plus','oppo k1','oppo k2','oppo neo 5s','oppo ne o5','oppo r11','oppo r11 plus','oppo r11s','oppo r15x','oppo r17','oppo r17 pro','oppo r7','oppo r7 lite','oppo r7 plus','oppo r9 plus','oppo r9s','oppo reno','oppo reno 2z','oppo 4 pro','oppo reno 4 pro','oppo reno 4z','oppo reno 5','google pixel ','google pixel 2','google pixel 2xl','google pixel 3','google pixel 3xl','google pixel 3a','google pixel xl','xiaomi ','xiaomi Mi 10','xiaomi Mi 10 Pro','xiaomi Mi 11','xiaomi Mi 11 Ultra','xiaomi Mi 4','xiaomi Mi 5','xiaomi Mi 5S','xiaomi Mi 6','xiaomi Mi7','xiaomi Mi 8 Lite','xiaomi Mi 8 Pro','xiaomi Mi 8 Pro','xiaomi Mi 9','xiaomi Mi 9','xiaomi Mi 9 SE','xiaomi Mi 9T','xiaomi A1','xiaomi A2','xiaomi A2 Lite','xiaomi Mi Max 2','xiaomi Mi Mix 2','xiaomi Mi Mix 2S','xiaomi Mi Mix 3','xiaomi Mi Note','xiaomi Mi Note2 ','xiaomi Poco F2 pro','xiaomi Poco M3','xiaomi Poco X3','xiaomi Poco X3 Nfc','xiaomi Poco','xiaomi Poco Phone F1','xiaomi Redmi 2','xiaomi Redmi 4i','xiaomi Redmi 4x','xiaomi Redmi 5 Plus','xiaomi Redmi 6','xiaomi 6A','xiaomi 9','xiaomi 9A','xiaomi 9C','xiaomi 9T','xiaomi Go','xiaomi Redmi Note 4','xiaomi Redmi Note 4G','xiaomi Redmi Note 5','xiaomi Redmi Note 5A','xiaomi Redmi Note 6','xiaomi Redmi Note 6 Pro','xiaomi Redmi Note 7','xiaomi Redmi Note 8','xiaomi redmi Note 8 pro','xiaomi Redmi Note 9','xiaomi Redmi Note 9 Pro','xiaomi Redmi Note 9T','xiaomi Redmi S2','xiaomi Poco F2 pro','xiaomi Poco M3','xiaomi Poco X3','xiaomi Poco X3 Nfc','xiaomi Poco','xiaomi PocoPhone F1','xiaomi Redmi 2','xiaomi Redmi 4i','xiaomi Redmi 4x','xiaomi Redmi 5 Plus','Redmi 6','Redmi Note 4','Redmi Note 4G','Redmi Note 5','Redmi Note 5A','Redmi Note 6','Redmi Note 6 Pro','Redmi Note 7','Redmi Note 8','redmi Note 8 pro','Redmi Note 9','Redmi Note 9 Pro','Redmi Note 9T','Redmi S2','HTC 10','HTC','HTC 10 evo','HTC 8X','HTC Desire 10','HTC Desire 10 Lifestyle','HTC Desire 10 Pro','HTC Desire 12','HTC Desire 12','HTC Desire 530','HTC Desire 610','HTC Desire 620','HTC Desire 626','HTC Desire 628','HTC Desire 650','HTC Desire 820','HTC Desire 825','HTC One','HTC One 8','HTC One A9','HTC One M7','HTC One M8','HTC One M9','HTC One M9 Plus','HTC One Mini','HTC One Mini2','HTC OneX','HTC One Xplus','HTC One X10','HTC One Plus','HTC One X9','HTC u11','HTC uPlay','nokia 1','nokia 1 black blue bs','nokia 1 plus','nokia 2','nokia 3','nokia 3.2','nokia 5','nokia 6','nokia 6.1','nokia 7 plus','nokia lumia 1020','nokia lumia 1320','nokia lumia 435','nokia lumia 520','nokia lumia 530','nokia lumia 535','nokia lumia 550','nokia lumia 610','nokia lumia 620','nokia lumia 620','nokia lumia 630','nokia lumia 650','nokia lumia 640','nokia lumia 710','nokia lumia 735','nokia lumia 800','nokia lumia 820','nokia lumia 900','nokia lumia 920','nokia lumia 925','nokia lumia 930','nokia lumia 950','nokia lumia 950 xl','sony xperia e3','sony xperia x','sony xperia xa','sony xperia xa21','sony xperia xz','sony xperia xz2','sony xperia z3','sony xperia z5','blackberry curve','BLACKBERRY Q10','BlackBerry leap','blackberry Q10','Lenovo Legion','lenovo k6 note','lenovo Legion Duel','lenovo P2','lenovo V7','lenovo M10','lenovo Z5','lenovo Z6','lenovo a6000','Asus RogPhone 3','Asus RogPhone 5','Asus ZenPhone 3','Asus RogPhone 2','Asus ZenPhone 4','Asus M930','Asus ZenPhone 6','Asus ZenPhone X008D','Asus Zen Phone Max Pro','LG G5','LG Q6','LG K41S','Lg k20','LG Q6','LG k51s','LG k11','LG v30','LG k40s','LG G8S','LG G4','LG x']
    def matcher(x):
        for i in q:
            if i.lower() in x.lower():
                return i
        else:
            return np.nan  
    data['Model'] = data['type'].apply(matcher)
    del data['type']
    del data['capa']
    del data['marque']
    data.dropna(subset=['Brand'], how='all', inplace=True)
    data.dropna(subset=['Model'], how='all', inplace=True)
    data.price=data.price.str[:-2]
    data.Storage=data.Storage.str[:-2]
    data['price']=data['price'].str.replace("\\u202f", "",regex=True)
    data['price']=data['price'].astype(str).astype(int)
    data['Storage'] = data['Storage'].astype('int64')
    data.columns = ['Price', 'Date', 'Stat', 'Storage','City','Brand','Model']
    data = data.reindex(columns=['Price','City', 'Date','Brand','Model','Storage','Stat'])
    data.loc[(data['Price'] < 200) | (data['Price'] > 20000)].count()
    data = data[(data['Price'] > 200) & (data['Price'] < 20000)]
    data.loc[data['Price'] > 20000].count()
    data.to_csv('phone_avito.csv')                               