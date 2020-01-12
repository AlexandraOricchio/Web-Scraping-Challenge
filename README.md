# Web-Scraping-Challenge

In this assignment, I built a web application that scrapes various websites for data related to Mars and displayed the information in a single HTML page

### Repository Guide:
- **mission_to_mars.ipynb:** jupyter notebook file with script for scraping and analysis 
- **scrape_mars.py:** python script with functions to execute data scrape and store the results into a python dictionary. 
- **app.py:** python script for flask application. Application includes routes that call my scrape function, stores the returned values into MongoDB, queries MongoDB and passes data into a HTML template. 
- **_templates:_**
    - **index.html:** HTML document displaying data passed from python application. 
- **_html_page_screenshots:_**
    - **html_page1.png, html_page2.png, html_page3.png, html_page4.png:** screenshots of final HTML page.
