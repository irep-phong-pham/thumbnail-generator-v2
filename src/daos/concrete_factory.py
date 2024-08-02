from .factory_interface import FactoryInterface
from .task_dao import TaskDAOInterface, TaskDAO
from .image_dao import ImageDAOInterface, ImageDAO


class ConcreteFactory(FactoryInterface):
    def create_task_dao(self) -> TaskDAOInterface:
        return TaskDAO()

    def create_image_dao(self) -> ImageDAOInterface:
        return ImageDAO()
