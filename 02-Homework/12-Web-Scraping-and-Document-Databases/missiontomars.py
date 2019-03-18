from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd
from datetime import datetime
# https://splinter.readthedocs.io/en/latest/drivers/chrome.html

def init_db():
    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    return db

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return Browser("chrome", **executable_path, headless=False)

def init_db():
    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    return db

def create_soup(url):
    # URL of page to be scraped
    browser = init_browser()
    browser.visit(url)
    soup = BeautifulSoup(browser.html,"html.parser")

    return soup

def get_mars_news():
    url = 'https://mars.nasa.gov/news/'
    soup = create_soup(url)
    title = soup.find("div",class_ = "content_title").text
    body = soup.find("div", class_="article_teaser_body").text
    return{
    (f"Title: {title}"),
    (f"Para: {body}")
    }

def get_MARS_image():
    JPL_home_url = "https://www.jpl.nasa.gov"
    JPL_img_url = JPL_home_url+"/spaceimages/?search=&category=Mars"
    jpl_soup = create_soup(JPL_img_url)
    items = jpl_soup.find("div",{"class":"carousel_items"})
    img_title = items.find("h1",{"class":"media_feature_title"})
    featured_img = items.find("article")
    img_url = JPL_home_url+featured_img['style'].split(':')[1].split('\'')[1]
    return {
            "title":img_title,
            "img_url":img_url
           }
    
def get_mars_weather():
    url_weather = "https://twitter.com/marswxreport?lang=en"
    soup = create_soup(url_weather)
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
  #  return(mars_weather) 

#Visit the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.
def get_mars_facts():
    url_weather = "https://space-facts.com/mars/"
    table = pd.read_html(url_weather)
    # this is to ensure that we get the first table.
    df = table[0]
    df.columns =["Parameter","Value"]
    df.set_index(["Parameter"])
    table[0]
    new_html_table = df.to_html()
    return(new_html_table)

def get_MARS_hemisphere_data():
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    soup = create_soup(url)
    items = soup.find("div",{"id":"product-section"}).find_all("div",{"class":"item"})
    hemisphere_data = []
    for item in items:
        print(item)
        img_main_url = "https://astrogeology.usgs.gov"+item.find("a")["href"]
        img_title = item.find("div",{"class":"description"}).find("a").find("h3").text
        img_soup = create_soup(img_main_url)
        download_item = img_soup.find("div",{"class":"downloads"})
        hemisphere_item = {
            "title":img_title,
            "img_url": download_item.find("li").find("a")["href"]
        }
        hemisphere_data.append(hemisphere_item)
        
    return hemisphere_data

def scrape():
    mars_news = get_mars_news()
    mars_img = get_MARS_image()
    mars_facts = get_mars_facts()
    mars_temp = get_mars_weather()
    mars_hm_data = get_MARS_hemisphere_data()
    #mars_hm_data = getValue()
    return {
        "date":datetime.now(),
        "news":mars_news,
        "featured_img":mars_img,
        "facts":mars_facts,
        "temperature":mars_temp,
        "hemisphere_data":mars_hm_data
    }
