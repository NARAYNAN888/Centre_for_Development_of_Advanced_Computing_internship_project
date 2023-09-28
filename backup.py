# # # <!--      <th bgcolor="grey"><div class="dropdown">-->
# # # <!--    <button class="dropbtn">Views</button>-->
# # # <!--    <i class="arrow down"></i>-->
# # # <!--    <div class="dropdown-content">-->
# # # <!--     <a onclick="location.href='{% url 'v1' %}'" >asscending</a>-->
# # # <!--     <a onclick="location.href='{% url 'v2' %}'">descending</a>-->
# # # <!--    </div>-->
# # # <!--    </div></th>-->
# # # <!--  <th bgcolor="grey"><div class="dropdown">-->
# # # <!--    <button class="dropbtn">Date </button>-->
# # # <!--    <i class="arrow down"></i>-->
# # # <!--    <div class="dropdown-content">-->
# # # <!--     <a onclick="location.href='{% url 'd1' %}'" >asscending</a>-->
# # # <!--     <a onclick="location.href='{% url 'd2' %}'">descending</a>-->
# # # <!--    </div>-->
# # # <!--    </div></center></th>-->
# # #
# # #
# # # global user
# # # temp = loader.get_template("ss/you_login.html")
# # #
# # # if request.method == "POST":
# # #     print("valu r", [x for x in result.POST])
# # #     username = request.POST['userName']
# # #     passwd = request.POST['password']
# # #     user[username] = passwd
# # #     return HttpResponse("<h1>naren</h1>")
# # #
# # # else:
# # #     # return HttpResponse(temp.render({}, request))
# #
# # # table content
# # <table id="ram" class="table table-striped table-bordered table-bordered border-primary" style="width:100%">
# #   <thead>
# #   {% if list2 %}
# #    <tr bgcolor="#OBDA51" ><th colspan="6"><h2><a href="https://www.youtube.com/" target="_blank"><center>YOUTUBE</center></a></h2></th></tr>
# #   <tr>
# #     <th bgcolor="grey"><center><div class="dropdown">
# #         <a class="dropdown-toggle" data-toggle="dropdown" style="color:white">Title</a><i class="arrow down"></i>
# #     <div class="dropdown-menu">
# #      <a onclick="location.href='{% url 'sort' %}'" >asscending</a><br>
# #      <a onclick="location.href='{% url 'ssd' %}'">descending</a>
# #     </div>
# #     </div></center></th>
# #   <th bgcolor="grey" style="color:white"><center>Channel Name</center></th>
# #     <th bgcolor="grey"><div class="dropdown"><CENTER>
# #         <a class="dropdown-toggle" data-toggle="dropdown"style="color:white">Views</a><i class="arrow down"></i>
# #     <div class="dropdown-menu">
# #      <a onclick="location.href='{% url 'v1' %}'" >asscending</a><br>
# #      <a onclick="location.href='{% url 'v2' %}'">descending</a>
# #     </div>
# #     </div></CENTER></th>
# #     <th bgcolor="grey"><center><div class="dropdown">
# #         <a class="dropdown-toggle" data-toggle="dropdown"style="color:white">Date</a>
# #     <i class="arrow down"></i>
# #     <div class="dropdown-menu">
# #      <a onclick="location.href='{% url 'd1' %}'" >asscending</a><br>
# #      <a onclick="location.href='{% url 'd2' %}'">descending</a>
# #     </div>
# #     </div></center></th>
# #
# #   <th bgcolor="grey" style="color:white"><center>Info</center></th>
# #   </tr>
# #   {% endif %}
# #   </thead>
# #   <form method="POST" action="{% url 'info' %}" target="_blank" id="dfd">
# #    {% csrf_token %}
# #   <tbody id="sri">
# #    {% for i in list2 %}
# #     <tr>
# #       <td><a href="{{i.video_url}}" target="blank">{{i.title}}</a></td>
# #       <td><a href="{{i.channel_url}}" target="blank">{{i.author}}</a></td>
# #       <td>{{i.views}}</td>
# #       <td>{{i.date}}</td>
# #       <td><button class="btn btn-load" type="submit" name="srrr" value="{{i.video_id}}" form="dfd">info</button></td>
# #     </tr>
# #    {% endfor %}
# #   </tbody>
# #   </form>
# # </table>
# #                     {% if list2 %}
# #                     <center><button class="btn btn-primary" onclick="location.href='{% url 'load' %}'">Load More</button></center>
# #                     {% endif %}
#
# # import json
# # from django.shortcuts import render, redirect
# # import urllib.request
# # import re
# # from pytube import *
# # import pymongo
# # import ipynb
# # from json import dumps
# # from pymongo import MongoClient
# # from time import sleep
# # # Create your views here.
# # global list2
# # global list3
# # global g
# # global g
# # global na
# # global gfg
# # g = ""
# # na = ""
# # rrr2 = ""
# #
# #
# # def loader(request):
# #     sleep(5)
# #     return render(request,'ss/index3.html')
#
# # def index3(request):
# #     global list2
# #     global list3
# #     list3 = []
# #     list2 = []
# #     global gfg
# #     global na
# #     rrr2 = request.POST.get('search3')
# #     user = request.POST.get('jjh')
# #
# #     def normal_search(na):
# #         if rrr2 != None:
# #             gfg = rrr2.replace(" ", "+")
# #             sss = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={gfg}+{na}').read().decode()
# #             dfsss = re.findall(r"watch\?v=(\S{11})", sss)
# #             for d in dfsss:
# #                 hhghh = "https://www.youtube.com/watch?v=" + d
# #                 hjdhdjj = YouTube(hhghh)
# #                 vuu = hhghh
# #                 tt = hjdhdjj.title
# #                 cn = hjdhdjj.author
# #                 vd = hjdhdjj.description
# #                 k = hjdhdjj.keywords
# #                 vk = hjdhdjj.views
# #                 vi = hjdhdjj.video_id
# #                 vl = hjdhdjj.watch_url
# #                 cl = hjdhdjj.channel_url
# #                 ci = hjdhdjj.channel_id
# #                 dd = hjdhdjj.publish_date
# #                 datas = {'title': tt, 'author': cn, 'descp': vd, 'keywords': k, 'views': vk, 'date': dd, 'video_id': vi,
# #                          'video_url': vl, 'channel_url': cl, 'channel_id': ci}
# #                 list2.append(datas)
# #                 list3.append(datas['channel_id'])
# #
# #     if user == 'today':
# #         na = "&sp=EgIIAQ%253D%253D"
# #         normal_search('&sp=EgIIAQ%253D%253D')
# #     elif user == 'last_hour':
# #         na = "&sp=EgQIARAB"
# #         normal_search('&sp=EgQIARAB')
# #     elif user == 'this_week':
# #         na = "&sp=EgQIAxAB"
# #         normal_search('&sp=EgQIAxAB')
# #     elif user == 'this_month':
# #         na = "&sp=EgQIBBAB"
# #         normal_search('&sp=EgQIBBAB')
# #     elif user == 'this_year':
# #         na = "&sp=EgQIBRAB"
# #         normal_search('&sp=EgQIBRAB')
# #     else:
# #         normal_search('')
# #     list3 = list(set(list3))
# #     sag=len(list2)
# #     return render(request, 'ss/index3.html', {'list2': list2, 'list3': list3, 'rrr2': rrr2, 'na': na , 'sag': sag})
# #
# #
# # def index4(request):
# #     global list2
# #     list2.sort(key=lambda data: data['title'])
# #     return render(request, 'ss/index3.html', {'list2': list2})
# #
# #
# # def index5(request):
# #     global list2
# #     list2.sort(key=lambda data: data['title'], reverse=True)
# #     return render(request, 'ss/index3.html', {'list2': list2})
# #
# #
# # def index6(request):
# #     global list2
# #     list2.sort(key=lambda data: data['views'])
# #     return render(request, 'ss/index3.html', {'list2': list2})
# #
# #
# # def index7(request):
# #     global list2
# #     list2.sort(key=lambda data: data['views'], reverse=True)
# #     return render(request, 'ss/index3.html', {'list2': list2})
# #
# #
# # def index8(request):
# #     global list2
# #     list2.sort(key=lambda data: data['date'])
# #     return render(request, 'ss/index3.html', {'list2': list2})
# #
# #
# # def index9(request):
# #     global list2
# #     list2.sort(key=lambda data: data['date'], reverse=True)
# #     return render(request, 'ss/index3.html', {'list2': list2})
# #
# #
# # def info(request):
# #     global list2
# #     ff = request.POST.get('srrr')
# #     global g
# #     g = {}
# #     for i in list2:
# #         if ff == i['video_id']:
# #             g = i
# #     return render(request, 'ss/info.html', {'list2': list2, 'g': g})
# #
# #
# # def db(request):
# #     global list2
# #     global g
# #     c = pymongo.MongoClient("mongodb://localhost:27017/")
# #     db = c["Youtube_Scraping"]
# #     col = db["Datas"]
# #     hema = request.POST.get('trt')
# #     global he
# #     he = {}
# #     for i in list2:
# #         if hema == i['video_id']:
# #             he = i
# #             db.col.insert_one(he)
# #     return render(request, 'ss/info.html', {'g': g})
# #
#
# #
# # def trending(request):
# #     global list2
# #     list2 = []
# #     nameee = request.POST.get('bbn')
# #
# #     def explore(a):
# #         sss = urllib.request.urlopen(f'https://www.youtube.com/feed/trending{a}').read().decode()
# #         dfsss = re.findall(r"watch\?v=(\S{11})", sss)
# #         for d in dfsss:
# #             hhghh = "https://www.youtube.com/watch?v=" + d
# #             hjdhdjj =YouTube(hhghh)
# #             vuu = hhghh
# #             tt = hjdhdjj.title
# #             cn = hjdhdjj.author
# #             vd = hjdhdjj.description
# #             k = hjdhdjj.keywords
# #             vk = hjdhdjj.views
# #             vi = hjdhdjj.video_id
# #             vl = hjdhdjj.watch_url
# #             cl = hjdhdjj.channel_url
# #             ci = hjdhdjj.channel_id
# #             dd = str(hjdhdjj.publish_date).replace("00:00:00", "")
# #             datas = {'title': tt, 'author': cn, 'descp': vd, 'keywords': k, 'views': vk, 'date': dd, 'video_id': vi,
# #                      'video_url': vl, 'channel_url': cl, 'channel_id': ci}
# #             list2.append(datas)
# #
# #     if nameee == 'now':
# #         explore('?bp=6gQJRkVleHBsb3Jl')
# #     elif nameee == 'music':
# #         explore('?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D')
# #     elif nameee == 'gaming':
# #         explore('?bp=4gIcGhpnYW1pbmdfY29ycHVzX21vc3RfcG9wdWxhcg%3D%3D')
# #     elif nameee == 'movies':
# #         explore('?bp=4gIKGgh0cmFpbGVycw%3D%3D')
# #     return render(request, 'ss/index3.html', {'list2': list2})
# #
# #
# # def chvi(request):
# #     global list2
# #     list2 = []
# #     ffg = request.POST.get('mmn')
# #     sss = urllib.request.urlopen(f'https://www.youtube.com/channel/{ffg}').read().decode()
# #     dfsss = re.findall(r"watch\?v=(\S{11})", sss)
# #     for d in dfsss:
# #         hhghh = "https://www.youtube.com/watch?v=" + d
# #         hjdhdjj = YouTube(hhghh)
# #         vuu = hhghh
# #         tt = hjdhdjj.title
# #         cn = hjdhdjj.author
# #         vd = hjdhdjj.description
# #         k = hjdhdjj.keywords
# #         vk = hjdhdjj.views
# #         vi = hjdhdjj.video_id
# #         vl = hjdhdjj.watch_url
# #         cl = hjdhdjj.channel_url
# #         ci = hjdhdjj.channel_id
# #         dd = (hjdhdjj.publish_date)
# #         datas = {'title': tt, 'author': cn, 'channel_id': ci, 'descp': vd, 'keywords': k, 'views': vk, 'date': dd,
# #                  'video_id': vi, 'video_url': vl, 'channel_url': cl}
# #         list2.append(datas)
# #     return render(request, 'ss/index3.html', {'list2': list2})
# #
# #
# # def load(request):
# #     global list2
# #     global list3
# #     global rrr2
# #     global na
# #     fgf = rrr2.replace(" ", "+")
# #     an = na
# #     print(fgf, an)
# #
# #     sss = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={fgf}+{an}').read().decode()
# #     dfsss = re.findall(r"watch\?v=(\S{11})", sss)
# #     for d in dfsss:
# #         hhghh = "https://www.youtube.com/watch?v=" + d
# #         hjdhdjj = YouTube(hhghh)
# #         vuu = hhghh
# #         tt = hjdhdjj.title
# #         cn = hjdhdjj.author
# #         vd = hjdhdjj.description
# #         k = hjdhdjj.keywords
# #         vk = hjdhdjj.views
# #         vi = hjdhdjj.video_id
# #         vl = hjdhdjj.watch_url
# #         cl = hjdhdjj.channel_url
# #         ci = hjdhdjj.channel_id
# #         dd = hjdhdjj.publish_date
# #         datas = {'title': tt, 'author': cn, 'descp': vd, 'keywords': k, 'views': vk, 'date': dd, 'video_id': vi,
# #                  'video_url': vl, 'channel_url': cl, 'channel_id': ci}
# #         list2.append(datas)
# #         list3.append(datas['channel_id'])
# #
# #     list3 = list(set(list3))
# #     return render(request, 'ss/index3.html', {'list2': list2, 'list3': list3, 'fgf': fgf, 'an': an})
# #
# #
# # #
# # # from django.shortcuts import render
# # # import os
# # # import googleapiclient
# # #
# # # import googleapiclient.discovery
# # # import googleapiclient.errors
# # #
# # #
# # # # Create your views here.
# # #
# # # global list1
# # # list1 = []
# # #
# # #
# # # def index3(request):
# # #     global list1
# # #     api_key = "AIzaSyBeOuvrRAnMt-YtYOeZD_pL7z1xFA_NgRI"
# # #     youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
# # #     h = request.POST.get("search3")
# # #     re = youtube.search().list(part="snippet",maxResults=25,q= h).execute()
# # #     for i in re['items']:
# # #         a = i['snippet']['title']
# # #         b = i['snippet']['publishedAt']
# # #         c = i['snippet']['channelTitle']
# # #         if i['id']['kind'] == 'youtube#video':
# # #              d = i['id']['videoId']
# # #         elif i['id']['kind'] == 'youtube#channel':
# # #             d = i['id']['channelId']
# # #         elif i['id']['kind'] == 'youtube#playlist':
# # #             d = i['id']['playlistId']
# # #         e = i['snippet']['channelId']
# # #     # print(a)
# # #     # print(b)
# # #     # print(c)
# # #     # print(d)
# # #     # print(e)
# # #         dict1 = {'title':a,'date':b,'channelname':c,'id':d,'channelid':e}
# # #         list1.append(dict1)
# # #     j = 0
# # #     while( j <= 5 ):
# # #         re = youtube.search().list(part="snippet",maxResults=25,q= h,pageToken=re["nextPageToken"]).execute()
# # #         for i in re['items']:
# # #             a = i['snippet']['title']
# # #             b = i['snippet']['publishedAt']
# # #             c = i['snippet']['channelTitle']
# # #             if i['id']['kind'] == 'youtube#video':
# # #                 d = i['id']['videoId']
# # #             elif i['id']['kind'] == 'youtube#channel':
# # #                 d = i['id']['channelId']
# # #             elif i['id']['kind'] == 'youtube#playlist':
# # #                 d = i['id']['playlistId']
# # #             e = i['snippet']['channelId']
# # #        # print(a)
# # #        # print(b)
# # #        # print(c)
# # #        # print(d)
# # #        # print(e)
# # #             dict1 = {'title':a,'date':b,'channelname':c,'id':d,'channelid':e}
# # #             list1.append(dict1)
# # #             j += 1
# # #     # print(list1)
# # #         return render(request,'ss/index.html',{'list1':list1})
# # user =authenticate(request, username=username, password=password)
# # if user is not None:
# #     login(request, user)
# #     return redirect('/')
# # else:
# #     messages.info(request, 'invalid credentials')
# #     return redirect('you_login.html')
# # a=request.POST.get("username")
# # b=request.POST.get("password")
# # cd=""
# # if a!=None:
# #     for i in col:
# #         if a==i:
# #             cd=a
# # df = pd.DataFrame({'Name': [i[0] for i in box], 'Comment': [i[1] for i in box], 'Time': [i[2] for i in box],
# #                'Likes': [i[3] for i in box], 'ReplyCount': [i[4] for i in box]})
# # df.to_csv('youtube-comments.csv', index=False, header=False)
# # from django.urls import path,include
# # from . import views
# # urlpatterns = [
# #     path('you/',views.index3,name="you"),
# #     path('sort/',views.index4,name="sort"),
# #     path('info/',views.info,name="info"),
# #     path('ssd/',views.index5,name="ssd"),
# #     path('v1/',views.index6,name="v1"),
# #     path('v2/',views.index7,name="v2"),
# #     path('d1/',views.index8,name="d1"),
# #     path('d2/',views.index9,name="d2"),
# #     path('db/',views.db,name="db"),
# #     path('trending/',views.trending,name="trending"),
# #     path('chvi/',views.chvi,name="chvi"),
# #     path('load/',views.load,name="load"),
#
# #     path('',views.index3,name="ll"),
# #     path('ylogin/', views.ylogin, name="ylogin"),
# #     path('tlogin/', views.tlogin, name="tlogin"),
# #     path('yrlogin/', views.yreglogin, name="yrlogin"),
# #     path('trlogin/', views.treglogin, name="trlogin"),
# #     path('frg/', views.frgpass, name="frg"),
# #
# #
# # ]
# {%load static%}
# <!DOCTYPE html>
# <html lang="en">
#
# <head>
#
#     <meta charset="UTF-8">
#     <title>home</title>
#  <link href="{%' css/bootstrap.min.css' }">
# </head>
#
#
# <body>
# {% block content %}
# <table id="ram" class="table table-striped table-bordered table-bordered border-primary" style="width:100%">
#   <thead>
#   {% if list1 %}
#    <tr bgcolor="#OBDA51" ><th colspan="5"><h2><a href="https://www.youtube.com/" target="_blank"><center>YOUTUBE</center></a></h2></th></tr>
#   <tr>
#     <th bgcolor="grey"><center><div class="dropdown">
#         <a class="dropdown-toggle" data-toggle="dropdown" style="color:white">Title</a><i class="arrow down"></i>
#     <div class="dropdown-menu">
#      <a onclick="location.href='{% url 'sort' %}'" >asscending</a><br>
#      <a onclick="location.href='{% url 'ssd' %}'">descending</a>
#     </div>
#     </div></center></th>
#   <th bgcolor="grey" style="color:white"><center>Channel Name</center></th>
#     <th bgcolor="grey"><div class="dropdown"><CENTER>
#         <a class="dropdown-toggle" data-toggle="dropdown"style="color:white">Views</a><i class="arrow down"></i>
#     <div class="dropdown-menu">
#      <a onclick="location.href='{% url 'v1' %}'" >asscending</a><br>
#      <a onclick="location.href='{% url 'v2' %}'">descending</a>
#     </div>
#     </div></CENTER></th>
#     <th bgcolor="grey"><center><div class="dropdown">
#         <a class="dropdown-toggle" data-toggle="dropdown"style="color:white">Date</a>
#     <i class="arrow down"></i>
#     <div class="dropdown-menu">
#      <a onclick="location.href='{% url 'd1' %}'" >asscending</a><br>
#      <a onclick="location.href='{% url 'd2' %}'">descending</a>
#     </div>
#     </div></center></th>
#
#   <th bgcolor="grey" style="color:white"><center>Info</center></th>
#   </tr>
#   {% endif %}
#   </thead>
#   <form method="POST" action="{% url 'info' %}" target="_blank" id="dfd">
#    {% csrf_token %}
#   <tbody id="sri">
#    {% for i in list2 %}
#     <tr>
#       <td><a href="{{i.video_url}}" target="blank">{{i.title}}</a></td>
#       <td><a href="{{i.channel_url}}" target="blank">{{i.author}}</a></td>
#       <td>{{i.views}}</td>
#       <td>{{i.date}}</td>
#       <td><button  type="submit" name="srrr" value="{{i.video_id}}" form="dfd">info</button></td>
#     </tr>
#    {% endfor %}
#   </tbody>
#   </form>
# </table>
#                     <!-- end of table content -->
#
# <script src="js/jquery.min.js"></script>
#
# <script src="js/bootstrap.min.js"></script>
# {% endblock %}
# </body>
#
#
#
# </html>

            <!-- Nav Item - Charts -->
            <li class="nav-item">
                <a class="nav-link" href="charts.html">
                    <i class="fas fa-fw fa-chart-area"></i>
                    <span>Maps</span></a>
            </li>
  <--<div class="text-center fs-6"> <a href="{% url 'frg' %}">Forget password?</a> or <a href="{% url 'yrlogin' %}">Sign up</a> </div>
</div>-->
