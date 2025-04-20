from enum import Enum, Flag, auto

""" You use Enum when you want a variable to have a restricted set of predefined values that are named and constant. """

# without Enum
status = "pending"

class Status(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

status = Status.PENDING  # clean and typo-proof!

# class Color(Enum):
#     RED: str = 'R'
#     BLUE: str = 'B'
#     GREEN: str = 'G'

# def create_car(color: Color) -> None:
#     match color:
#         case Color.RED:
#             print(f'A  smoking hot red car was created')
#         case Color.BLUE:
#             print(f'A  slick smooth blue car was created')
#         case Color.GREEN:
#             print(f'A nice green car was created')
#         case _:
#             print(f'We do not have color {color} in our databace')


# class Color(Flag):
#     RED: int = 1
#     BLUE: int = 2
#     GREEN: int = 4
#     YELLOW: int = 8
#     BLACK: int = 16

# yellow_and_red = Color.YELLOW | Color.RED
# print(yellow_and_red)

# for color in Color:
#     if color & yellow_and_red:  
#         print(color)

# combination = Color.RED | Color.YELLOW
# print(combination.value)


class Color(Flag):
    RED: int = auto()
    BLUE: int = auto()
    GREEN: int = auto()
    YELLOW: int = auto()
    BLACK: int = auto()
    ALL: int = RED | GREEN | BLACK | YELLOW | BLACK

# the power of 2
print(Color.RED.value)
print(Color.BLUE.value)
print(Color.GREEN.value)
print(Color.YELLOW.value)
print(Color.BLACK.value)
print(Color.ALL.value)
# 1
# 2
# 4
# 8
# 16
# 29
print(Color.RED in Color.ALL)
# True


""" LAMP """

class State(Enum):
    OFF: int = 0
    ON: int = 1

switch: State = State.OFF

match switch:
    case State.ON:
        print('The lamp is ON')
    case State.OFF:
        print('The lamp is turned OFF')
    case _:
        print('Your lamp is')