import os
import csv

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs

from dotenv import load_dotenv
from pprint import pprint


def main():
    """
    Converting from csv files to postgres database
    Two file should be located on ./data_drop folder
    """

    load_dotenv()
    conn_param = {
        "host": os.getenv("PG_HOST"),
        "port": os.getenv("PG_PORT"),
        "user": os.getenv("PG_USER"),
        "password": os.getenv("PG_PW"),
    }
    dbname = os.getenv("PG_DB")

    # Environment setup
    with psycopg2.connect(**conn_param) as conn:
        conn.autocommit = True
    
        try:
            with conn.cursor() as cur:
                cur.execute("DROP DATABASE IF EXISTS {};".format(dbname))
                cur.execute("CREATE DATABASE {};".format(dbname))
                print("Test database environment setup complete...")
        except Exception as e:
            print("Error message: {}".format(e))



def get_data():
    """
    Additional feature.
    Easy to get data from database which created from main function
    """

    load_dotenv()
    conn_param = {
        "host": os.getenv("PG_HOST"),
        "port": os.getenv("PG_PORT"),
        "user": os.getenv("PG_USER"),
        "password": os.getenv("PG_PW"),
        "database": os.getenv("PG_DB")
    }


    with psycopg2.connect(**conn_param) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM %s;", (AsIs(conn_param["database"]),))
            data = cur.fetchall()
            pprint(data)



if __name__ == "__main__":
    
    if os.sys.argv[1] == "run":
        main()
    elif os.sys.argv[1] == "get_all":
        get_data()