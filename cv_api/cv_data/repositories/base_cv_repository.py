from typing import Dict, List
from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def get_personal_info(self) -> Dict[str, str] | None:
        pass

    @abstractmethod
    def get_experience(self) -> List[Dict[str, str]] | None:
        pass

    @abstractmethod
    def get_education(self) -> List[Dict[str, str]] | None:
        pass
