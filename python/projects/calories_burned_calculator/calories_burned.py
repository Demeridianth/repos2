""" calories burned in a day calculator"""


def calculate_bmr_tdee(gender: str, weight: int, height: int, age: int, activity_level: float) -> float:
    # bmr = Basal Metabolic Rate
    # tdee = Total Daily Energy Expenditure

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
    # met = Metabolic Equivalent of Tasks
    met_values = {
        'running': 9.8,
        'cycling': 7.5,
        'walking': 3.3,
        'swimming': 6.0,
        'weightlifting': 3.0,
        'yoga': 2.5,
        'sitting/resting': 1.0
    }

    calories_burned =  met_values[activity] * weight * duration
    return calories_burned   


def calculate_tef(daily_caloric_intake: float) -> float:
    # tef = Thermic Effect of Food
    tef = daily_caloric_intake * 0.10 
    return tef


def get_choice(prompt, choices):
    while True:
        user_input = input(f'{prompt}' )
        if user_input in choices:
            return user_input
        else:
            print('enter valid choice')


def get_input(prompt, converter=str):
    while True:
        try:
            return converter(input(prompt))
        except ValueError:
            print('enter valid parameter')


def main():
    activity_lvls = ['sedentary', 'light', 'moderate', 'active', 'super']
    activities = ['running', 'cycling', 'walking', 'swimming', 'weightlifting', 'yoga', 'sitting/resting']

    gender = get_input('enter your gender: male/female: ')
    weight = get_input('enter your weight: (kg) ', int)
    height = get_input('enter your height: (cm) ', int)
    age = get_input('enter your age: ', int)

    print('\nActivity levels:', ', '.join(activity_lvls))
    activity_level = get_choice('choose your activity level: ', activity_lvls)

    print('\nActivities:', ', '.join(activities))
    activity = get_choice('choose your daily physical activity: ', activities)   
    duration = get_input('enter your activity duration: (hours) ', float)
    calories = get_input('please enter your daily coloric intake: ', float)
        
    # calculate calories burned
    calories_burned = calculate_bmr_tdee(gender, weight, height, age, activity_level) 
    + calculate_met(weight, activity, duration) 
    + calculate_tef(calories)

    print('-' * 10)
    print(f'you have burned {calories_burned:,.2f} calories')
    print('-' * 10)
    


if __name__ == '__main__':
    main()


