import  tweepy
import  json
import subprocess
import  wget
import sys
import os
import  shutil

from urllib import request



consumer_key = 'mw5qwkQaBjvw99F2pNF9R3Ht8'
consumer_secret = '9ESeJIDYx3BXS15yYEbxtOqakFVxGJdoEWQ2Xg5h4d2eIcTnqy'
access_token = '1038768523366019074-0jW1slz19e304mGsTTMNSqjx0NM2s7'
access_token_secret='hlmCDhNAeNbx8zv1dUXUnamqhB1XI1Svd4xFGqjy83U0j'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

tweets=api.home_timeline()
for tweet in tweets:
    print(tweet.text)

name=input('user screen name:')
tweets = api.user_timeline(screen_name=name,count=5)

url=[]
for items in tweets:

    if items.entities.__contains__('media')==0:
        continue

    media_class = items.extended_entities.get('media')
    for sth in media_class:
        if sth['type']!='photo':
            continue
        #print(type(items))

        print('$$$', sth['media_url'], '$$$')
        url.append(sth['media_url'])


for i in url:
    print(i)
    photos=wget.download(i)
    #equest.urlretrieve(i,'image',)
    file = open('tweet', 'w')
    for status in tweets:
        json.dump(status._json, file, sort_keys=True, indent=4)
    file.close()
x=1
if os.path.exists('D:\photos\images')==0:
    os.makedirs('D:\photos\images',mode=0o777)
for files in  os.listdir('D:\photos'):
    print(files)
    if files=='tweepy-use.py':
        continue
    if files=='tweet':
        continue
    if files=='images':
        continue
    if x<10:
        x=str(x)
        #os.rename(files,'0'+x+'.jpg')
        os.rename(files,x + '.jpg')
        #shutil.move("D:\\photos\\"+'0'+x+'.jpg',"D:\\photos\\images")
        shutil.move("D:\\photos\\"+x + '.jpg', "D:\\photos\\images")
    else:
        x = str(x)
        os.rename(files,x + '.jpg')
        shutil.move("D:\\photos\\"+x + '.jpg', "D:\\photos\\images")
    x=int(x)
    x=x+1
os.system("ffmpeg -r 0.5 -i images/%01d.jpg  video.avi")


