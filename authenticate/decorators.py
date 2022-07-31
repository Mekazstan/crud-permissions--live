from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):            
            group = None
            if request.user.groups.exists():   #if user is in a group/groups
                group = request.user.groups.all()[0].name    # make group == user's group/first group name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'You are not a SUPER USER!!!!')
                return redirect('/')
                print('You are not a SUPER USER!!!!')
        return wrapper_func
    return decorator

# def admin_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         groups = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#         if group == 'customer':
#             return redirect('Customer-page')
#         if group == 'admin':
#             return view_func(request, *args, **kwargs)
#     return wrapper_func
        
        