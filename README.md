# Web-Scraping-Challenge

In this assignment, I built a web application that scrapes various websites for data related to Mars and displayed the information in a single HTML page. I completed the web scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

## Scraping: 
- **NASA Mars News:**
Collected the latest News Titles and paragraph text from [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest).

- **JPL Mars Space Images:**
Used splinter to navigate site for [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and captured current feautred image of Mars.

- **Mars Weather:**
Scraped the latest Mars weather from the [Mars Weather Twitter Account](https://twitter.com/marswxreport?lang=en).

- **Mars Facts:**
Used Pandas to scrape table of Mars facts from the [Mars Facts webpage](https://space-facts.com/mars/) and converted data to a HTML table string.

- **Mars Hemispheres:**
Obtained images for each of Mar's hemispheres from [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) and used Python dictionaries to store data.

## MongoDB & Flask Application: 
Used MongoDB with Flask templating and created a new HTML page that displays all of the information that was scraped from the URLs above. 

![html part 1](html_page_screenshots/html_page1.png)
![html part 2](html_page_screenshots/html_page2.png)

## Repository Guide:
- **mission_to_mars.ipynb:** jupyter notebook file with script for scraping and analysis.
- **scrape_mars.py:** python script with functions to execute data scrape and store the results into a python dictionary. 
- **app.py:** python script for flask application. Application includes routes that call my scrape function, stores the returned values into MongoDB, queries MongoDB and passes data into a HTML template. 
- **_templates:_**
    - **index.html:** HTML template displaying data passed from python application. 
- **_html_page_screenshots:_**
    - **html_page1.png, html_page2.png, html_page3.png, html_page4.png:** screenshots of final HTML page.
