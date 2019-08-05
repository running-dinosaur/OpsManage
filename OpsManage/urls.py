from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path

from OpsManage.views import index,users


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.IndexView.as_view()),
    url(r'^login/$', index.login),
    url(r'^logout/$', index.logout),
    url(r'^403/$', index.Permission.as_view()),
    url(r'^404/$', index.PageError.as_view()),
    url(r'^user/manage/$', users.UserManage.as_view()),
    url(r'^user/center/$', users.UserCenter.as_view()),
    url(r'^group/manage/$', users.GroupManage.as_view()),
    url(r'^api/',include('api.urls')),
    url(r'^assets/',include('asset.urls')),
    url(r'^deploy/',include('deploy.urls')),
    url(r'^db/',include('databases.urls')),
    url(r'^sched/',include('sched.urls')),
    url(r'^apps/',include('cicd.urls')),
    url(r'^nav/',include('navbar.urls')),
    url(r'^websocket/',include('websocket.urls')),
    url(r'^wiki/',include('wiki.urls')),
    url(r'^order/',include('orders.urls')),
    url(r'^apply/',include('apply.urls')),
    path('favicon.ico', serve, {'path': 'images/favicon.png'}),
]
