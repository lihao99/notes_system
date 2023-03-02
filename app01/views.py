import json
from .models import UserInfo, AdminTable
from django.shortcuts import render, redirect, HttpResponse
from django import forms
from .utils.encrypt import md5
from .utils.code import check_code
from django.http import JsonResponse


# Create your views here.


def user_list(request):
    queryset = UserInfo.objects.all()
    return render(request, 'user_list.html', {'queryset': queryset})


##########  Moudleform  ############
class UserForm_add(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'depart', 'gender']


def user_add(request):
    """add部门"""
    if request.method == 'GET':
        form = UserForm_add()
        # content = {
        #     'gender_choice': UserInfo.gender_choices,
        #     'depart_list': Department.objects.all()
        # }
        return render(request, 'user_add.html', {'form': form})
    # post提交数据
    form = UserForm_add(data=request.POST)
    if form.is_valid():
        # 保存到数据库
        form.save()
        return redirect('/app01/user/list/')
    else:
        print(form.errors)


def user_edit(request, uid):
    moud_form = UserInfo.objects.filter(id=uid).first()
    if request.method == 'GET':
        form = UserForm_add(instance=moud_form)
        return render(request, 'user_edit.html', {'form': form})

    form = UserForm_add(data=request.POST, instance=moud_form)
    if form.is_valid():
        form.save()
        return redirect('/app01/user/list')

    return render(request, 'user_edit.html', {'form': form})


def user_del(request, uid):
    UserInfo.objects.filter(id=uid).delete()
    return redirect('/app01/user/list/')


class AdminForm(forms.ModelForm):
    config_pass = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput
    )

    class Meta:
        model = AdminTable
        fields = ['name', 'password', 'config_pass']
        widgets = {
            'password': forms.PasswordInput(render_value=True)  # 密码……………………
        }

    def clean_password(self):
        password = md5(self.cleaned_data.get('password'))
        return password

    def clean_config_pass(self):
        password = self.cleaned_data.get('password')
        re_password = md5(self.cleaned_data.get('config_pass'))
        if password != re_password:
            raise ValueError("密码不一致")
        return re_password


def admin_register(request):
    if request.method == 'GET':
        form = AdminForm()
        return render(request, 'register.html', {'form': form})
    form = AdminForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/app01/user/list')
    else:
        return render(request, 'register.html', {'form': form})


class LoginForm(forms.Form):
    name = forms.CharField(
        label='用户名',
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput,
        required=True
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        password = md5(self.cleaned_data.get('password'))
        return password


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        code = form.cleaned_data.pop('code')
        code_new = request.session.get('code_mage', "")
        if code.upper() != code_new.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {'form': form})

        admin_object = AdminTable.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或者密码错误")
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.name}
        return redirect('/learn_notes/learn/list/')
    return redirect('/app01/login/')


def logout(request):
    request.session.clear()
    return redirect('/app01/login/')


from io import BytesIO


def images_code(request):
    """"图片验证码"""
    img, code_string = check_code()
    request.session['code_mage'] = code_string
    # 设置超时60s
    # request.session.set_expiry('code_mage',60)
    steam = BytesIO()
    img.save(steam, 'png')
    return HttpResponse(steam.getvalue())


def test(request):
    if request.method == "GET":
        return render(request, 'test.html')
    return HttpResponse("12")


def count_num(request):
    return render(request, 'count_num.html')


def chart_bar(request):
    legend = ["A", "B"]
    xAxis = ['1月', '2月', '3月']
    data_list = [{
        "name": 'A',
        "type": 'bar',
        "data": [5, 20, 36, 10, 10, 20]
    },
        {
            "name": 'B',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
        }, ]
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "xAxis": xAxis,
            "series": data_list
        },
    }
    return JsonResponse(result)

#上传图片
def update_pi(request):
    # if request.method == "GET":
    #     return render(request, 'update_pi.html')

    object_name = request.FILES.get("avatar")
    path = "./pict/"+object_name.name
    with open(path, 'wb') as f:
        for chunk in object_name.chunks():
            f.write(chunk)
    return HttpResponse("file_path")
