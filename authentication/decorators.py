from django.shortcuts import redirect

def only_alessandro(view_func):
    def wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        if request.user.username != 'Alessandro':
            return redirect('inicio')

        return view_func(request, *args, **kwargs)
    return wrapped
