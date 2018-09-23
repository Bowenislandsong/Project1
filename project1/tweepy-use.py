#author:Hao Li
import  tweepy
import  json
import  wget
import os
import  shutil
import io
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ImageFont
from userkey import *


def add_text(u,fn):

    im = Image.open('images/'+fn+'.jpg').convert('RGBA')
    min_size =1000
    fill_color = (0, 0, 0, 0)
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    a = int(size - x)
    b = int(size - y)
    new_im.paste(im, (int(a / 2), int(b / 2)))

    words = Image.new('RGBA', new_im.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype('arial.ttf', 60)
    d = ImageDraw.Draw(words)
    # draw text
    xx = 1
    c = im.size[1] / 50
    c = int(c)

    for i in u:
        if(xx>c):
            break

        d.text((100,xx*40 ), i, font=fnt, fill=(235, 21, 200, 255))
        out = Image.alpha_composite(new_im, words)
        xx=xx+1

    im=out.convert("RGB")
    im.save(fn+'.jpg')
    shutil.move( fn + '.jpg', "video_image")



def google_vision(figure_number,num):
    # verify the API
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"
    verify_api = vision.ImageAnnotatorClient()

    # add some images
    filepath = "images"
    fn=str(figure_number)
    if num>=10:
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

        u.append(k.description)

    add_text(u, fn)

def API_verify():
# verify credential keys
    if consumer_key == '' or consumer_secret == '' or access_token == '' or access_token_secret =='':
        exit('please input your Twitter credential keys')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return (api)

def Twitter_Photos(api):
# input screen name and number
    name = input('please input user screen name:')
    tn=input('please input how many tweets you want to scan?(20-50):')
    tn=int(tn)
    if tn>50:
        print('the scan number:50(fixed)')
        tn=50
    elif tn<20:
        tn=20
        print('the scan number:20(fixed)')
    else:
        print('the scan number is:',tn)


# begain to scan
    try:
        tweets = api.user_timeline(screen_name=name, count=tn)

        url = []
        for items in tweets:

            if items.entities.__contains__('media') == 0:
                continue
# make sure the media is photo
            media_class = items.extended_entities.get('media')
            for sth in media_class:
                if sth['type'] != 'photo':
                    continue
                if len(url)>=99:
                    break
                url.append(sth['media_url'])

        num = len(url)
        for i in url:
            photos = wget.download(i)
            file = open('tweet.txt', 'w')
            for status in tweets:
                json.dump(status._json, file, sort_keys=True, indent=4)
            file.close()
        x = 1

# put photos into folder image
        if os.path.exists('images') == 0:
            os.makedirs('images', mode=0o777)
        for files in os.listdir():
            search = list(files)
            # select photos
            if search[-1] == 'g' and search[-2] == 'p' and search[-3] == 'j':
                if num < 10:
                    x = str(x)
                    if os.path.exists('images/' + x + '.jpg') == 0:
                        os.rename(files, x + '.jpg')
                    else:
                        os.remove('images\\' + x + '.jpg')
                        os.rename(files, x + '.jpg')
                    shutil.move(x + '.jpg', "images")

                else:
                    if x < 10:
                        x = str(x)
                        if os.path.exists('images\\' + '0' + x + '.jpg') == 0:
                            os.rename(files, '0' + x + '.jpg')
                        else:
                            os.remove('images\\' + '0' + x + '.jpg')
                            os.rename(files, '0' + x + '.jpg')
                        shutil.move('0' + x + '.jpg', "images")
                    else:
                        x = str(x)
                        if os.path.exists('images\\' + x + '.jpg') == 0:
                            os.rename(files, x + '.jpg')
                        else:
                            os.remove('images\\' + x + '.jpg')
                            os.rename(files, x + '.jpg')
                        shutil.move(x + '.jpg', "images")



                x = int(x)
                x = x + 1
        return (num)



    except:
        print('seems nobody has this name.... or something unknown happened')
        exit()





    # mian function
api=API_verify()

#remake folders to delete photos downloaded before
if os.path.exists('video_image') == 1:
    shutil.rmtree('video_image')

    os.makedirs('video_image', mode=0o777)
else:
    os.makedirs('video_image', mode=0o777)

if os.path.exists('images') == 1:
    shutil.rmtree('images')

    os.makedirs('images', mode=0o777)
else:
    os.makedirs('images', mode=0o777)
num=Twitter_Photos(api)
try:
    for i in range(num):
        f = i + 1
        google_vision(f, num)

    if os.path.exists('outcome.mp4') == 1:
        os.remove('outcome.mp4')

    if num < 10:
        os.system("ffmpeg -f image2 -framerate 0.5 -y -i video_image\%01d.jpg  -c:v libx264 -pix_fmt yuv420p outcome.mp4")

    else:
        os.system("ffmpeg -f image2 -framerate 0.5 -y -i video_image\%02d.jpg  -c:v libx264 -pix_fmt yuv420p outcome.mp4")
    if os.path.exists('outcome.mp4') == 0:
        print('there is no video made, maybe we can not found photo or something else problem happened')
        exit()
    else:
        print('you can find the result from current folder \(^-^)/ ')
except:
    print('Maybe...this account enough photos or google credential problem.')