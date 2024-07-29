import mimesis
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender


person = Person(Locale.EN)

female = person.full_name(gender=Gender.FEMALE)
male = person.full_name(gender=Gender.MALE)

