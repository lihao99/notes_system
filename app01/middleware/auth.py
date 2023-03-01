from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, HttpResponse


class AuthMiddle(MiddlewareMixin):
    def process_request(self, request):

        if request.path_info in ['/app01/images/code/', '/app01/login/', '/app01/admin/register/']:
            return
        # 读取当前访问用户的session信息
        new_session = request.session.get("info")
        if new_session:
            return
        else:
            return redirect('/app01/login/')
