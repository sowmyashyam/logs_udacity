# logs_analysis

* Psycopg2 is used as DB-API. Python is connected to "NEWS" database through "Psycopg2". News database contains 3 tables namely **articles, authors, logs**. The internal reporting tool is used to connect to the database to fetch various results.
* The log has a database row for each time a reader loaded a web page. 
* Python is used as frontend language. The program  won't take any input from the user. Instead, it will connect to the database, using SQL queries to analyze the data and to fetch the results of the queries.
* The tool runs three reports for the following queries:
* `1.What are the most popular three articles of all time?`
* `2.Who are the most popular article authors of all time?`
* `3.On which days did more than 1% of requests lead to errors?`
* We'll need to create database views for the reporting tool to work properly:
```sh
create view numviews_view as (select title, author, count(*) as num from articles,log where log.path=CONCAT('/article/',articles.slug) group by articles.title,articles.author order by num desc);
select * from numviews_view;
```
# Getting started:
### Python
1.Install [python] using the following url (https://www.python.org)<br>
2.Press the *dowload* tab and click **Download python 3.6.2**<br>
3.Run and install the python version
### Vagrant
### VirtualBox
# Prerequisites
* From the 'vagrant' directory, run vagrant up.
* When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
* Connect to the psql database with psql -d news.
# To Run
*Launch Vagrant VM and run the commands: vagrant up, and then vagrant ssh
*Load the data, using  the command 
```sh
psql -d news -f newsdata.sql.
```
* The database should contain three tables namely:
* `Authors table`
* `Articles table`
* `Log table`
4.Run the python script file
The results of the queries will be dispalyed.

# Authors
**Sowmya shyam** - Initial work

# License
Logs analysis is a educational perspective project. Feel free to do edit it if so needed.

