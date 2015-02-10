from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfriends_webserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/createuser$','wefriends_web_services.views.view_createUser'),
    url(r'^users/login$','wefriends_web_services.views.view_login'),
    url(r'^users/getuserinfobytoken$','wefriends_web_services.views.view_getUserInfoByToken'),
    url(r'^users/getuserinfobywefriendsid$','wefriends_web_services.views.view_getUserInfoByWefriendsId'),
    url(r'^users/updateuserinfo$','wefriends_web_services.views.view_updateUserInfo'),
    url(r'^users/updatewhatsup$','wefriends_web_services.views.view_updateWhatsup'),


    url(r'^files/upload$','wefriends_web_services.views.view_uploadFile'),

)
