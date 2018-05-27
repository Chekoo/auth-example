from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(request):
    # 只有当请求为post时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的是username, password, email,用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)
        # 验证数据的合法性
        if form.is_valid():
            # 合法，调用save将数据保存到数据库
            form.save()
            # 注册成功，跳回首页
            return redirect('/')
    else:
        # 请求不是POST,表明用户正在访问注册页面，展示一个新的注册表单给用户
        form = RegisterForm()
    # 渲染模板
    return render(request, 'users/register.html', context={'form': form})


