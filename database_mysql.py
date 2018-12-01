import MySQLdb
import time
import Password
import warnings
warnings.filterwarnings("ignore")
def mysql(query,tweet_number,photo_number,image_location,video_location):

    try:
        #db = MySQLdb.connect("localhost", "root", "", "TESTDB", charset='utf8' )
        db = MySQLdb.connect("localhost", Password.username, Password.password, charset='utf8')
        cursor = db.cursor()
        cursor.execute('create database if not exists TWEET')                 #create a new database TWEET to store data
    except:
        print('there are something wrong when create the new database')
        exit()


    # switch to the new database
    try:
        cursor.execute('use TWEET')
        #print('ok')
        flag_tb=0

        cursor.execute('show tables')
        rows = cursor.fetchall()
        for row in rows:
            if len(rows)==0:
                break
            tbname = "%2s" % row
            if tbname=='log':
                flag_tb=1

        if flag_tb!=1:                         #form of LOG
            sql = """create TABLE LOG (
                     DATE  CHAR(60) NOT NULL,
                     INQUIRY  CHAR(60),
                     TWEET_NUMBER INT,  
                     PHOTO_NUMBER INT,
                     IMAGES_LOCATION CHAR(60),
                     VIDEO_LOCATION CHAR(60),
                     USERNAME CHAR(60))"""
            cursor.execute(sql)


    except:
        print('There are some problems when create the LOG table')
    a=time.asctime()
    sql = "INSERT INTO LOG(DATE,INQUIRY,\
             TWEET_NUMBER, PHOTO_NUMBER, IMAGES_LOCATION, VIDEO_LOCATION,USERNAME)\
             VALUES ('%s','%s', '%d', '%d', '%s', '%s','%s')"%(a,query,tweet_number,photo_number,image_location,video_location,Password.username)
    cursor.execute(sql)
    db.commit()




    db.close()




def data_save(photo_location,photo_name, labels):         #save the labels of photos
    try:
        #db = MySQLdb.connect("localhost", "root", "", "TESTDB", charset='utf8' )
        db = MySQLdb.connect("localhost", Password.username, Password.password, charset='utf8')
        cursor = db.cursor()
        cursor.execute('create database if not exists TWEET')
    except:
        print('there are something wrong when create the new database')
        exit()

    try:
        cursor.execute('use TWEET')

        flag_tb=0

        cursor.execute('show tables')
        rows = cursor.fetchall()
        for row in rows:
            if len(rows)==0:
                break
            tbname = "%2s" % row
            if tbname=='information':
                flag_tb=1

        a = time.asctime()
        if flag_tb!=1:
            sql = """create TABLE information (
                     DATE  CHAR(60) NOT NULL,
                     photo_location  CHAR(60),
                     photo_name CHAR(60),
                     labels CHAR(250)   )"""
            cursor.execute(sql)
            #print('A new table has been created')

    except:
        print('There are some problems when create the information table')

    sql = "INSERT INTO information(DATE,photo_location,\
           photo_name, labels)\
           VALUES ('%s','%s','%s','%s')"%(a,photo_location,photo_name, labels)
    cursor.execute(sql)
    db.commit()
    db.close()

def mysql_most():            #use labels to find the most popular descriptor
    try:
        db = MySQLdb.connect("localhost", Password.username, Password.password, charset='utf8')
        cursor = db.cursor()
        cursor.execute('create database if not exists TWEET')
    except:
        print('seems database has not been created, please use Twitter+FFMPEG+Google at least once or did you open mysql service?')

    try:
        cursor.execute('use TWEET')
        flag_tb = 0
        cursor.execute('show tables')
        rows = cursor.fetchall()
        for row in rows:
            if len(rows) == 0:
                break
            tbname = "%2s" % row
            if tbname == 'information':
                flag_tb = 1
        if flag_tb==0:
            exit('seems no information table, please use Twitter+FFMPEG+Google at least once')

    except:
        print('something wrong happend please use Twitter+FFMPEG+Google at least once ')
        exit()

    sql = "SELECT * FROM information"
    all_labels=''
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        labels = row[3]

        all_labels=all_labels+','+labels

    fq = all_labels.split(',')

    # find the most popular descriptor
    index1 = 0
    max = 0
    for i in range(len(fq)):
        flag = 0
        for j in range(i + 1, len(fq)):
            if fq[i] == fq[j]:
                flag = flag + 1

        if flag > max:
            max = flag
            index1 = i
    print('the most popular descriptor is '+fq[index1])
    db.close()


def mysql_find(find_word):
    try:
        db = MySQLdb.connect("localhost", Password.username, Password.password, charset='utf8')
        cursor = db.cursor()
        cursor.execute('create database if not exists TWEET')
    except:
        print('seems database has not been created, please use Twitter+FFMPEG+Google at least once or did you open mysql service?')
        exit()

    try:
        cursor.execute('use TWEET')
        flag_tb = 0
        cursor.execute('show tables')
        rows = cursor.fetchall()
        for row in rows:
            if len(rows) == 0:
                break
            tbname = "%2s" % row
            if tbname == 'information':
                flag_tb = 1
        if flag_tb==0:
            exit('seems no information table, please use Twitter+FFMPEG+Google at least once')

    except:
        print('something wrong happend please use Twitter+FFMPEG+Google at least once ')
        exit()

    sql = "SELECT * FROM information"
    cursor.execute(sql)
    results = cursor.fetchall()
    big_flag=0
    for row in results:
        date = row[0]
        photo_location = row[1]
        photo_name = row[2]
        labels = row[3]
        fq='date: '+date,'photo_location： '+photo_location,' photo_name: '+photo_name,' labels: '+labels
        fp = labels.split(',')
        flag = 0
        for j in fp:
            if j==find_word:
                flag=1
                big_flag=1

        if flag==1:
            print(fq)

    if big_flag==0:
        print('seems no session include '+find_word)



    db.close()


def mysql_LOG():      # show all information of each operation before
    try:
        db = MySQLdb.connect("localhost", Password.username, Password.password, charset='utf8')
        cursor = db.cursor()
        cursor.execute('create database if not exists TWEET ')
    except:
        print('seems database has not been created, please use Twitter+FFMPEG+Google at least once or did you open mysql service?')
        exit()

    try:
        cursor.execute('use TWEET')
        flag_tb = 0
        cursor.execute('show tables')
        rows = cursor.fetchall()
        for row in rows:
            if len(rows) == 0:
                break
            tbname = "%2s" % row
            if tbname == 'log':
                flag_tb = 1
        if flag_tb==0:
            exit('seems no LOG table, please use Twitter+FFMPEG+Google at least once')

    except:
        print('something wrong happend please use Twitter+FFMPEG+Google at least once ')
        exit()

    sql = "SELECT * FROM LOG"
    cursor.execute(sql)
    results = cursor.fetchall()
    big_flag=0
    for row in results:
        date = row[0]
        inquery= row[1]    # download photos from this username(Twitter)
        tweet_number = str(row[2])  #how many tweet you want to search
        photo_number= str(row[3])   # how many photos are downloaded
        image_location=row[4]  # where the photos are downloaded
        video_location=row[5]  # where to find the final video
        User=row[6]  # user of database
        fq='date: '+date,'inquery： '+inquery,' tweet_number: '+tweet_number,' photo_number: '+photo_number,'image_location: '+image_location,'video_location: '+video_location,'User: '+User


        print(fq)




    db.close()

def mysql_all():    #show all information of photos
    try:
        db = MySQLdb.connect("localhost", Password.username, Password.password, charset='utf8')
        cursor = db.cursor()
        cursor.execute('create database if not exists TWEET')
    except:
        print('seems database has not been created, please use Twitter+FFMPEG+Google at least once or did you open mysql service?')
        exit()

    try:
        cursor.execute('use TWEET')
        flag_tb = 0
        cursor.execute('show tables')
        rows = cursor.fetchall()
        for row in rows:
            if len(rows) == 0:
                break
            tbname = "%2s" % row
            if tbname == 'information':
                flag_tb = 1
        if flag_tb==0:
            exit('seems no information table, please use Twitter+FFMPEG+Google at least once')

    except:
        print('something wrong happend please use Twitter+FFMPEG+Google at least once ')
        exit()

    sql = "SELECT * FROM information"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        date = row[0]
        photo_location = row[1]
        photo_name = row[2]
        labels = row[3]
        fq='date: '+date,'photo_location： '+photo_location,' photo_name: '+photo_name,' labels: '+labels

        print(fq)



    db.close()

