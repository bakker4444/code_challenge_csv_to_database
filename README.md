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
