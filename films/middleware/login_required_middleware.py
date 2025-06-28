from django.shortcuts import redirect

EXEMPT_URLS = [
    '/login/',
    '/register/',
    '/admin/',
    '/',
    '/static/',

]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if not request.session.get('kullanici_id'):
            if not any(path.startswith(url) for url in EXEMPT_URLS):
                return redirect('login')

        return self.get_response(request)