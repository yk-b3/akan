from django.conf.urls import url
from cms import views

urlpatterns = [

    url(r'^user/$', views.user_list, name='user_list'),   # 一覧
    url(r'^user/add/$', views.user_edit, name='user_add'),  # 登録
    url(r'^user/mod/(?P<user_id>\d+)/$', views.user_edit, name='use_mod'),  # 修正
    url(r'^user/del/(?P<user_id>\d+)/$', views.user_del, name='user_del'),   # 削除

    url(r'^account/$', views.account_list, name='account_list'),   # 一覧
    url(r'^account/add/$', views.user_edit, name='account_add'),  # 登録
    url(r'^account/mod/(?P<user_id>\d+)/$', views.user_edit, name='account_mod'),  # 修正
    url(r'^account/del/(?P<user_id>\d+)/$', views.user_del, name='account_del'),   # 削除
]