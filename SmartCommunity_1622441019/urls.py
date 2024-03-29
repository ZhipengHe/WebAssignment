from django.conf.urls import url
from . import views

app_name = 'SmartCommunity_1622441019'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^result/$', views.searched, name='result'),
    url(r'^about/$', views.about, name='about'),
    url(r'^help/$', views.help, name='help'),
    url(r'^provider/(?P<id>\d+)/$', views.provider, name='provider'),
    url(r'^profile/$', views.result, name='profile'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/create$', views.createadmin, name='createadmin'),
    url(r'^user/$', views.user, name='user'),
    url(r'^admin/add_info/$', views.info, name='info'),
    url(r'^addissue/$', views.issue, name='createissue'),
    url(r'^result/Volunteer/$', views.volunteer, name='Volunteer'),
    url(r'^result/Member/$', views.member, name='Member'),
    url(r'^result/Issue/$', views.allissue, name='Issue'),
    url(r'^result/Provider/$', views.allprovider, name='Provider'),
    url(r'^issue/(?P<id>\d+)/$', views.eachissue, name='eachissue'),
    ]


