from django.http import JsonResponse
from .data import CV_DATA


def personal_view(request):
    return JsonResponse(CV_DATA['personal'])


def experience_view(request):
    return JsonResponse(CV_DATA['experience'], safe=False)


def education_view(request):
    return JsonResponse(CV_DATA['education'], safe=False)
