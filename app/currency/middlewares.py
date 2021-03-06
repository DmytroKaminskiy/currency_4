from django.db.models import F

from currency.models import Analytics
from currency import choices

class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):


        '''
        path = '/foo/'
        method = 'GET'

        Analytics.objects.filter(method=method, path=path)
        Analytics.objects.update_or_create(method=method, path=path)
        '''

        response = self.get_response(request)
        if response.status_code == 200:
            # https://stackoverflow.com/questions/52024039/how-to-use-update-or-create-and-f-to-create-a-new-record-in-django
            request_method = choices.REQUEST_METHOD_CHOICES_MAPPER[request.method]
            obj, created = Analytics.objects.get_or_create(
                request_method=request_method, path=request.path,
                defaults={'counter': 1}
            )
            if not created:
                Analytics.objects.filter(pk=obj.pk).update(counter=F('counter') + 1)
            # counter = Analytics.objects.filter(
            #     request_method=request_method, path=request.path).last()
            # if counter:
            #     counter.counter += 1
            #     counter.save()
            # else:
            #     Analytics.objects.create(
            #         request_method=request_method, path=request.path, counter=1)
        return response
