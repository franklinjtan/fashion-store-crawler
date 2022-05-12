#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Created By: Franklin Tan
# Created Date: 05/10/2022
# Version = '1.0'
# --------------------------------------------------
"""
Program Description:
The application crawls the online fashion website https://www.reformation.com
and scrapes the following information:
- display_name, product_material, color, size, price, product_url, image_links,
brand_name, description, scraped_date, and category.

The extracted information is then structured and stored in a hosted PostGRES database
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep
import psycopg2
import os

# Using Chrome Driver aligned with my Google Chrome Version 101.0.4951.54
PATH = "C:\Program Files (x86)\chromedriver.exe"
data = []


def get_chromedriver():
    driver = webdriver.Chrome(PATH)
    return driver


def get_links():
    url = "https://www.thereformation.com/clothing"
    driver = get_chromedriver()
    driver.get(url)

    # Derive the number of product links that appear
    links = driver.find_elements(By.XPATH, '//div[@class="product-tile__quickadd"]/div/a')
    return links


def get_database_connection():
    DB_ENDPOINT = 'database-2.csoidnby0uk5.us-east-1.rds.amazonaws.com'
    DB_NAME = "Reformation_db"
    DB_USER = "postgres"
    DB_PASS = os.environ.get('DB_PASS')
    DB_PORT = "5432"
    DB_REGION = 'us-east-1b'
    os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

    try:
        connection = psycopg2.connect(dbname=DB_NAME,
                                      user=DB_USER,
                                      host=DB_ENDPOINT,
                                      password=DB_PASS,
                                      port=DB_PORT)
        return connection
    except Exception as e:
        print("Database connection failed due to {}".format(e))


def main():
    links = get_links()
    # Counter = 10 - unique id already exists due to a previous run and...
    # Using counter for primary key in db. Counter needs to be updated.
    counter = 10
    for link in links:

        counter += 1
        current_url = (link.get_attribute('href'))
        driver = get_chromedriver()
        driver.get(current_url)
        sleep(2)

        # DISPLAY NAME
        product_title = driver.find_element(By.XPATH, '//h1').text

        # PRODUCT MATERIAL
        product_material_find = driver.find_elements(By.XPATH, '//div[@class="margin-b--15"]')
        product_materials_list = [y.get_attribute('innerHTML') for y in product_material_find]
        product_material = " ".join(list(map(lambda z: z.strip(), product_materials_list)))

        # COLOR
        color_list = driver.find_elements(By.XPATH,
                                          '//div[@class="product-attribute__contents flex flex-flow-wrap"]/button/span[@class="sr-only"]')
        colors = ", ".join([x.text.split(':')[1] for x in color_list])

        # SIZE
        size_list = driver.find_elements(By.XPATH,
                                         '//div[@class="product-attribute__contents flex flex-flow-wrap"]/button[@class="product-attribute__anchor anchor--size  selectable "]')
        sizes = [x.text for x in size_list]

        # PRICE
        price = driver.find_element(By.XPATH, '//span[@class="price--reduced"]').text

        # IMAGE LINKS
        image_list = driver.find_elements(By.XPATH, '//div[@data-test="img-zoom-wrap"]/img')
        image_url = [x.get_attribute("src") for x in image_list]

        # BRAND NAME
        brand_name = "Reformation"

        # PRODUCT DESCRIPTION
        product_description = driver.find_elements(By.XPATH, '//div[@class="cms-generic-copy"]')[0].text

        # Scraped Date
        date_today = date.today().strftime("%m/%d/%Y")

        # CATEGORY
        category = driver.find_elements(By.XPATH, '//a[@class="breadcrumbs__anchor link link--secondary"]')[1].text

        connection = get_database_connection()
        cur = connection.cursor()

        cur.execute(
            """
            INSERT INTO reformation_db(id,Display,Product_material,Colors, Size, Price, Product_image, 
            Image_links, Brand_name, Description, Scraped_date, Category) VALUES
            (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)
            """,
            (counter,
             str(product_title),
             str(product_material),
             str(colors), (sizes),
             str(price),
             str(current_url), (image_url), str(brand_name), str(product_description), str(date_today),
             str(category)))
        connection.commit()

        data.append({
            "Primary Key": counter,
            "Display Name": product_title,
            "Product Material": product_material,
            "Color": colors,
            "Size": sizes,
            "Price": price,
            "Product URL": current_url,
            "Image Links": image_url,
            "Brand Name": brand_name,
            "Description": product_description,
            "Scraped Date": date_today,
            "Category": category
        })

        driver.quit()
        if counter == 20:
            break
    print(data)


if __name__ == '__main__':
    main()