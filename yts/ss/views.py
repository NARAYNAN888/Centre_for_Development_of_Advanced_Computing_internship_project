from django.shortcuts import render
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pymongo
from pymongo import MongoClient
from googleapiclient.errors import HttpError
import urllib.request
import re
from pytube import *
from textblob import TextBlob


# Create your views here.

global list2,list5,ggg
global hh
global na
global sb1,sb2,sb3
sb1 = 0
sb2 = 0
sb3 = 0

na = ""
sriram = "AIzaSyAvQgc5laXF4gz1oBH19IXMTT4tfY5LoHk"


def index3(request):
	global list2,list5,ggg
	global hh,sb1,sb2,sb3
	ggg = 0
	list5 = []
	list2 = []
	sb1 = 0
	sb2 = 0
	sb3 = 0
	sss = urllib.request.urlopen('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl').read().decode()
	dfsss = re.findall(r"watch\?v=(\S{11})", sss)
	for d in range(5):
		hhghh = "https://www.youtube.com/watch?v=" + dfsss[d]
		hjdhdjj = YouTube(hhghh)
		vuu = hhghh
		tt = hjdhdjj.title
		tex = [vuu,tt]
		list5.append(tex)
	api_key = sriram
	youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
	hh = request.POST.get("search3")
	if hh == None:
		hh = "tamilnadu+trending+news&sp=EgQIARAB"
	hh = hh.replace(" ","+")
	reg = youtube.search().list(part="snippet",maxResults=25,q= hh).execute()
	for i in reg['items']:
		a = i['snippet']['title']
		abb = TextBlob(a)
		sd = abb.sentiment.polarity
		pri = ''
		if sd == 0:
			sb1 += 1
			pri ='nu'
		elif sd > 0:
			sb2 += 1
			pri = 'p'
		else:
			sb3 += 1
			pri = 'ne'
		b = i['snippet']['publishedAt']
		c = i['snippet']['channelTitle']
		d = ""
		f = ""
		g = ""
		if i['id']['kind'] == 'youtube#video':
			d = i['id']['videoId']
			# hhghh = "https://www.youtube.com/watch?v=" + d
			# vk = YouTube(hhghh).views
			vk = 0
		elif i['id']['kind'] == 'youtube#channel':
			f = i['id']['channelId']
		elif i['id']['kind'] == 'youtube#playlist':
			g = i['id']['playlistId']
			e = i['snippet']['channelId']
			dict1 = {'pri': pri, 'title':a,'date':b,'channelname':c,'vid': d, 'cid': f, 'pid': g, 'channelid':e,'views': vk}
			list2.append(dict1)
		# return render('ss/index3.html',{'list2':list2})
	j = 0
	while( j <= 2 and "nextPageToken" in reg ):
		reg = youtube.search().list(part="snippet",maxResults=25,q= hh,pageToken=reg["nextPageToken"]).execute()
		for i in reg['items']:
			a = i['snippet']['title']
			abb = TextBlob(a)
			sd = abb.sentiment.polarity
			pri = ''
			if sd == 0:
				sb1 += 1
				pri ='nu'
			elif sd > 0:
				sb2 += 1
				pri = 'p'
			else:
				sb3 += 1
				pri = 'ne'
			b = i['snippet']['publishedAt']
			c = i['snippet']['channelTitle']
			d = ""
			f = ""
			g = ""
			if i['id']['kind'] == 'youtube#video':
				d = i['id']['videoId']
				#hhghh = "https://www.youtube.com/watch?v=" + d
				#vk = YouTube(hhghh).views
				vk = 0
			elif i['id']['kind'] == 'youtube#channel':
				f = i['id']['channelId']
			elif i['id']['kind'] == 'youtube#playlist':
				g = i['id']['playlistId']
			e = i['snippet']['channelId']
			jj = i['snippet']['thumbnails']['high']['url']
			dict1 = {'pri': pri, 'title':a,'date':b,'channelname':c,'vid': d, 'cid': f, 'pid': g,'img':jj, 'channelid':e, 'views': vk}
			list2.append(dict1)
		j += 1
	ggg = len(list2)
	print(ggg)
	return render(request,'ss/index3.html',{'list2':list2,'list5':list5,'sss': ggg, 'sb1': sb1, 'sb2': sb2, 'sb3': sb3})

def ylogin(request):
	return render(request,'you_login.html')
def yrlogin(request):
	return render(request,'youtubereg.html')

def info(request):
	global list5
	api_key = sriram
	youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)


	list2 = []
	d1 ={}
	z  = request.POST.get("srrr")
	req = youtube.videos().list(part="snippet,contentDetails,statistics",id= z).execute()
	a = (req['items'][0]['snippet']['title'])
	b = (req['items'][0]['snippet']['publishedAt'])
	c = (req['items'][0]['snippet']['channelTitle'])
	d = (req['items'][0]['snippet']['description'])
	e = (req['items'][0]['snippet']['tags'])
	f = (req['items'][0]['snippet']['categoryId'])
	g = (req['items'][0]['snippet']['thumbnails']['high']['url'])
	if "defaultAudioLanguage" in req['items'][0]['snippet'] :
		h = (req['items'][0]['snippet']['defaultAudioLanguage'])
		d1 = {'h':h}
	i = (req['items'][0]['contentDetails']['duration'])
	j = (req['items'][0]['contentDetails']['caption'])
	k = (req['items'][0]['contentDetails']['licensedContent'])
	l = (req['items'][0]['contentDetails']['contentRating'])
	m = (req['items'][0]['contentDetails']['dimension'])
	o = (req['items'][0]['statistics']['viewCount'])
	p = (req['items'][0]['statistics']['likeCount'])
	q = (req['items'][0]['statistics']['commentCount'])
	d1 = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'i':i,'j':j,'k':k,'l':l,'m':m,'o':o,'p':p,'q':q}

	return render(request,'ss/info.html',{'list2': d1,'list5': list5})


def comm(request):
	global sb1,sb2,sb3,list5
	sb1 = 0
	sb2 = 0
	sb3 = 0 
	vi = request.POST.get('nana')
	print(vi)
	api_key = sriram 
	youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)


	global list2
	list2 = []
	def scrape_comments_with_replies():
		global sb1,sb2,sb3,list5
		sb1 = 0
		sb2 = 0
		sb3 = 0
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
			data = youtube.commentThreads().list(part='snippet', videoId=id, pageToken=data["nextPageToken"],maxResults='25', textFormat="plainText").execute()
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
	scrape_comments_with_replies()
	sss = len(list2)
	return render(request,'ss/comm.html',{'list2': list2,'sss': sss, 'sb1': sb1, 'sb2': sb2, 'sb3': sb3,'list5': list5})

def csort(request):
    global list2,list5
    list2.sort(key=lambda data2: data2['r'],reverse=True)
    return render(request,'ss/comm.html',{'list2': list2,'list5': list5})

def sort1(request):
	global list2,list5
	list2.sort(key=lambda data2: data2['title'])
	ddd = len(list2)
	return render(request,'ss/index3.html',{ 'list2': list2, 'sss': ddd,'list5': list5})

def sort2(request):
	global list2,list5
	list2.sort(key=lambda data2: data2['title'],reverse=True)
	ddd = len(list2)
	return render(request,'ss/index3.html',{ 'list2': list2,'sss': ddd,'list5': list5})

def sort3(request):
	global list2,list5
	list2.sort(key=lambda data2: data2['date'])
	ddd = len(list2)
	return render(request,'ss/index3.html',{ 'list2': list2,'sss':ddd,'list5': list5})

def sort4(request):
	global list2,list5
	list2.sort(key=lambda data2: data2['date'],reverse=True)
	ddd = len(list2)
	return render(request,'ss/index3.html',{ 'list2': list2,'sss': ddd,'list5': list5})

def sort5(request):
	global list2,list5
	list7 = []
	for i in list2:
		if i['pri'] == 'nu':
			list7.append(i)
	ddd = len(list7)
	return render(request,'ss/index3.html',{'list2':list7, 'sss': ddd,'list5': list5})

def sort6(request):
	global list2,list5
	list7 = []
	for i in list2:
		if i['pri'] == 'p':
			list7.append(i)
	ddd = len(list7)
	return render(request,'ss/index3.html',{'list2':list7, 'sss': ddd,'list5': list5})

def sort7(request):
	global list2,list5
	list7 = []
	for i in list2:
		if i['pri'] == 'ne':
			list7.append(i)
	ddd = len(list7)
	return render(request,'ss/index3.html',{'list2':list7, 'sss': ddd,'list5': list5})

def sort8(request):
	global list2,list5,sb1,sb2,sb3
	list7 = []
	for i in list2:
		if i['pri'] == 'nu':
			list7.append(i)
	ddd = len(list7)
	return render(request,'ss/comm.html',{'list2':list7, 'sss': ddd,'list5': list5})

def sort9(request):
	global list2,list5
	list7 = []
	for i in list2:
		if i['pri'] == 'p':
			list7.append(i)
	ddd = len(list7)
	return render(request,'ss/comm.html',{'list2':list7, 'sss': ddd,'list5': list5})

def sort10(request):
	global list2,list5
	list7 = []
	for i in list2:
		if i['pri'] == 'ne':
			list7.append(i)
	ddd = len(list7)
	return render(request,'ss/comm.html',{'list2':list7, 'sss': ddd,'list5': list5})

def wholedata(request):
	global list2,list5
	global g
	c = pymongo.MongoClient("mongodb://localhost:27017/")
	db = c["Youtube"]
	col = db["Datas"]
	for i in list2:
		db.col.insert_one(i)
	gs = "successfully saved"
	return render(request, 'ss/index3.html', {'list2':list2,'gs': gs,'list5': list5})

def db(request):
	return render(request,'ss/info.html',{})


def channelinfo(request):
	global list5
	list3 = []
	x = request.POST.get("mmn")
	api_key = sriram 
	youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
	req = youtube.channels().list(part="snippet,contentDetails,statistics",id= x).execute()
	a = req['items'][0]['id']
	b = req['items'][0]['snippet']['title']
	c = req['items'][0]['snippet']['description']
	# d = req['items'][0]['snippet']['customUrl']
	e = req['items'][0]['snippet']['publishedAt']
	f = req['items'][0]['snippet']['thumbnails']['high']['url']
	# g = req['items'][0]['snippet']['country']
	h = req['items'][0]['contentDetails']['relatedPlaylists']['likes']
	i = req['items'][0]['contentDetails']['relatedPlaylists']['uploads']
	j = req['items'][0]['statistics']['viewCount']
	k = req['items'][0]['statistics']['subscriberCount']
	l = req['items'][0]['statistics']['videoCount']
	d2 = {'a':a,'b':b,'c':c,'e':e,'f':f,'h':h,'i':i,'j':j,'k':k,'l':l}
	list3.append(d2)
	return render(request,'ss/channelinfo.html',{'list3':list3,'list5': list5})


def filter(request):
	global hh,list5,sb1,sb2,sb3
	kk = hh
	list4 = []
	user = request.POST.get("jjh")
	def normal_search(na):
		sss = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={kk}+{na}').read().decode()
		dfsss = re.findall(r"watch\?v=(\S{11})", sss)
		for d in dfsss:
			hhghh = "https://www.youtube.com/watch?v=" + d
			hjdhdjj = YouTube(hhghh)
			tt = hjdhdjj.title
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

			cn=hjdhdjj.author
			vk = hjdhdjj.views
			vi = hjdhdjj.video_id
			jj = hjdhdjj.thumbnail_url
			ci = hjdhdjj.channel_id
			dd = hjdhdjj.publish_date
			datas = {'pri':pri,'title': tt,'img':jj,'channelname': cn, 'date': dd,'vid': vi, 'channelid': ci,'views': vk}
			list4.append(datas)
	if user == 'today':
		global na
		na = "&sp=EgIIAQ%253D%253D"
		normal_search('&sp=EgIIAQ%253D%253D')
	elif user == 'last_hour':
		na = "&sp=EgQIARAB"
		normal_search('&sp=EgQIARAB')
	elif user == 'this_week':
		na = "&sp=EgQIAxAB"
		normal_search('&sp=EgQIAxAB')
	elif user =='this_month':
		na = "&sp=EgQIBBAB"
		normal_search('&sp=EgQIBBAB')
	elif user =='this_year':
		na = "&sp=EgQIBRAB"
		normal_search('&sp=EgQIBRAB')
	else :
		normal_search('')
	ddd = len(list2)
	return render(request,'ss/index3.html',{'list2':list4, 'sss': ddd,'list5': list5})


def chvi(request):
	global list2,list5,sb1,sb2,sb3
	sb1 = 0
	sb2 = 0
	sb3 = 0
	list2 = []
	jj = request.POST.get("kar")
	sss = urllib.request.urlopen(f'https://www.youtube.com/channel/{jj}').read().decode()
	dfsss = re.findall(r"watch\?v=(\S{11})", sss)
	for d in dfsss:
		hhghh = "https://www.youtube.com/watch?v=" + d
		hjdhdjj = YouTube(hhghh)
		tt = hjdhdjj.title
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

		cn=hjdhdjj.author
		vk = hjdhdjj.views
		vi = hjdhdjj.video_id
		ci = hjdhdjj.channel_id
		dd = hjdhdjj.publish_date
		datas = {'pri':pri,'title': tt,'channelname':cn, 'channelid': ci, 'date': dd,'vid': vi,'views': vk}
		list2.append(datas)
	ddd=len(list2)
	return render(request,'ss/index3.html',{'list2':list2, 'sss': ddd,'list5': list5})


def trending(request):
	global list2,list5,sb1,sb2,sb3
	sb1 = 0
	sb2 = 0
	sb3 = 0
	list2 = []
	nameee = request.POST.get('bbn')
	def explore(a):
		global sb1,sb2,sb3
		sb1 = 0
		sb2 = 0
		sb3 = 0
		sss = urllib.request.urlopen(f'https://www.youtube.com/feed/trending{a}').read().decode()
		dfsss = re.findall(r"watch\?v=(\S{11})", sss)
		for d in dfsss:
			hhghh = "https://www.youtube.com/watch?v=" + d
			hjdhdjj = YouTube(hhghh)
			vuu = hhghh
			tt = hjdhdjj.title
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
			cn=hjdhdjj.author
			vk = hjdhdjj.views
			vi = hjdhdjj.video_id
			ci = hjdhdjj.channel_id
			jj = hjdhdjj.thumbnail_url
			dd = hjdhdjj.publish_date
			datas = {'pri':pri,'title': tt,'img':jj,'channelname':cn, 'date': dd,'vid': vi, 'channelid': ci,'views': vk }
			list2.append(datas)

	if nameee == 'now':
		explore('?bp=6gQJRkVleHBsb3Jl')
	elif nameee=='music':
		explore('?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D')
	elif nameee=='gaming':
		explore('?bp=4gIcGhpnYW1pbmdfY29ycHVzX21vc3RfcG9wdWxhcg%3D%3D')
	elif nameee =='movies':
		explore('?bp=4gIKGgh0cmFpbGVycw%3D%3D')
	ddd=len(list2)
	return render(request, 'ss/index3.html', {'list2': list2,'sss':ddd,'sb1':sb1,'sb2':sb2,'sb3':sb3,'list5': list5})


def live(request):
	global list2,list5,sb1,sb2,sb3
	global ddd
	ddd = 0
	list2 = []
	naamoi = request.POST.get('lol')
	def livee(l):
		global sb1,sb2,sb3
		sb1 = 0
		sb2 = 0
		sb3 = 0
		sss = urllib.request.urlopen(f'https://www.youtube.com/playlist?list=PL{l}').read().decode()
		dfsss = re.findall(r"watch\?v=(\S{11})", sss)
		for d in dfsss:
			hhghh = "https://www.youtube.com/watch?v=" + d
			hjdhdjj = YouTube(hhghh)
			tt = hjdhdjj.title
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
			cn = hjdhdjj.author
			v = hjdhdjj.views
			jj = hjdhdjj.thumbnail_url
			vi = hjdhdjj.video_id
			ci = hjdhdjj.channel_id
			dd = hjdhdjj.publish_date
			datas = {'pri':pri,'title': tt,'views': v,'channelname':cn,'img':jj, 'date': dd,'vid': vi, 'channelid': ci }
			list2.append(datas)
	if naamoi=='live_now':
			livee('U12uITxBEPGwcL0DXQwsIWPesljEdnTb')
	elif naamoi=='recent_stream':
			livee('U12uITxBEPEebFqzWloVENofiVNISGyV')
	elif naamoi=='upcoming_lives':
			livee('U12uITxBEPHHsWCq16kbXhhV4q7DPTka')
	elif naamoi=='live_news':
			livee('3ZQ5CpNulQn0D7Qs8aXKn7AYjS2UwcDt')
	elif naamoi=='live_games':
			livee('iCvVJzBupKnX5f-MIkSuwjVlfm99lJl7')
	elif naamoi=='live_sports':
			livee('8fVUTBmJhHIWLs2PG_T-Kgvic3bZTPX7')
	elif naamoi=='top_stories':
			livee('3ZQ5CpNulQlYMfgK9TMmQT6skrzHjNxd')
	ddd = len(list2)
	return render(request,'ss/index3.html', {'list2':list2,'sss':ddd,'list5': list5,'sb1':sb1,'sb2':sb2,'sb3':sb3})