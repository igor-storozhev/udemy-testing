class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"<Blog({self.title},{self.author},{self.posts}>"

    def create_post(self, title, content):
        self.posts.append([title, content])

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'posts': self.posts,
        }

