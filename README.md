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

Guarantee Twiiter+FFMPEG+Google api could work:https://github.com/lihaooo233/Project1/tree/master , especially add google certification (please rename it google.json) and tweet developer username and password.

The database api include database_mysql.py, mongodb_store.py and Password.py three python files. database_mysql.py includes all functions which are implemented by mysql database, mongodb_store.py includes all functions which are implemented by mongodb database, and Password.py is used to save username and password of mysql\mongodb.

# beginning
Firstly, open Password.py and iput your mysql username and password to 'username' and 'password' of Password.py(This is important). And please create a username for mongoDB and input it in 'mongodb_name'.

Secondly,if you want to use this api to store the data from Twitter+FFMPEG+Google api, you should open mongodb and mysql database server first or the program will be stuck until time out.

Then use cmd line 'python tweepy-use.py' in root directory of mini-project3 to run tweepy-use.py (which is the main program of project1). If everything goes well, you could see the outcome as presented by the following picture.

![index](https://github.com/lihaooo233/Project1/blob/database/pictures/picture1.jpg)


# Main functions

After beginning, you will see 3 options:

Function 1: Input neither 1 nor 2, the program will continue to ask you if you want to try Twitter+FFMPEG+Google, please at least use this function at least one time or database will not be created. All images and the video will be stored in a directory 'imageX' X is how many times you use Twitter+FFMPEG+Google function. After you first time using this function, a database named 'tweet' has been created by mongoDB and mysql. Besides, two tables(or collections) named 'LOG' and 'information' should have been created as well. Those are two tables(or collections) to record all informations about users and photos

Function 2：Input 1, The program will show all LOG informations from table(or collection) LOG. You could find who used this api and the details.Besides, you could also find the most popular descriptor here. All information come from both mongoDB and mysql.

![index](https://github.com/lihaooo233/Project1/blob/database/pictures/picture3.jpg)


Date: When this operation happend;

Inquiry: Photos are downloaded from this Tweet username.

Tweet number&photo number: how many tweets you wantted to find and how many photos are included.

Image location& Video location: Where are photos and video stored.

User/Username: Who did that, used mysql login name and mongoDB username (in Password.py)


Function 3: Input 2, you can search all photos which have the specific word in tag. Besides, you could input 'see_all' to find all photos have been stored.

![index](https://github.com/lihaooo233/Project1/blob/database/pictures/picture4.jpg)

You could find some details about all photos including when and where they are stored (date,location) and all tags from google vision(labels).

Or,input a key word, and you could find all photos which have this word in their tags.

![index](https://github.com/lihaooo233/Project1/blob/database/pictures/picture5.jpg)


# CONTACT


So, please let me know if you face any problem when you use this program especially for TA and professor.

contact: lihaooo@bu.edu
