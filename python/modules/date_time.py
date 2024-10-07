from datetime import datetime
import locale


def get_date():
    user_locale = locale.getlocale()
    # locale.setlocale(locale.LC_TIME, 'en_GB.UTF-8')
    try:
        locale.setlocale(locale.LC_TIME, user_locale)
    except locale.Error:
        print(f'Locale {user_locale} is not supported on your system. Falling back to "C" locale')
        locale.setlocale(locale.LC_TIME, 'C')
        

    today = datetime.now()
    return f'{today:%c}'
        

print(get_date())