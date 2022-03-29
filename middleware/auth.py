from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.http import JsonResponse
class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        #排除不需要登陆的url
        #request.path_info 获取当前用户请求的URL
        if request.path_info == '/api/login_v1/' or request.path_info == '/api/login_v2/' or request.path_info == '/api/add_v1/' or request.path_info == '/api/add_v2/' or request.path_info == '/api/logout/':
            return
        #获取session中信息
        session_data = request.session.get('info')
        #如果已登陆则放行请求
        if session_data:
            return
        return JsonResponse({'status': 201, 'msg': '未登录'})
