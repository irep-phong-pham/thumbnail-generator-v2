from .thumbnail_dao_interface import ThumbnailDAOInterface
from ..base_dao import BaseDao


class ThumbnailDAO(BaseDao, ThumbnailDAOInterface):
    def __init__(self):
        BaseDao.__init__(self)

    def get_image_by_id(self, id):
        session = self.db.Session()
        try:
            query = """
            SELECT id, image_url, image_name
            FROM T_IMAGES
            WHERE id=:id
            """
            res_p = session.execute(query, {'id': id})
            res = self.db.to_dict(res_p)
            if res:
                return res[0]
            return None
        except Exception as e:
            print(e)
        finally:
            session.close()

    def create_image(self, image_url, image_name, image_size):
        session = self.db.Session()
        try:
            query = """
            INSERT INTO T_IMAGES (image_url, image_name, image_size)
            VALUES (:image_url, :image_name, :image_size)
            """
            data = {
                "image_url": image_url,
                "image_name": image_name,
                "image_size": image_size
            }
            result = session.execute(query, data)
            image_id = result.lastrowid
            session.commit()
            return image_id
        except Exception as e:
            print(e)
        finally:
            session.close()
