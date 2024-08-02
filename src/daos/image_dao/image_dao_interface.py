from abc import ABC, abstractmethod


class ImageDAOInterface(ABC):
    @abstractmethod
    def get_image_by_id(self, id):
        pass

    @abstractmethod
    def create_image(self, image_url, image_name, image_size):
        pass
