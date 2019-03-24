# Back-End Code Challenge


## Problem Details

Your application should expect two associated `.csv` files to be dropped into a folder. One file will be called `schema.csv` and will describe the schema of the table we will create. The other file will be called `data.csv` and will contain a comma-separated list of data points to be injected into that table.

<br />

## Example

- /data_drop/schema.csv:
```
field name,width,datatype
author_name,10,CHAR
is_alive,1,BOOLEAN
books_authored_count,2,INTEGER
```

The schema.csv file will always contain a header with three columns that describe the field name, width, and data type. After the header, the schema csv file could contain any number of rows that describe the fields to be added to the table.

<br />

- /data_drop/data.csv:
```
Michael Crichton,1,28
Ernest Hemingway,0,13
J.K. Rowling,1,9
Stephen King,0,54
Mark Twain,0,103
```

The data.csv file will contain any number of rows should fit the table schema and will be ingested into the table.

<br />

- Output:

Taking the example above, the table and the data injected into it should look like:
```
author_name      | is_alive | books_authored_count| 
---------------- | -------- | --------------------|
Michael Crichton | True     | 28                  |        
Ernest Hemingway | False    | 13                  |
J.K. Rowling     | True     | 9                   |
Stephen King     | False    | 54                  |
Mark Twain       | False    | 03                  |
```

- Expectations
1. Database type and connection mechanism is left to your discretion.
2. If time permits, we would love to see tests that at least cover the example given.
3. Files can be assumed to use UTF-8 encoding
4. You should be prepared to discuss implementation decisions and possible extensions to your application.

<hr />

<br /><br /><br />


# Solution

## Configuration
<hr />

## 1. Database Setup
Run a PostgreSQL docker container  

### Container Info
- name : postgres-0
- password : password (**SET YOUR PASSWORD**, for this particular example, I will using just "password" )
- detached mode
- port : 5432

```
docker run --name postgres-0 -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
```

## 2. .env File Setup

make a file named ".env". Information on .env file is for postgresql environment variables. For this particular example, I will use the information shown on the below. **Change the parameters on your discretion.**

```
PG_HOST=localhost
PG_PORT=5432
PG_DB=test_db
PG_USER=postgres
PG_PW=password
```

## 3. schema.csv file and data.csv on data_drop folder

make a folder named "data_drop". schema.csv file and data.csv file locates on this folder. I will use the example shown on the description.


## 4. Virtual Environment Setup

I use the virtualenv package for setup python version. I use python 3.7.2 version for this particular example.

* setup virtualenv & activate the environment
```
virtualenv venv --python=python3.7
source ./venv/bin/activate
```

* (cf) Deactivate the environment
```
deactivate
```

## 5. (Required) Python Package Install

- psycopg2
- python-dotenv

I used two packages, psycopg2 for PostgreSQL, and python-dotenv for setting up the environments.

```
pip install -r requirements.txt
```

<br /><br />

<hr />

# Running Script

<br />

## 1. Convert input files to database
run python file with run argument
```
python main.py run
```

<br /><br />

## 2. Getting all data from DB
(additional feature - debugging purpose)  

```
python main.py get_all
```


<br /><br />

<hr />

# Future works
- Additional column data type support
  - currently available data type : CHAR, INTEGER, BOOLEAN
- Add logging feature instead print statements



<br /><br />

<hr />

# Questions

* COLUMN WIDTH on "schema.csv" file
  - "author_name" column width is 10, however output shows more than 10 characters. Output shown on the description seems wrong?
  - "books_authored_count" column width is 2, and output shows two digits. How to cut or limit the integer data?
  - NEED more detail description or clarifications.

