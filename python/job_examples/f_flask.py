from flask import Flask, request, render_template

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
