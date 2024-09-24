from flask import Flask, render_template, request

app = Flask(__name__)

# Existing functions to calculate calories burned
def calculate_bmr_tdee(gender: str, weight: int, height: int, age: int, activity_level: str) -> float:
    activity_levels = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'super': 1.9
    }

    if gender == 'male':
        bmr_male = 10 * weight + 6.25 * height - 5 * age + 5
        tdee_male = bmr_male * activity_levels[activity_level]
        return tdee_male

    elif gender == 'female':
        bmr_female = 10 * weight + 6.25 * height - 5 * age - 161
        tdee_female = bmr_female * activity_levels[activity_level]
        return tdee_female
    

def calculate_met(weight: int, activity: str, duration: float) -> float:
    met_values = {
        'running': 9.8,
        'cycling': 7.5,
        'walking': 3.3,
        'swimming': 6.0,
        'weightlifting': 3.0,
        'yoga': 2.5,
        'sitting/resting': 1.0
    }
    return met_values[activity] * weight * duration


def calculate_tef(daily_caloric_intake: float) -> float:
    return daily_caloric_intake * 0.10


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gender = request.form['gender']
        weight = int(request.form['weight'])
        height = int(request.form['height'])
        age = int(request.form['age'])
        activity_level = request.form['activity_level']
        activity = request.form['activity']
        duration = float(request.form['duration'])
        calories = float(request.form['calories'])

        # Calculate calories burned
        calories_burned = (
            calculate_bmr_tdee(gender, weight, height, age, activity_level) +
            calculate_met(weight, activity, duration) +
            calculate_tef(calories)
        )

        return render_template('result.html', calories_burned=calories_burned)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

