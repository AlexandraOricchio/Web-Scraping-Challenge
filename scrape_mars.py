from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # NASA MARS NEWS
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(1)

    soup= BeautifulSoup(browser.html, "html.parser")
    
    # get lisst of news articles and pull most recent title and text
    results = soup.find_all('li', class_="slide")
    latest_news=results[0]
    title=latest_news.find("div", class_="content_title").text
    text=latest_news.find("div", class_="article_teaser_body").text

    # create dictionary with results 
    scrape_results = {
        "news_title":title,
        "news_text":text
    }

    # JPL MARS SPACE IMAGE FEATURED
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    browser.click_link_by_partial_text('FULL')
    time.sleep(1)

    soup = BeautifulSoup(browser.html, 'html.parser')

    # find featured image and save url to variable
    image=soup.find_all('img', class_="fancybox-image")
    img_src=image[0]['src']
    ft_image_url = 'https://www.jpl.nasa.gov' + img_src

    # add results to scrape dictionary
    scrape_results["ft_image_url"]=ft_image_url

    # MARS WEATHER
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    time.sleep(1)

    soup = BeautifulSoup(browser.html, 'html.parser')

    # find recent tweet and save text as variable
    tweets=soup.find_all('div', class_='js-tweet-text-container')
    mars_weather=tweets[0].find('p').text
    mars_weather = mars_weather.replace('\n', ', ')

    # add to results dictionary
    scrape_results['mars_weather']=mars_weather

    # MARS FACTS
    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)
    time.sleep(1)

    # scrape for tabular data, take first table, clean & convert to html table
    dfs = pd.read_html(url4)
    mars_facts = dfs[0]
    mars_facts=mars_facts.rename(columns={0:'Description', 1:'Value'})
    mars_facts=mars_facts.set_index("Description")
    html_table=mars_facts.to_html()
    html_table=html_table.replace('\n', '')

    # add to results dictionary 
    scrape_results['mars_table']=html_table

    # MARS HEMISPHERES
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    time.sleep(1)

    soup = BeautifulSoup(browser.html, 'html.parser')

    # find hemispheres and loop to get each hemispheres title and image url
    results = soup.find_all('div', class_='description')
    hems_imgs = []
    for result in results:
        browser.visit(url5)
    
        a=result.find('a')
        title=a.find('h3').text
    
        browser.click_link_by_partial_text(title)
        browser.click_link_by_partial_text('Open')
        soup = BeautifulSoup(browser.html, 'html.parser')
        img = soup.find_all('img', class_='wide-image')
        img_src = img[0]['src']
        img_url = 'https://astrogeology.usgs.gov' + img_src
    
        hems={'title':title, 'image_url':img_url}
        hems_imgs.append(hems)

    # add to results dictionary 
    scrape_results['hems_imgs']=hems_imgs

    print(scrape_results)

    # Close the browser after scraping
    browser.quit()

    # Return results
    return scrape_results