# logs_analysis
Postgresql
Psycopg2 is used a s DB-API. Python is connected to "NEWS" database through "Psycopg2". News database contains 3 tables namely articles, authors, logs. The internal reporting tool is used to connect to the database to discover what kind of articles the site's readers like.
The log has a database row for each time a reader loaded a web page. 
Python is used as frontend language. The program  won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some queries.
The tool runs three reports for the following queries:
1.What are the most popular three articles of all time?
2.Who are the most popular article authors of all time?
3.On which days did more than 1% of requests lead to errors?
# Getting started:
#Python
1.Install [python] using the following url (https://www.python.org)<br>
2.Press the *dowload* tab and click **Download python 3.6.2**<br>
3.Run and install the python version
#
