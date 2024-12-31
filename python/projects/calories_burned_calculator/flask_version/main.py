from flask import Flask, request, render_template

app = Flask(__name__)

activity_levels = {
    'sedentary': 1.2,
    'light': 1.375,
    'moderate': 1.55,
    'active': 1.725,
    'super': 1.9
}

met_values = {
    'running': 9.8,
    'cycling': 7.5,
    'walking': 3.3,
    'swimming': 6.0,
    'weightlifting': 3.0,
    'yoga': 2.5,
    'sitting/resting': 1.0
}

def calculate_bmr_tdee(gender, weight, height, age, activity_level):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    tdee = bmr * activity_levels[activity_level]
    return tdee

def calculate_met(weight, activity, duration):
    return met_values[activity] * weight * duration

def calculate_tef(daily_caloric_intake):
    return daily_caloric_intake * 0.10

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            gender = request.form['gender']
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            age = int(request.form['age'])
            activity_level = request.form['activity_level']
            activity = request.form['activity']
            duration = float(request.form['duration'])
            caloric_intake = float(request.form['caloric_intake'])

            tdee = calculate_bmr_tdee(gender, weight, height, age, activity_level)
            met_calories = calculate_met(weight, activity, duration)
            tef = calculate_tef(caloric_intake)

            total_calories_burned = tdee + met_calories + tef

            return render_template('index.html', result=f"You burned {total_calories_burned:,.2f} calories today!")
        except Exception as e:
            return render_template('index.html', result=f"Error: {e}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


# http://127.0.0.1:5000