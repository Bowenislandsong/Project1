import MySQLdb
import time
def mysql(query,tweet_number,photo_number,image_location,video_location):

    try:
        #db = MySQLdb.connect("localhost", "root", "", "TESTDB", charset='utf8' )
        db = MySQLdb.connect("localhost", "root", "", charset='utf8')
        cursor = db.cursor()
        cursor.execute('create database if not exists TWEET')                 #create a new database TWEET to store data
    except:
        print('there are something wrong when create the new database')


    # switch to the new database
    try:
        cursor.execute('use TWEET')
        print('ok')
        flag_tb=0
        #cursor.execute("DROP TABLE IF EXISTS LOG")
        cursor.execute('show tables')
        rows = cursor.fetchall()
        for row in rows:
            if len(rows)==0:
                break
            tbname = "%2s" % row
            if tbname=='log':
                flag_tb=1
        print(flag_tb)
        if flag_tb!=1:
            sql = """create TABLE LOG (
                     DATE  CHAR(60) NOT NULL,
                     INQUIRY  CHAR(60),
                     TWEET_NUMBER INT,  
                     PHOTO_NUMBER INT,
                     IMAGES_LOCATION CHAR(60),
                     VIDEO_LOCATION CHAR(60) )"""
            cursor.execute(sql)
            print('A new table has been created')

    except:
        print('no new database is created')
    a=time.asctime()
    sql = "INSERT INTO LOG(DATE,INQUIRY,\
             TWEET_NUMBER, PHOTO_NUMBER, IMAGES_LOCATION, VIDEO_LOCATION)\
             VALUES ('%s','%s', '%d', '%d', '%s', '%s')"%(a,query,tweet_number,photo_number,image_location,video_location)
    cursor.execute(sql)
    db.commit()




    db.close()