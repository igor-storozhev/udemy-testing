from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():    # context manager
            item = ItemModel('test', 19.99)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"check {item.name} is not exist into db")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test')) # check test is not exist into db
