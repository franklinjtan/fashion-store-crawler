import psycopg2
import os

DB_ENDPOINT = 'database-2.csoidnby0uk5.us-east-1.rds.amazonaws.com'
DB_NAME = "Reformation_db"
DB_USER = "postgres"
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = 5432
DB_REGION = 'us-east-1b'
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

try:
    connection = psycopg2.connect(dbname=DB_NAME,
                                  user=DB_USER,
                                  host=DB_ENDPOINT,
                                  password=DB_PASS,
                                  port="5432")
    cur = connection.cursor()
    postgres_query = "SELECT * FROM reformation_db"

    cur.execute(postgres_query)
    records = cur.fetchall()
    print('Fetching')

    for row in records:
        print(row)
    # cur.execute("""
    # CREATE TABLE reformation_db(
    # id SERIAL PRIMARY KEY ,
    # Display varchar(5000),
    # Product_material varchar(5000),
    # Colors varchar(5000),
    # Size varchar(5000),
    # Price varchar(5000),
    # Product_image varchar(5000),
    # Image_links varchar(5000),
    # Brand_name varchar(5000),
    # Description varchar(5000),
    # Scraped_date varchar(5000),
    # Category varchar(5000)
    # )
    # """)
    connection.commit()
except Exception as e:
    print("Database connection failed due to {}".format(e))
