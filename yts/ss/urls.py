from django.urls import path
from . import views

urlpatterns = [
    path('',views.index3,name="you"),
    # path('load/',views.load,name="load"),
    path('info/',views.info,name="info"),
    path('comm/',views.comm,name="comm"),
    path('ylogin/',views.ylogin,name="ylogin"),
    path('yrlogin/',views.ylogin,name="yrlogin"),
    path('wd',views.wholedata,name="wd"),
    path('csort/',views.csort,name="csort"),
    path('sort1/',views.sort1,name="sort"),
    path('sort2/',views.sort2,name="ssd"),
    path('sort3/',views.sort3,name="d1"),
    path('sort4/',views.sort4,name="d2"),
    path('sort5/',views.sort5,name="sort5"),
    path('sort6/',views.sort6,name="sort6"),
    path('sort7/',views.sort7,name="sort7"),
    path('sort8/',views.sort8,name="sort8"),
    path('sort9/',views.sort9,name="sort9"),
    path('sort10/',views.sort10,name="sort10"),
    path('db/',views.db,name="db"),
    path('channelinfo/',views.channelinfo,name="channelinfo"),
    path('filter/',views.filter,name="filter"),
    path('chvi/',views.chvi,name="chvi"),
    path('trending/',views.trending,name="trending"),
    path('live/',views.live,name="live"),
]