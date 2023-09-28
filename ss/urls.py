from django.urls import path
from . import views
urlpatterns = [
    path('',views.index3,name="you"),
    path('wd',views.wholedata,name="wd"),
    path('sort/',views.index4,name="sort"),
    path('info/',views.info,name="info"),
    path('ssd/',views.index5,name="ssd"),
    path('v1/',views.index6,name="v1"),
    path('v2/',views.index7,name="v2"),
    path('d1/',views.index8,name="d1"),
    path('d2/',views.index9,name="d2"),
    path('sort5/', views.sort5, name="sort5"),
    path('sort6/', views.sort6, name="sort6"),
    path('sort7/', views.sort7, name="sort7"),
    path('sort8/', views.sort8, name="sort8"),
    path('sort9/', views.sort9, name="sort9"),
    path('sort10/', views.sort10, name="sort10"),
    path('db/',views.db,name="db"),
    path('trending/',views.trending,name="trending"),
    path('chvi/',views.chvi,name="chvi"),
    path('load/',views.load,name="load"),
    path('comm/',views.comm,name="comm"),
    path('csort/',views.csort,name="csort"),
    path('live/',views.live,name="live"),
    path('',views.index3,name="ll"),
    path('ylogin/', views.ylogin, name="ylogin"),
    path('yrlogin/', views.yreglogin, name="yrlogin"),


]
