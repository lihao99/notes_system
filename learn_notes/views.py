import datetime
import time

from django import forms
from django.shortcuts import HttpResponse, render, redirect
from django.utils.safestring import mark_safe

from .models import Learn_Notes


# Create your views here.
class LearnNotes(forms.ModelForm):
    class Meta:
        model = Learn_Notes
        fields = ['name', 'content', 'create_type']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15})  # 设置样式
        }


def learn_list(request):
    username = request.session['info']['name']
    data_list = {'username': username}
    valu = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    if valu:
        data_list = {'name__contains': valu}

    page_size = 5  # 每页多少条信息
    start = (page - 1) * page_size
    ending = start + page_size
    form_all = Learn_Notes.objects.filter(**data_list).order_by("-create_time")
    form = form_all[start:ending]  # 每页显示 的信息是那几条
    conut_all = form_all.count()  # 总条数

    # 计算总共有多少页
    toale_page, div = divmod(conut_all, page_size)
    if div:
        toale_page += 1
    page_list = []

    # 取出前后5页的值，不可能把所有的都显示出来。前后都有最大最小值
    start_page = page - 5
    if start_page <= 0:
        start_page = 1
    end_page = page + 5 + 1
    if end_page >= toale_page + 1:
        end_page = toale_page + 1

    # 上一页
    if page != 1:
        elo = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    else:
        elo = '<li><a href="?page=1">首页</a></li>'
    page_list.append(elo)

    # 循环去写入页数
    for i in range(start_page, end_page):
        if i == page:
            elo = '<li class="active" ><a href="?page={}">{}</a></li>'.format(i, i)
        else:
            elo = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_list.append(elo)

        # xia一页
    if page != toale_page:
        elo = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    else:
        elo = '<li><a href="?page={}">尾页</a></li>'.format(toale_page)
    page_list.append(elo)

    string_list = mark_safe("".join(page_list))

    return render(request, 'myshow.html', {'form': form, 'vale': valu, 'string_list': string_list})


def learn_list_all(request):
    data_list = {'create_type': 2}
    valu = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    if valu:
        data_list = {'name__contains': valu}

    page_size = 5  # 每页多少条信息
    start = (page - 1) * page_size
    ending = start + page_size
    form_all = Learn_Notes.objects.filter(**data_list).order_by("-create_time")
    form = form_all[start:ending]  # 每页显示 的信息是那几条
    conut_all = form_all.count()  # 总条数

    # 计算总共有多少页
    toale_page, div = divmod(conut_all, page_size)
    if div:
        toale_page += 1
    page_list = []

    # 取出前后5页的值，不可能把所有的都显示出来。前后都有最大最小值
    start_page = page - 5
    if start_page <= 0:
        start_page = 1
    end_page = page + 5 + 1
    if end_page >= toale_page + 1:
        end_page = toale_page + 1

    # 上一页
    if page != 1:
        elo = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    else:
        elo = '<li><a href="?page=1">首页</a></li>'
    page_list.append(elo)

    # 循环去写入页数
    for i in range(start_page, end_page):
        if i == page:
            elo = '<li class="active" ><a href="?page={}">{}</a></li>'.format(i, i)
        else:
            elo = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_list.append(elo)

        # xia一页
    if page != toale_page:
        elo = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    else:
        elo = '<li><a href="?page={}">尾页</a></li>'.format(toale_page)
    page_list.append(elo)

    string_list = mark_safe("".join(page_list))

    return render(request, 'show.html', {'form': form, 'vale': valu, 'string_list': string_list})


def learn_del(request, uid):
    Learn_Notes.objects.filter(id=uid).delete()
    return redirect('/learn_notes/learn/list/')


def learn_add(request):
    if request.method == 'GET':
        form = LearnNotes()
        return render(request, 'add_note.html', {'form': form})
    # request.POST
    username = request.session['info']['name']
    name = request.POST.get('name')
    content = request.POST.get('content')
    create_type = request.POST.get('create_type')
    cert = Learn_Notes(name=name, content=content, username=username, create_type=create_type)
    cert.save()
    return redirect('/learn_notes/learn/list/')
    # form = LearnNotes(data=request.POST)
    # if form.is_valid():
    #     form.save()
    #     username = request.session['info']['name']
    #     print(username)
    #
    #     return redirect('/learn_notes/learn/list/')


# 详情
def learn_read(request, uid):
    all_con = Learn_Notes.objects.filter(id=uid).first()
    return render(request, 'read.html', {'all_con': all_con})


def learn_edit(request, uid):
    all_con = Learn_Notes.objects.filter(id=uid).first()
    if request.method == 'GET':
        form = LearnNotes(instance=all_con)
        return render(request, 'edit_note.html', {'form': form})

    form = LearnNotes(data=request.POST, instance=all_con)
    if form.is_valid():
        form.save()
        return redirect('/learn_notes/learn/list/')
