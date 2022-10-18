from django.urls import resolve
from django.utils.translation import activate


# Source: https://stackoverflow.com/a/9791452
class DisableAdminI18nMiddleware:
    """Custom middleware that disables admin page translation"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver_match = resolve(request.path)
        if resolver_match.app_name == 'admin':
            activate('en')
        response = self.get_response(request)
        return response
