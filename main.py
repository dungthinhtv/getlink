#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from flask import Flask, render_template, request,jsonify
from slugify import slugify



app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        
        path = "chromedriver"
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service)

        title = request.form['title']
        driver.get('https://phim1080.biz/xem-phim/' + slugify(title))
        
        try:
            src1 = driver.find_element(by="xpath",value='//div[@class="film-info-action"]/a[1]').get_attribute("data-link")
        except:
            src1 = ''
            
        try:
            src2 = driver.find_element(by="xpath",value='//div[@class="film-info-action"]/a[2]').get_attribute("data-link")
        except:
            src2 = ''
            
        try:
            src3 = driver.find_element(by="xpath",value='//div[@class="film-info-action"]/a[3]').get_attribute("data-link")
        except:
            src3 = ''
            
        driver.quit()
        
        links = [src1,src2,src3]

        
        return jsonify(links)
    
        
if __name__ == "__main__":
    app.run()