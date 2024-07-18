from typing import Dict, List
from cv_data.models import Personal, Experience, Education
from .base_cv_repository import BaseRepository


class DatabaseCVRepository(BaseRepository):
    def get_personal_info(self) -> Dict[str, str]:
        if Personal.objects.exists():
            personal: Personal = Personal.objects.first()
            return {
                'name': personal.name,
                'email': personal.email,
                'phone': personal.phone
            }
        return None

    def get_education(self) -> List[Dict[str, str]] | None:
        education_records = list(Education.objects.values(
            'institution', 'degree', 'start_date', 'end_date'))

        if education_records:
            return education_records
        return None

    def get_experience(self) -> List[Dict[str, str]] | None:
        experience_records = list(Experience.objects.values(
            'company', 'position', 'start_date', 'end_date'))

        if experience_records:
            return experience_records
        return None
