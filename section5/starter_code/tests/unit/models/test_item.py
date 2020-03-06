from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel("test", 19.99)

        self.assertEqual(item.name, "test",
                         "The name of the Item does not equal constructed argument")
        self.assertEqual(item.price, 19.99,
                         "Price does not equal to value in constructor")

    def test_item_json(self):
        item = ItemModel("test", 19.99)
        expected = {
            'name': 'test',
            'price': 19.99,
        }

        self.assertEqual(item.json(), expected, "Json incorrect, received={} expected={}" \
                         .format(item.json(), expected))

