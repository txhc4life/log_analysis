### **log_analysis**
log_analysis will create a report from a fictional news website database.

The database contains 3 tables. Articles, authors, and log. The log file contains web server log information such as the response code and time of the http request.

The report will answer the following questions.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The report will be written to a file named "news_report.txt" in your current working directory.

### **Requirements**
log_analysis uses Vagrant and Virtualbox to provide a virtual machine for dev/testing purposes.

Git  
`sudo apt-get install git`  
Git for Windows  
https://git-scm.com/download/win  
Vagrant  
https://www.vagrantup.com/downloads.html   
Virtualbox  
https://www.virtualbox.org/wiki/Downloads  
Python 3 - Included in VM  
https://www.python.org/downloads/  
Postresql - Included in VM  
https://www.postgresql.org/download/

### **Instructions**
Clone repository from github  
`git clone https://github.com/txhc4life/log_analysis.git`

Change the directory to the shared vagrant directory  
`cd log_analysis/vagrant/``

Start the VM  
`vagrant up`

SSH into the VM  
`vagrant ssh`

Change the directory to the shared vagrant directory  
`cd /vagrant/`

Import the database into postgresql  
`psql -d news -f newsdata.sql`

Install psycopg2  
`pip3 install --user psycopg2-binary`

Ensure the file is executable  
`chmod +x log_analysis.py`

Execute   
`./log_analysis.py`
