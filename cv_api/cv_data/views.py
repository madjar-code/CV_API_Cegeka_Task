from django.http import (
    JsonResponse,
)
from .data import CV_DATA


def personal_view(request):
    return JsonResponse(CV_DATA['personal'])
