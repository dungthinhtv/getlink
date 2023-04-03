from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from slugify import slugify

df = pd.read_csv("movies_title_new.csv")

path = "chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


names = []
slugs = []
src1s=[]
src2s=[]
src3s=[]
links=[]
descs = []
years=[]


for i,row in df.iterrows():
    
    if i < 100:
    
    
        # print(row['link'])
        driver.get('https://phimmoi9.net/Full/' + row['link'] + '.html')
        
        print(str(i) + '-' + row["name"])
        
        descs.append(row['desc'])
        names.append(row['name'])
        slugs.append(slugify(row['name']))
        years.append(row['year'])
        links.append('https://phimmoi9.net/' + row['link'] + '.html')
        
        try:
            src1 = driver.find_element(by="xpath",value='//*[@id="go-server"]/center/ul/li/ul/li/a[1]').get_attribute("onclick")
            src1 = src1.replace("document.getElementById('phimmoi').src = ","").replace("/play.php?","https://phimmoi9.net/play.php?").replace("'","")
        except:
            src1 = ''
        src1s.append(src1)
        
        try:
            src2 = driver.find_element(by="xpath",value='//*[@id="go-server"]/center/ul/li/ul/li/a[2]').get_attribute("onclick")
            src2 = src2.replace("document.getElementById('phimmoi').src = ","").replace("/play.php?","https://phimmoi9.net/play.php?").replace("'","")
        except:
            src2 = ''
        src2s.append(src2)
        
        try:
            src3 = driver.find_element(by="xpath",value='//*[@id="go-server"]/center/ul/li/ul/li/a[3]').get_attribute("onclick")
            src3 = src3.replace("document.getElementById('phimmoi').src = ","").replace("/play.php?","https://phimmoi9.net/play.php?").replace("'","")
        except:
            src3 =''
        src3s.append(src3)
        
        
    
my_dict = {'name': names, 'slug': slugs, 'link': links, 'src1': src1s,'src2':src2s, 'src3':src3s, 'desc': descs, 'year': years, }
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('movie_title_100_detail.csv')

driver.quit()
