### **log_analysis**
log_analysis will create a report from a fictional news website database.

The database contains 3 tables, articles, authors, and log. The log file contains web server log information such as the response code and time of the http request.

The report will answer the following questions.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The report will be written to a file named "news_report.txt" in your current working directory.

### **Requirements**
log_analysis uses Vagrant and Virtualbox to provide a virtual machine for dev/testing purposes.

Git for Ubuntu
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
You can use the provided VM to test log_analysis. First we will clone this repository to our local workstation. Then we will use vagrant to provision a new VM with Postgresql and Python3 are preinstalled. Once the VM is running we can proceed to download, extract, and import the news database. We then use pip3 to install psycopg2. log_analysis is now ready for testing.

Clone repository from github  
`git clone https://github.com/txhc4life/log_analysis.git`

Change the directory to the shared vagrant directory  
`cd log_analysis/vagrant/`

Start the VM  
`vagrant up`

SSH into the VM  
`vagrant ssh`

Download the news database  
`wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip`

Extract the news database  
`unzip newsdata.zip`

Import the database into postgresql  
`psql -d news -f newsdata.sql`

Install psycopg2  
`pip3 install --user psycopg2-binary`

Change directory to shared synced folder
`cd /vagrant`

Execute   
`./log_analysis.py`

View report  
`cat news_report.txt`
