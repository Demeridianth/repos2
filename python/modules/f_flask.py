from flask import Flask, url_for, request, redirect, render_template_string, render_template
from markupsafe import escape


app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello,'

# $ flask --app f_flask run
# OR
# app.run(debug=True) WITH DEBUGGER
# TO RUN

# http://127.0.0.1:5000/



# @app.route('/')
# def index():
#     return 'Index page'

# @app.route('/hello') 
# def hello():
#     return 'Hello'      


# -----------------------------------


# @app.route('/')
# def home():
#     return "Welcome to the Flask App!"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/test/<testname>')
# def show_test(testname):
#     return f'test {escape(testname)}'

# in browser: http://127.0.0.1:5000/user/bob - will show 'User bob'
# in browser: http://127.0.0.1:5000/post/1 - will show 'Post 1'
# in browser: http://127.0.0.1:5000/path/sub - will show 'Subpath sub

# string

# (default) accepts any text without a slash

# int

# accepts positive integers

# float

# accepts positive floating point values

# path

# like string but also accepts slashes

# uuid

# accepts UUID strings




# ---------------------------------




# @app.route('/')
# def home():
#     return "Welcome to the Flask App!"

# @app.route('/projects/')
# def projects():
#     return 'project page'
# # only projects can end with /

# @app.route('/about')
# def about():
#     return 'about page'



# ---------------------------------



# URL FOR

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'profile {username}'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# print without hardcoding in every function



# ---------------------------------



# POST | GET needs clicking the HTML file

# @app.route('/')
# def home():
#     return "Welcome to the Flask App!"


# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name=user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success', name=user))


#  -------------------------------------


# HTML Template for rendering the form and displaying data

# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Flask GET and POST Example</title>
# </head>
# <body>
#     <h1>Submit Your Info</h1>
#     <form method="POST">
#         <label for="name">Name:</label>
#         <input type="text" id="name" name="name" required>
#         <br>
#         <label for="age">Age:</label>
#         <input type="number" id="age" name="age" required>
#         <br>
#         <button type="submit">Submit</button>
#     </form>
    
#     {% if name and age %}
#     <h2>Submitted Data:</h2>
#     <p><strong>Name:</strong> {{ name }}</p>
#     <p><strong>Age:</strong> {{ age }}</p>
#     {% endif %}
# </body>
# </html>
# """


# @app.route('/', methods=['GET', 'POST'])

# def index():
#     name = None
#     age = None

#     if request.method == 'POST':
#         name = request.form.get('name')
#         age = request.form.get('age')

#      # Render the HTML template with submitted data (GET or POST)
#     return render_template_string(HTML_TEMPLATE, name=name, age=age)



# -------------------------------------


# RENDER TEMPLATE

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    age = None

    if request.method == 'POST':
        # Retrieve data from the form submission (POST)
        name = request.form.get('name')
        age = request.form.get('age')

    return render_template('form.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)

