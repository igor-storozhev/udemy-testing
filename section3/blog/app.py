from blog import Blog

MENU_PROMPT = 'Enter "c" to create blog, "l" list blog, "r" read one, "p" create post , "q" to quit'
POST_TEMPLATE = '''
    --- {} ---
    
    {}
    '''

blogs = dict() # blog_name: Blog object

def menu():
    # show user available blogs
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():     # [(blog_name, blog), ...]
        print('- {}'.format(blog))

def ask_create_blog():
    title = input("Blog title:")
    author = input("Your name:")
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input("Enter blog name:")

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('Enter blog name for post:')
    title = input('Enter post title:')
    content = input('Enter post content:')

    blogs[blog_name].create_post(title, content)


