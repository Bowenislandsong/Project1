import os
import  pymongo
import  time
import Password
# use mongod first
def mongodb_log(query, tweet_number, photo_number, image_location, video_location):
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    except:
        print('did you open mongodb service?')
    a=time.asctime()
    #insert a conllection
    db = myclient.tweet
    collection = db.LOG
    student = {
        '_id': '%s'%(a),
        'inquiry': '%s'%(query),
        'tweet_number': '%d'%(tweet_number),
        'photo_number': '%d'%(photo_number),
        'image_location': '%s' % (image_location),
        'video_location': '%s' % (video_location),
        'username': '%s' % (Password.mongodb_name)
    }

    collection.insert_one(student)

def mongodb_data(photo_location,photo_name, labels):
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    except:
        print('did you open mongodb service?')
    a = time.asctime()
    db = myclient.tweet
    collection = db.data
    data = {
        '_id': '%s'%(a),
        'photo_location': '%s'%(photo_location),
        'photo_name': '%s'%(photo_name),
        'labels': '%s' % (labels)
    }
    collection.insert_one(data)


def mongodb_most():
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    except:
        print('did you open mongodb service?')

    dblist = myclient.list_database_names()
    # dblist = myclient.database_names()
    #for i in dblist:
        #print(i)
    db = myclient.tweet
    collection = db.data

    temp_string = ''
    for x in collection.find({}, {"_id": 0, "labels": 1}):
        #print(x['labels'])
        # print(x['labels'])
        temp_string = temp_string + ','+x['labels']
    #print(temp_string)
    fq = temp_string.split(',')
    #print(fq)
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

def mongodb_find(find_word):
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    except:
        print('did you open mongodb service?')
    db = myclient.tweet
    collection = db.data
    big_flag=0
    for x in collection.find():
        fq = x['labels'].split(',')
        #print(fq)
        flag=0
        for j in fq:
            if j==find_word:
                flag=1
                big_flag=1

        if flag==1:
            print(x)

    if big_flag==0:
        print('seems no session include '+find_word)


def mongodb_show_log():
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    except:
        print('did you open mongodb service?')
    db = myclient.tweet
    collection = db.LOG

    for x in collection.find():
        print(x)

def mongodb_show_all():
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    except:
        print('did you open mongodb service?')
    db = myclient.tweet
    collection = db.data

    for x in collection.find():
        print(x)



#mongodb_show_all()
#mongodb_most()





















