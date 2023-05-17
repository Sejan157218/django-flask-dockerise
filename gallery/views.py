from django.http import JsonResponse


def Test(request):
    return JsonResponse({'app':'Running'}) 