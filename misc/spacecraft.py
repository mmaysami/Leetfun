"""
Shopify

the Canadian Space Agency is building an unmanned spacecraft that’ll go to the moon.
Here’s some more info about the project.
    The ship’s starting coordinates are (0, 0), which is on Earth.
    The ship’s destination is (0, 250), which is on the moon.

The ship will be controlled over a CLI using a standard keyboard as follows:

    The ship starts at (0, 0) at 0 speed, i.e. at complete rest.
    The ship only moves when a valid key is pressed.
    Pressing W increases the ship’s speed and then moves it forward by speed units. The ship’s maximum speed is 5.
    Pressing S decreases the ship’s speed and then moves it forward by speed units. The ship’s minimum speed is 0.
    After launch, the ship cannot go below speed 1, i.e. it always moves forward until it reaches the moon.
    Pressing A and D move the ship left and right by one unit respectively.
        The ship also moves forward by speed units.

Problem:
Simulate the above spacecraft. Display output as follows:
    Begin with (0, 0) ready for launch.
    After every movement, display the updated position.
    If the ship goes more than 5 points to the left/right, display wrong trajectory.
    If the ship tries to decrease the speed below 1, display minimum speed.
    If the ship tries to increase the speed over 5, display maximum speed.
    When the ship reaches (0, 250) display on the moon.
    If the ship goes beyond 250 on the y-axis, display contact lost.

Sample Output:
    (0, 0) # Begin with original position.
    (0, 1) # W increases the speed to 1 and moves forward.
    (0, 3) # W increases the speed to 2 and moves forward.
    (-1, 5) # A moves the ship left and forward.
    (0, 7) # D moves the ship right and forward.
    (0, 8) # S decreases the speed to 1 and moves forward.
    ...
    (0, 250) on the moon # Ship reaches the moon.
"""

import re
from datetime import datetime as dt


def move(coordinates, speed, command):
    message = None
    if len(command)>0:
        command = command.lower()[0]
    else: command = ''

    if speed == 0 and coordinates == [0, 0]:
        if command == 'w':
            speed = 1
            coordinates = [0, 1]
        else:
            pass

    elif command == 'w':
        if speed == 5: message = 'Maximum Speed'
        speed = min(5, speed + 1)

        coordinates[1] += speed

    elif command == 's':
        if speed == 1: message = 'Minimum Speed'
        speed = max(1, speed - 1)
        coordinates[1] += speed

    elif command == 'a':
        coordinates[1] += speed
        coordinates[0] += -1
        if abs(coordinates[0]) > 5: message = 'wrong trajectory'

    elif command == 'd':
        coordinates[1] += speed
        coordinates[0] += +1
        if abs(coordinates[0]) > 5: message = 'wrong trajectory'

    else:
        # Keep Moving with Wrong Command
        coordinates[1] += speed

    if coordinates[1] > 250:
        message = 'contact lost'
    elif coordinates == [0, 250]:
        message = 'on the moon'

    return coordinates, speed, message


# =========================================================================
coordinates = [0, 0]
speed = 0

while coordinates[1] <= [0, 250]:
    command = input('Press Command Key [W, S, A, D]')
    coordinates, speed, message = move(coordinates, speed, command)
    if message is not None:
        print(message)
    print(coordinates)

