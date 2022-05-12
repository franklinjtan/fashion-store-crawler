# 👘👗Fashion Store Crawler
[![LinkedIn][https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555]][https://www.linkedin.com/in/franklinjtan/]

I created an application that crawls the fashion store brand [Reformation](https://reformation.com/) and extracts product information. 

## About the Project

A coding challenge was provided by [Changing Room](https://changingroom.eco/), a Honey extension for sustainable fashion that helps users track and reduce their environmental impact. The coding challenge features an application that crawls a fashion brand's website using a crawler framework (in this case Selenium), extracts information in a structured manner, and stores the data in a hosted database (AWS RDS).

Extracted information:
* display_name (str)
* product_material (str)
* color (str)
* size (list)
* price (str)
* product_url (str)
* image_links (list)
* brand_name (str)
* description (str)
* scraped_date (date)
* category (str)

## Process
* [x] Understand key objectives and deliverables
* [x] Research and study the structure of the website: [Reformation](https://reformation.com/)
* [x] Reading Selenium documentation and downloading the appropriate Web Driver with my Chrome version
* [x] Brainstorm/strategize/pseudocode for collecting extracted information and inserting into DB
* [x] Programming(using By.XPATH to find all clothing links to loop through)
* [x] Continue extracting information from the site, testing functions, and appending it to a dictionary
* [x] Creating an account on AWS, setting up AWS IAM User, and creating a DB with AWS RDS
* [x] Planning out a potential primary key for the database
* [x] Establishing database connection and setting up environment variables for DB_PASS
* [x] Inserting into reformation_db
* [x] SELECT * from reformation_db

## Addressing Strategy to Scrape Entire Website & Automatic Updates
> "By finding the appropriate xpath, '//div[@class="product-tile__quickadd"]/div/a', I was able to grab all the product links which enabled me to go through each product page and extract the necessary information. I think this strategy can be expanded to include all the critical pages of the site using [Beautiful Soup](https://www.geeksforgeeks.org/beautifulsoup-scraping-link-from-html/). 

> "I understand that the site structure can change which can be tricky, so finding a unique ID/primary would be necessary to keep track of new, old, or not available products. This is something I would look into more. I know for Amazon products, there is a unique identifier (ASINS) that can be used to track the stage of the product.

> "Lastly, with all the projected requests on the site, it is likely that an IP block will occur, so a proxy server would need to be purchased. 

## Information Extraction Example
```python
 product_material_find = driver.find_elements(By.XPATH, '//div[@class="margin-b--15"]')
 product_materials_list = [y.get_attribute('innerHTML') for y in product_material_find]
 product_material = " ".join(list(map(lambda z: z.strip(), product_materials_list)))
```


## Technologies
* [Selenium with Python](https://selenium-python.readthedocs.io/ "Selenium with Python Docs")
* [WebDriver with Selenium](https://www.selenium.dev/documentation/webdriver/)
* [PostgreSQL on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
* [Amazon Web Services](https://docs.aws.amazon.com/polly/latest/dg/setting-up.html)'

## Screenshots of Process
![Inspecting the Reformation Website](https://github.com/fjt7/fashion-store-crawler/blob/main/Reformation%20Website%20Structure.png)
![AWS RDS](https://github.com/fjt7/fashion-store-crawler/blob/main/AWS.JPG)

## Other Acknowledgements
* [Chrome Driver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/)
* [Getting Started with AWS RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)
* [Psycopg 2.9.3 documentation](https://www.psycopg.org/docs/cursor.html)
* [SQL using Python](geeksforgeeks.org/sql-using-python/)
* [Basic Date and Time Types](https://docs.python.org/3/library/datetime.html)

## License
[MIT](https://choosealicense.com/licenses/mit/)
