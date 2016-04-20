from django.conf.urls import url
from cms import views

urlpatterns = [

    url(r'^user/$', views.user_list, name='use_list'),   # 一覧
    url(r'^user/add/$', views.user_edit, name='user_add'),  # 登録
    url(r'^user/mod/(?P<user_id>\d+)/$', views.user_edit, name='use_mod'),  # 修正
    url(r'^user/del/(?P<user_id>\d+)/$', views.user_del, name='user_del'),   # 削除
]