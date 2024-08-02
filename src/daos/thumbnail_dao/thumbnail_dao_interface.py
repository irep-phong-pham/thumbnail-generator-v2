from abc import ABC, abstractmethod


class ThumbnailDAOInterface(ABC):
    @abstractmethod
    def get_thumbnail_by_id(self, id):
        pass

    @abstractmethod
    def create_thumbnail(self, image_url, image_name, image_size):
        pass
