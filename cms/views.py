from django.shortcuts import render
from django.http import HttpResponse


def user_list(request):
    """ユーザ情報の一覧"""

    return render(request,
                  'cms/user_list.html'
                 )


def user_edit(request, parameter_id=None):
    """ユーザ情報の編集"""
    return HttpResponse('ユーザ情報の編集')


def user_del(request, parameter_id):
    """ユーザ情報の削除"""
    return HttpResponse('ユーザ情報の削除')