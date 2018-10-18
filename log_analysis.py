#!/usr/bin/python3
"""Prints report from the news database."""
import psycopg2

print("Starting report.")

try:
    conn = psycopg2.connect("dbname=news")
except e:
    print("Could not connect to the database.")

cur = conn.cursor()
cur.execute("""
            SELECT title, COUNT(title) AS views
            FROM log, articles
            WHERE replace(path, '/article/', '')  = slug
            GROUP BY title
            ORDER BY count(title)
            DESC
            LIMIT 3;
            """)
top_articles = cur.fetchall()

cur.execute("""
            SELECT name, COUNT(title) AS views
            FROM authors, articles, log
            WHERE replace(path, '/article/', '')  = slug
            AND authors.id = articles.author
            GROUP BY name
            ORDER BY COUNT(title)
            DESC;
            """)
top_authors = cur.fetchall()

cur.execute("""
           SELECT date(time) AS time,
           (cast(COUNT(case when status = '404 NOT FOUND' then 1 end) AS float)
           / COUNT(case when status = '200 OK' then 1 end)) * 100 as percentage
           FROM log
           GROUP BY date(time)
           HAVING (cast(COUNT(case when status = '404 NOT FOUND' then 1 end)
           AS float) / COUNT(case when status = '200 OK' then 1 end))
           * 100 > 1.0;
           """)
days_with_errors = cur.fetchall()

cur.close()
conn.close()

with open("news_report.txt", "w") as report_file:
    print("Top Three Articles", file=report_file)
    print("-------------------", file=report_file)
    for i in range(len(top_articles)):
        print('"%s" - %s views' % (top_articles[i][0], top_articles[i][1]),
              file=report_file)

    print("", file=report_file)
    print("Most Popular Authors", file=report_file)
    print("---------------------", file=report_file)
    for i in range(len(top_authors)):
        print('%s - %s views' % (top_authors[i][0], top_authors[i][1]),
              file=report_file)

    print("", file=report_file)
    print("Days with more then 1% of errors", file=report_file)
    print("---------------------------------", file=report_file)
    for i in range(len(days_with_errors)):
        print('%s : %.1f%%' % (days_with_errors[i][0], days_with_errors[i][1]),
              file=report_file)

print("Report is finished.")
print("Filename: news_report.txt")
