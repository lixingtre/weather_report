import traceback
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


class ExceptionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        
        if exception == 'no_api_url':
            errormsg='Please fill in the api url in the setting file!'
            status_code=404
        elif exception == 'timeout':
            errormsg='The api request is timeout!'
            status_code=504
        else:
            errormsg='Your api is not correct!'
            status_code=500
        traceback_info = traceback.format_exc()
        logger.info(f"request_path: {request.path}, traceback_info: {traceback_info}")
        return JsonResponse({"msg": errormsg}, status=status_code)