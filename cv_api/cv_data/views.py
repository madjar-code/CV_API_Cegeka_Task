from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .repositories.hard_code_cv_repository import HardCodeCVRepository
# from .repositories.database_cv_repository import DatabaseCVRepository


repository = HardCodeCVRepository()


@swagger_auto_schema(
    method='GET',
    operation_id='get_personal_data',
)
@api_view(['GET'])
def personal_view(request: Request) -> Response:
    personal_info = repository.get_personal_info()
    if personal_info:
        return Response(
            data=personal_info,
            status=status.HTTP_200_OK
        )
    return Response(
        data={"detail": "Personal information not found"},
        status=status.HTTP_404_NOT_FOUND
    )


@swagger_auto_schema(
    method='GET',
    operation_id='get_experience_data',
)
@api_view(['GET'])
def experience_view(request: Request) -> Response:
    experience_info = repository.get_experience()
    if experience_info:
        return Response(
            data=experience_info,
            status=status.HTTP_200_OK
        )
    return Response(
        data={"detail": "Experience information not found"},
        status=status.HTTP_404_NOT_FOUND
    )


@swagger_auto_schema(
    method='GET',
    operation_id='get_education_data',
)
@api_view(['GET'])
def education_view(request: Request) -> Response:
    education_info = repository.get_education()
    if education_info:
        return Response(
            data=education_info,
            status=status.HTTP_200_OK
        )
    return Response(
        data={"detail": "Education information not found"},
        status=status.HTTP_404_NOT_FOUND
    )
