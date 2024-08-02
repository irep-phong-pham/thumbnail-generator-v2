from abc import ABC, abstractmethod
from .task_dao import TaskDAOInterface
from .image_dao import ImageDAOInterface


class FactoryInterface(ABC):
    @abstractmethod
    def create_task_dao(self) -> TaskDAOInterface:
        pass

    @abstractmethod
    def create_image_dao(self) -> ImageDAOInterface:
        pass
