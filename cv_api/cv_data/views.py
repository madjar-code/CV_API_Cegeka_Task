from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .data import CV_DATA


@swagger_auto_schema(
    method='GET',
    operation_id='get_personal_data',
)
@api_view(['GET'])
def personal_view(request: Request) -> Response:
    return Response(
        data=CV_DATA['personal'],
        status=status.HTTP_200_OK
    )


@swagger_auto_schema(
    method='GET',
    operation_id='get_experience_data',
)
@api_view(['GET'])
def experience_view(request: Request) -> Response:
    return Response(
        data=CV_DATA['experience'],
        status=status.HTTP_200_OK
    )


@swagger_auto_schema(
    method='GET',
    operation_id='get_education_data',
)
@api_view(['GET'])
def education_view(request: Request) -> Response:
    return Response(
        data=CV_DATA['education'],
        status=status.HTTP_200_OK
    )
