from django.shortcuts import render

class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        context = {
            'error_message': str(exception),
        }
        return render(request, 'shop/base.html', context)