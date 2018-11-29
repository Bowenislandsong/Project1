# Project3 database（only for windows system now）
This mini-project is a database api which is used by Twitter+FFMPEG+Google api (project1).
The basic functions include:

<1>storing all addresses and tags of each photo downloaded by Twitter+FFMPEG+Google api.

<2>searching the photos which have specific description word. 

<3>showing the LOG of using Twitter+FFMPEG+Google api and the most popular descriptor.

<4>All of functions are achieved by both  mongoDB and mysql database.

# Introduction and essential libraries
This api used some libraries which should be installed before:

python libraries: MySQLdb, pymongo and all libraries of Twitter+FFMPEG+Google api (project1)

database service: mongoDB and mysql

The database api include database_mysql.py, mongodb_store.py and Password.py three python files. database_mysql.py includes all functions which are implemented by mysql database, mongodb_store.py includes all functions which are implemented by mongodb database, and Password.py is used to save username and password of mysql\mongodb.

# beginning
Firstly, if you want to use this api to store the data from Twitter+FFMPEG+Google api, you should open mongodb and mysql database server first or the program will be stuck until time out.

Then use cmd line 'python tweepy-use.py' in root directory of mini-project3 to run tweepy-use.py (which is the main program of project1). If everything goes well, you could see the outcome as presented by the following picture.
![draw](https://github.com/plantclassification/seedlings_classification/blob/master/arch.jpeg)




So, please let me know if you face any problem when you use this program especially for TA and professor.

contact: lihaooo@bu.edu
