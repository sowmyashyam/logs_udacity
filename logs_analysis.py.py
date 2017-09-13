import psycopg2
dbname = "news"

# List of queries passed:

# What are the most popular three articles of all time?
query1 = ''' select title,count(*) as num from articles,log where
log.path=CONCAT('/article/',articles.slug) group by articles.title order by
num DESC limit 3; '''

# View is created named as count_view
view = '''create view count_view as (select title, author,
count(*) as num from articles,log
where log.path=CONCAT('/article/',articles.slug)
group by articles.title,articles.author order by num desc);'''

# To check the view
# select * from count_view;

# Who are the most popular  authors of all time?
query2 = ''' select authors.name, sum(count_view.num) as views from
count_view,authors where authors.id=count_view.author group by
authors.name order by views desc'''

# On which days did more than 1% of requests lead to errors?
query3 = '''select * from (select date(time),round(100.0*sum(case log.status
when '200 OK'  then 0 else 1 end)/count(log.status),3) as error from log group
by date(time) order by error desc) as subquery where error > 1;'''


def make_connection(query):
    '''Makes a connection to the database'''
    global conn
    conn = psycopg2.connect(dbname='news', user='postgres',
                            password='admin', port=5432)
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def popular_articles(query):
    '''The most popular three articles of all time'''
    output1 = make_connection(query)
    print('1.The most popular three articles of all time:')
    print(output1)


def popular_authors(query):
    '''The most popular authors of all time:'''
    output2 = make_connection(query)
    print('2.The most popular authors of all time:')
    print(output2)


def error_percentage(query):
    '''Days in which more than 1% of requests lead to errors'''
    output3 = make_connection(query)
    print('3.Days in which more than 1% of requests lead to errors:')
    print(output3)
    conn.close()

# Order of program execution
popular_articles(query1)
popular_authors(query2)
error_percentage(query3)

























