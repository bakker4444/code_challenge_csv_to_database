import os
import csv

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs

from dotenv import load_dotenv
from pprint import pprint

from table_info import Table
from row import Row

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


    # Connect newly created database
    conn_param["database"] = dbname
    with psycopg2.connect(**conn_param) as conn:
        conn.autocommit = True
        print("Database connected...")

        with conn.cursor() as cur:
            # Table information saved for data entry
            tb_info = Table()

            # Table create
            cur.execute("CREATE TABLE IF NOT EXISTS %s();", (AsIs(conn_param["database"]),))
            print("Table created...")

            # Column Info added to the table
            with open("./data_drop/schema.csv", "r") as schema_file:
                csv_reader = csv.reader(schema_file)

                # passing first row
                next(csv_reader)

                for line in csv_reader:
                    # Table information saved for data entry
                    tb_info.add_col_info(line)

                    """
                    Currently support column data type : CHAR, INTEGER, BOOLEAN
                    TODO : need to add different column data type for general usages
                    (eg. data, time, real, uuid, ...)
                    """
                    if line[2] == "CHAR":
                        cur.execute(sql.SQL("""
                                ALTER TABLE {}
                                ADD COLUMN %s %s (%s);
                            """).format(sql.Identifier(conn_param["database"])),
                            (AsIs(line[0]), AsIs(line[2]), AsIs(line[1])))
                    elif line[2] == "INTEGER" or line[2] == "BOOLEAN":
                        cur.execute("""
                                ALTER TABLE %s
                                ADD COLUMN %s %s;
                            """,
                            ( AsIs(conn_param["database"]), AsIs(line[0]), AsIs(line[2]) )
                        )
                    conn.commit()
                    print("Column generated...")
                print("Column entry finished")

            # Data entry
            with open("./data_drop/data.csv", "r") as data_file:
                csv_reader = csv.reader(data_file)

                for line in csv_reader:
                    data = Row(line)
                    data.data_mod(tb_info.get_col_type(), tb_info.get_col_width())

                    cur.execute(
                        sql.SQL("""
                                INSERT INTO {}
                                VALUES ({});
                            """.format(
                                conn_param["database"],
                                sql.SQL(", ").join(sql.Placeholder() * tb_info.get_num_of_cols()).as_string(conn)
                            )
                        ), data.get_data()
                    )
                    conn.commit()
                print("Data entry finished...")

    print("DB generation finished...")


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