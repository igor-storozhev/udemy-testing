blogs = dict() # blog_name: Blog object

def menu():
    # show user available blogs
    print_blogs()

def print_blogs():
    for key, blog in blogs.items():     # [(blog_name, blog), ...]
        print('- {}'.format(blog))

