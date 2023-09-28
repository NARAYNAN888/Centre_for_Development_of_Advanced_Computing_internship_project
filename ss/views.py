from django.shortcuts import render
import googleapiclient.discovery
import googleapiclient.errors
import pymongo
from pymongo import MongoClient
import urllib.request
import re
from pytube import *
from textblob import TextBlob

# Create your views here.
global list2,list8
global list5,sb1,sb2,sb3
sb1 = 0
sb2 = 0
sb3 = 0
global g
global na
global rrr2
global list2
g = ""
na = ""
rrr2 = ""


def wholedata(request):
    global list2
    global g
    c = pymongo.MongoClient("mongodb://localhost:27017/")
    db = c["Youtube_Scraping"]
    col = db["Datas"]
    for i in list2:
        db.col.insert_one(i)
    return render(request, 'ss/index3.html', {'g': g})

def ylogin(request):
    c = pymongo.MongoClient("mongodb://localhost:27017/")
    db = c["Youtube_Scraping"]
    col = db["user"]
    rr=db.col
    db.collection.find()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        seo_specialist = authenticate(username=username, password=password)
        if seo_specialist is not col:
            return HttpResponse('ss/you_login.html')
        else:
            return HttpResponse("Not signed in")

    return render(request,'ss/you_login.html')
def yreglogin(request):

    return render(request,'ss/youtubereg.html')

def index3(request):
    global list2,list8,sb1,sb2,sb3,list5
    global dict1
    list2 = []
    list8 = []
    sb1 = 0
    sb2 = 0
    sb3 = 0
    dict1={}
    global rrr2
    rrr2 = request.POST.get('search3')
    user = request.POST.get('jjh')
    list5 = []
    sss = urllib.request.urlopen('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl').read().decode()
    dfsss = re.findall(r"watch\?v=(\S{11})", sss)
    for d in range(5):
        hhghh = "https://www.youtube.com/watch?v=" + dfsss[d]
        hjdhdjj = YouTube(hhghh)
        vuu = hhghh
        tt = hjdhdjj.title
        tex = [vuu, tt]
        list5.append(tex)
    if user == None:
        user = ""
    if rrr2 != None:
        gfg = rrr2.replace(" ", "+")
        sss = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={gfg}+{user}').read().decode()
        dfsss = re.findall(r"watch\?v=(\S{11})", sss)
        for d in dfsss:
            hhghh = "https://www.youtube.com/watch?v=" + d
            hjdhdjj = YouTube(hhghh)
            tt = hjdhdjj.title
            cn = hjdhdjj.author
            vk = hjdhdjj.views
            vi = hjdhdjj.video_id
            vt = hjdhdjj.thumbnail_url
            ci = hjdhdjj.channel_id
            de = hjdhdjj.description
            kk = hjdhdjj.keywords
            dd = hjdhdjj.publish_date
            abb = TextBlob(tt)
            sd = abb.sentiment.polarity
            pri = ''
            if sd == 0:
               sb1 += 1
               pri = 'nu'
            elif sd > 0:
               sb2 += 1
               pri = 'p'
            else:
               sb3 += 1
               pri = 'ne'
            datas = {'title': tt,'descp':de,'keywords': kk,'img': vt, 'pri ': pri, 'author': cn, 'views': vk,'date': dd, 'video_id': vi, 'channel_id': ci,'pri': pri}
            list2.append(datas)
            bel = {'author': cn, 'channel_id': ci}
            list8.append(bel)

    sag = len(list2)
    return render(request, 'ss/index3.html', {'list2': list2, 'list5': list5,'list8': list8, 'rrr2': rrr2, 'user': user,'sag': sag,'sb1':sb1,'sb2':sb2,'sb3':sb3})

def sort5(request):
        global list2,list5,sb1,sb2,sb3
        list7 = []
        for i in list2:
            if i['pri'] == 'nu':
                list7.append(i)
        ddd = len(list7)
        return render(request,'ss/index3.html',{'list2':list7, 'sss': ddd,'list5': list5,'sb1':sb1,'sb2':sb2,'sb3':sb3})

def sort6(request):
        global list2,list5,sb1,sb2,sb3
        list7 = []
        for i in list2:
            if i['pri'] == 'p':
                list7.append(i)
        ddd = len(list7)
        return render(request,'ss/index3.html',{'list2':list7, 'sss': ddd,'list5': list5,'sb1':sb1,'sb2':sb2,'sb3':sb3})

def sort7(request):
        global list2,list5,sb1,sb2,sb3
        list7 = []
        for i in list2:
            if i['pri'] == 'ne':
                list7.append(i)
        ddd = len(list7)
        return render(request,'ss/index3.html',{'list2':list7, 'sss': ddd,'list5': list5,'sb1':sb1,'sb2':sb2,'sb3':sb3})

def sort8(request):
        global list2,sb1,sb2,sb3
        list7 = []
        for i in list2:
            if i['pri'] == 'nu':
                list7.append(i)
        ddd = len(list7)
        return render(request,'ss/comm.html',{'list2':list7, 'sss': ddd,'sb1':sb1,'sb2':sb2,'sb3':sb3})

def sort9(request):
        global list2,sb1,sb2,sb3
        list7 = []
        for i in list2:
            if i['pri'] == 'p':
                list7.append(i)
        ddd = len(list7)
        return render(request,'ss/comm.html',{'list2':list7, 'sss': ddd,'sb1':sb1,'sb2':sb2,'sb3':sb3})

def sort10(request):
        global list2,sb1,sb2,sb3
        list7 = []
        for i in list2:
            if i['pri'] == 'ne':
                list7.append(i)
        ddd = len(list7)
        return render(request,'ss/comm.html',{'list2':list7, 'sss': ddd,'sb1':sb1,'sb2':sb2,'sb3':sb3})

def index4(request):
    global list2,list5
    list2.sort(key=lambda data: data['title'])
    return render(request, 'ss/index3.html', {'list2': list2,'list5': list5})


def index5(request):
    global list2,list5
    list2.sort(key=lambda data: data['title'], reverse=True)
    return render(request, 'ss/index3.html', {'list2': list2,'list5': list5})


def index6(request):
    global list2,list5
    list2.sort(key=lambda data: data['views'])
    return render(request, 'ss/index3.html', {'list2': list2,'list5':list5})


def index7(request):
    global list2,list5
    list2.sort(key=lambda data: data['views'], reverse=True)
    return render(request, 'ss/index3.html', {'list2': list2,'list5':list5})


def index8(request):
    global list2,list5
    list2.sort(key=lambda data: data['date'])
    return render(request, 'ss/index3.html', {'list2': list2,'list5':list5})


def index9(request):
    global list2,list5
    list2.sort(key=lambda data: data['date'], reverse=True)
    return render(request, 'ss/index3.html', {'list2': list2,'list5': list5})


def info(request):
    global list2
    ff = request.POST.get('srrr')
    global g
    g = {}
    for i in list2:
        if ff == i['video_id']:
            g = i
    return render(request, 'ss/info.html', {'list2': list2, 'g': g})


def db(request):
    global list2
    global g
    c = pymongo.MongoClient("mongodb://localhost:27017/")
    db = c["Youtube_Scraping"]
    col = db["Datas"]
    hema = request.POST.get('trt')
    global he
    he = {}
    for i in list2:
        if hema == i['video_id']:
            he = i
            db.col.insert_one(he)
    return render(request, 'ss/info.html', {'g': g})


def trending(request):
    global list2,sb1,sb2,sb3,list5
    sb1 = 0
    sb2 = 0
    sb3 = 0
    list2 = []
    nameee = request.POST.get('bbn')
    sss = urllib.request.urlopen(f'https://www.youtube.com/feed/trending{nameee}').read().decode()
    dfsss = re.findall(r"watch\?v=(\S{11})", sss)
    for d in dfsss:
        hhghh = "https://www.youtube.com/watch?v=" + d
        hjdhdjj = YouTube(hhghh)
        tt = hjdhdjj.title
        cn = hjdhdjj.author
        vd = hjdhdjj.description
        k = hjdhdjj.keywords
        vk = hjdhdjj.views
        vi = hjdhdjj.video_id
        ci = hjdhdjj.channel_id
        vt = hjdhdjj.thumbnail_url
        abb = TextBlob(tt)
        sd = abb.sentiment.polarity
        pri = ''
        if sd == 0:
            sb1 += 1
            pri = 'nu'
        elif sd > 0:
            sb2 += 1
            pri = 'p'
        else:
            sb3 += 1
            pri = 'ne'
        dd = hjdhdjj.publish_date
        datas = {'title': tt, 'author': cn,'img':vt, 'descp': vd, 'keywords': k, 'views': vk, 'date': dd, 'video_id': vi, 'channel_id': ci,'pri':pri}
        list2.append(datas)

    sag=len(list2)

    return render(request, 'ss/index3.html', {'list2': list2,'sag': sag,'list5': list5,'sb1':sb1,'sb2':sb2,'sb3': sb3})


def chvi(request):
    global list2,sb1,sb2,sb3,list5
    sb1 = 0
    sb2 = 0
    sb3 = 0
    list2 = []
    ffg = request.POST.get('mmn')
    sss = urllib.request.urlopen(f'https://www.youtube.com/channel/{ffg}/videos').read().decode()
    dfsss = re.findall(r"watch\?v=(\S{11})", sss)
    l = 1
    while ( l <= 10 ):
        hhghh = "https://www.youtube.com/watch?v=" + dfsss[l]
        hjdhdjj = YouTube(hhghh)
        tt = hjdhdjj.title
        cn = hjdhdjj.author
        vd = hjdhdjj.description
        k = hjdhdjj.keywords
        vk = hjdhdjj.views
        vi = hjdhdjj.video_id
        ci = hjdhdjj.channel_id
        vt = hjdhdjj.thumbnail_url
        dd = hjdhdjj.publish_date

        abb = TextBlob(tt)
        sd = abb.sentiment.polarity
        pri = ''
        if sd == 0:
            sb1 += 1
            pri = 'nu'
        elif sd > 0:
            sb2 += 1
            pri = 'p'
        else:
            sb3 += 1
            pri = 'ne'
        datas = {'title': tt,'img': vt, 'author': cn, 'channel_id': ci, 'descp': vd, 'keywords': k, 'views': vk, 'date': dd,
                 'video_id': vi,'pri':pri}
        list2.append(datas)
        l += 1
    ddd = len(list2)
    return render(request, 'ss/index3.html', {'list2': list2,'list5': list5,'sag':ddd,'sb1':sb1,'sb2':sb2,'sb3':sb3 })


def load(request):
    global list2
    global list3
    global rrr2
    global na,sb1,sb2,sb3,list5
    fgf = rrr2.replace(" ", "+")
    an = na
    sss = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={fgf}+{an}').read().decode()
    dfsss = re.findall(r"watch\?v=(\S{11})", sss)
    for d in dfsss:
        hhghh = "https://www.youtube.com/watch?v=" + d
        hjdhdjj = YouTube(hhghh)
        vuu = hhghh
        tt = hjdhdjj.title
        cn = hjdhdjj.author
        vd = hjdhdjj.description
        k = hjdhdjj.keywords
        vk = hjdhdjj.views
        vi = hjdhdjj.video_id
        ci = hjdhdjj.channel_id
        dd = hjdhdjj.publish_date
        abb = TextBlob(tt)
        sd = abb.sentiment.polarity
        pri = ''
        if sd == 0:
            sb1 += 1
            pri = 'nu'
        elif sd > 0:
            sb2 += 1
            pri = 'p'
        else:
            sb3 += 1
            pri = 'ne'
        datas = {'title': tt, 'author': cn, 'descp': vd, 'keywords': k, 'views': vk, 'date': dd, 'video_id': vi,
                 'video_url': vl, 'channel_url': cl, 'channel_id': ci,'pri':pri}
        list2.append(datas)
        list3.append(datas['channel_id'])

    list3 = list(set(list3))
    return render(request, 'ss/index3.html', {'list2': list2, 'list3': list3, 'fgf': fgf, 'an': an,'list5': list5 })

def comm(request):
    global sb1,sb2,sb3
    sb1 = 0
    sb2 = 0
    sb3 = 0
    vi = request.POST.get('nana')
    print(vi)
    api_key = "AIzaSyA04PT8RSIMY0VAywvNlKuhmJNhfnnAYdQ"
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    global list2
    list2 = []

    data = youtube.commentThreads().list(part='snippet', videoId=vi, maxResults='25', textFormat="plainText").execute()
    for i in data["items"]:
        name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
        comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
        abb = TextBlob(comment)
        sd = abb.sentiment.polarity
        pri = ''
        if sd == 0:
            sb1 += 1
            pri = 'nu'
        elif sd > 0:
            sb2 += 1
            pri = 'p'
        else:
            sb3 += 1
            pri = 'ne'
        published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt']
        likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
        replies = i["snippet"]['totalReplyCount']
        kk = {'pri': pri ,'n': name, 'c': comment, 'd': published_at, 'l': likes, 'r': replies}
        list2.append(kk)
        totalReplyCount = i["snippet"]['totalReplyCount']
        if totalReplyCount > 0:
            parent = i["snippet"]['topLevelComment']["id"]
            data2 = youtube.comments().list(part='snippet', maxResults='25', parentId=parent,textFormat="plainText").execute()
            for i in data2["items"]:
                name = i["snippet"]["authorDisplayName"]
                comment = i["snippet"]["textDisplay"]
                abb = TextBlob(comment)
                sd = abb.sentiment.polarity
                pri = ''
                if sd == 0:
                    sb1 += 1
                    pri = 'nu'
                elif sd > 0:
                    sb2 += 1
                    pri = 'p'
                else:
                    sb3 += 1
                    pri = 'ne'
                published_at = i["snippet"]['publishedAt']
                likes = i["snippet"]['likeCount']
                replies = 0
                kk = {'pri': pri ,'n': name, 'c': comment, 'd': published_at, 'l': likes, 'r': replies}
                list2.append(kk)
    j = 0
    while ( j <= 1 and "nextPageToken" in data ):
        data = youtube.commentThreads().list(part='snippet', videoId=vi , pageToken=data["nextPageToken"],maxResults='25', textFormat="plainText").execute()
        for i in data["items"]:
            name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
            comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
            abb = TextBlob(comment)
            sd = abb.sentiment.polarity
            pri = ''
            if sd == 0:
                sb1 += 1
                pri = 'nu'
            elif sd > 0:
                sb2 += 1
                pri = 'p'
            else:
                sb3 += 1
                pri = 'ne'
            published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt']
            likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
            replies = i["snippet"]['totalReplyCount']
            kk = {'pri': pri ,'n': name, 'c': comment, 'd': published_at, 'l': likes, 'r': replies}
            list2.append(kk)
            totalReplyCount = i["snippet"]['totalReplyCount']
            if totalReplyCount > 0:
                parent = i["snippet"]['topLevelComment']["id"]
                data2 = youtube.comments().list(part='snippet', maxResults='25', parentId=parent,textFormat="plainText").execute()
                for i in data2["items"]:
                    name = i["snippet"]["authorDisplayName"]
                    comment = i["snippet"]["textDisplay"]
                    abb = TextBlob(comment)
                    sd = abb.sentiment.polarity
                    pri = ''
                    if sd == 0:
                        sb1 += 1
                        pri = 'nu'
                    elif sd > 0:
                        sb2 += 1
                        pri = 'p'
                    else:
                        sb3 += 1
                        pri = 'ne'
                    published_at = i["snippet"]['publishedAt']
                    likes = i["snippet"]['likeCount']
                    replies = 0
                    kk = {'pri': pri ,'n': name, 'c': comment, 'd': published_at, 'l': likes, 'r': replies}
                    list2.append(kk)
        j += 1
    sag = len(list2)
    return render(request,'ss/comm.html',{'list2': list2,'sag': sag, 'sb1': sb1, 'sb2': sb2, 'sb3': sb3})




def csort(request):
    global list2,sb1,sb2,sb3
    list2.sort(key=lambda data2: data2['r'], reverse=True)
    return render(request, 'ss/comm.html', {'list2': list2,'sb1': sb1, 'sb2': sb2, 'sb3': sb3,})


def live(request):
    global list2
    global list3,sb1,sb2,sb3,list5
    list2 = []
    list3 = []
    naamoi = request.POST.get('lol')

    sss = urllib.request.urlopen(f'https://www.youtube.com/playlist?list=PL{naamoi}').read().decode()
    dfsss = re.findall(r"watch\?v=(\S{11})", sss)
    for d in dfsss:
        hhghh = "https://www.youtube.com/watch?v=" + d
        hjdhdjj = YouTube(hhghh)
        tt = hjdhdjj.title
        cn = hjdhdjj.author
        vd = hjdhdjj.description
        k = hjdhdjj.keywords
        vk = hjdhdjj.views
        vt = hjdhdjj.thumbnail_url
        vi = hjdhdjj.video_id
        ci = hjdhdjj.channel_id
        dd = hjdhdjj.publish_date
        abb = TextBlob(tt)
        sd = abb.sentiment.polarity
        pri = ''
        if sd == 0:
            sb1 += 1
            pri = 'nu'
        elif sd > 0:
            sb2 += 1
            pri = 'p'
        else:
            sb3 += 1
            pri = 'ne'
        datas = {'title': tt,'img': vt, 'author': cn, 'descp': vd, 'keywords': k, 'views': vk, 'date': dd, 'video_id': vi, 'channel_id': ci}
        list2.append(datas)
    sag=len(list2)
    return render(request, 'ss/index3.html', {'list2': list2,'list5':list5,'sag': sag,'sb1':sb1,'sb2':sb2,'sb3':sb3})

