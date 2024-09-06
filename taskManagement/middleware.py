# myapp/middleware.py
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # List of URL patterns that should not require authentication
        exempt_urls = ['/login/', '/register/', '/public/']  # Add URLs you want to be public

        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('/login/')