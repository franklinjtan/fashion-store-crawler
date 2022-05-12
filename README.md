# 👘👗Fashion Store Crawler

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


## Information Extraction Example
```python
 product_material_find = driver.find_elements(By.XPATH, '//div[@class="margin-b--15"]')
 product_materials_list = [y.get_attribute('innerHTML') for y in product_material_find]
 product_material = " ".join(list(map(lambda z: z.strip(), product_materials_list)))
```

## Usage

## Technologies
* [Selenium with Python](https://selenium-python.readthedocs.io/ "Selenium with Python Docs")
* [WebDriver with Selenium](https://www.selenium.dev/documentation/webdriver/)
* [PostgreSQL on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
* [Amazon Web Services](https://docs.aws.amazon.com/polly/latest/dg/setting-up.html)

## Screenshots of Process
![alt text](https://github.com/fjt7/fashion-store-crawler/blob/main/Reformation%20Website%20Structure.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
