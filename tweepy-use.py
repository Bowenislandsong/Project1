import  tweepy
import  json
import subprocess
import  wget
import sys
import os
import  shutil
import io
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from urllib import request


def add_text(u,fn):

    im = Image.open('D:/photos/images/'+fn+'.jpg').convert('RGBA')

    words = Image.new('RGBA', im.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 40)
    d = ImageDraw.Draw(words)
    # draw text, half opacity
    xx=1
    for i in u:

        d.text((100,xx*70 ), i, font=fnt, fill=(255, 255, 255, 128))
        out = Image.alpha_composite(im, words)
        xx=xx+1
    out.show()
    im=out.convert("RGB")
    im.save(fn+'.png')




def google_vision(figure_number,num):
    # verify the API
    verify_api = vision.ImageAnnotatorClient()
    # add some images
    filepath = "D:/photos/images"
    fn=str(figure_number)
    if num>10:
        if int(fn)<10:
            fn='0'+fn

    image_used = os.path.join(filepath, fn+'.jpg')

    # load the photos
    images = io.open(image_used, 'rb').read()
    image = types.Image(content=images)
    # detect the label
    outcome = verify_api.label_detection(image=image)
    text = outcome.label_annotations
    u = []
    for k in text:
        print(k.description)
        u.append(k.description)

    add_text(u, fn)

def API_verify():
    consumer_key = 'mw5qwkQaBjvw99F2pNF9R3Ht8'
    consumer_secret = '9ESeJIDYx3BXS15yYEbxtOqakFVxGJdoEWQ2Xg5h4d2eIcTnqy'
    access_token = '1038768523366019074-0jW1slz19e304mGsTTMNSqjx0NM2s7'
    access_token_secret = 'hlmCDhNAeNbx8zv1dUXUnamqhB1XI1Svd4xFGqjy83U0j'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return (api)

def Twitter_Photos(api):
    tweets = api.home_timeline()
    for tweet in tweets:
        print(tweet.text)

    name = input('user screen name:')
    tweets = api.user_timeline(screen_name=name, count=20)

    url = []
    for items in tweets:

        if items.entities.__contains__('media') == 0:
            continue

        media_class = items.extended_entities.get('media')
        for sth in media_class:
            if sth['type'] != 'photo':
                continue
            # print(type(items))

            print('$$$', sth['media_url'], '$$$')
            url.append(sth['media_url'])

    for i in url:
        print(i)
        photos = wget.download(i)
        # equest.urlretrieve(i,'image',)
        file = open('tweet', 'w')
        for status in tweets:
            json.dump(status._json, file, sort_keys=True, indent=4)
        file.close()
    x = 1
    num = len(url)
    print('^^^^&^&^&^&',num)
    if os.path.exists('D:\photos\images') == 0:
        os.makedirs('D:\photos\images', mode=0o777)
    for files in os.listdir('D:\photos'):
        print(files)
        if files == 'tweepy-use.py':
            continue
        if files == 'tweet':
            continue
        if files == 'images':
            continue

        if num < 10:
            x = str(x)
            # os.rename(files,'0'+x+'.jpg')
            if os.path.exists('D:\photos\images\\'+x+'.jpg') == 0:
                os.rename(files, x + '.jpg')
            else :
                os.remove('D:\photos\images\\'+x+'.jpg')
                os.rename(files, x + '.jpg')
            # shutil.move("D:\\photos\\"+'0'+x+'.jpg',"D:\\photos\\images")
            shutil.move("D:\\photos\\" + x + '.jpg', "D:\\photos\\images")

        else:
            if x < 10:
                x = str(x)
                if os.path.exists('D:\photos\images\\'+'0'+x+'.jpg') == 0:
                    os.rename(files, '0' + x + '.jpg')
                else:
                    os.remove('D:\photos\images\\' +'0'+ x + '.jpg')
                    os.rename(files, '0' + x + '.jpg')
                # os.rename(files, x + '.jpg')
                shutil.move("D:\\photos\\" + '0' + x + '.jpg', "D:\\photos\\images")
                #shutil.move("D:\\photos\\" + x + '.jpg', "D:\\photos\\images")
            else:
                x = str(x)
                if os.path.exists('D:\photos\images\\' + x + '.jpg') == 0:
                    os.rename(files, x + '.jpg')
                else:
                    os.remove('D:\photos\images\\' + x + '.jpg')
                    os.rename(files, x + '.jpg')
                shutil.move("D:\\photos\\" + x + '.jpg', "D:\\photos\\images")

        x = int(x)
        x = x + 1
    return (num)




# mian function
api=API_verify()

num=Twitter_Photos(api)

for i in range(num):
    f=i+1
    google_vision(f,num)


if num<10:
    os.system("ffmpeg -r 0.5 -i %01d.png  video.avi")
else:
    os.system("ffmpeg -r 0.5 -i %001d.png  video.avi")







