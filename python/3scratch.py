from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    age = None

    if request.method == 'POST':
        request.form.get('name')
        request.form.get('age')

    return render_template('INSERT_HTML_FILE_HERE.html', name=name, age=age)




if __name__ == '__main__':
    app.run(debug=True)