from typing import Dict, List
from cv_data.data import CV_DATA
from .base_cv_repository import BaseRepository


class HardCodeCVRepository(BaseRepository):
    def get_personal_info(self) -> Dict[str, str] | None:
        return CV_DATA.get('personal')

    def get_experience(self) -> List[Dict[str, str]] | None:
        return CV_DATA.get('experience')

    def get_education(self) -> List[Dict[str, str]] | None:
        return CV_DATA.get('education')
