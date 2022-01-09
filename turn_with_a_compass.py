class TurnIsOutOfRange(Exception):
    """Raised when the input 'turn' is out of range."""

    def __init__(self, turn, message='Turn is not in (-1080, 1080) range or isn\'t multiple of 45'):
        self.turn = turn
        self.message = message
        super().__init__(f'{self.message}. Got turn={self.turn}')


class InvalidDirection(Exception):
    """Raised when the input 'turn' is out of range."""

    def __init__(self, direction, message='Direction of facing is invalid'):
        self.direction = direction
        self.message = message
        super().__init__(f'{self.message}. Got direction="{self.direction}"')


def get_key_by_value(my_dict, val):
    """Util function to find key from 'my_dict' by value 'val'"""
    for key, value in my_dict.items():
        if value == val:
            return key


def direction(facing, turn):
    # Check if turn is between needed range
    if((turn % 45 != 0) or (turn > 1080) or (turn < -1080)):
        raise TurnIsOutOfRange(turn)

    direction_degree = {
        "N": 0,
        "NE": 45,
        "E": 90,
        "SE": 135,
        "S": 180,
        "SW": 225,
        "W": 270,
        "NW": 315,
    }

    # Check if facing direction is valid
    if(facing not in direction_degree):
        raise InvalidDirection(facing)

    # Find current degree facing and calculate new one and name the direction
    current_degree = direction_degree[facing]

    # will be always positive number, bc of positive delimeter
    new_degree = (current_degree + turn) % 360
    new_direction = get_key_by_value(direction_degree, new_degree)

    return new_direction
