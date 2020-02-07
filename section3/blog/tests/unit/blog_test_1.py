from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertEqual([], b.posts)
        #self.assertEqual(0, len(b.posts))

    def test_blog_repr(self):
        b = Blog('Test', 'Test Author')
        b.create_post('test title', 'test blog text')

        self.assertEqual(f'<Blog({b.title},{b.author},{b.posts}>', b.__repr__())

    def test_create_post(self):
        b = Blog('Test', 'Test Author')
        b.create_post('test title', 'test blog text')

        self.assertListEqual([['test title', 'test blog text']], b.posts)

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('test title', 'test blog text')

        self.assertDictEqual({'title': b.title, 'author': b.author, 'posts': b.posts}, b.json())