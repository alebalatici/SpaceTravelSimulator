import math
from math import radians, sin, cos, sqrt
class Calculations:
    G = 6.67e-11
    Earth_Mass = 5.9722e24
    AU = 149597870.7

    def convert_kilometres_to_metres(self, kilometre: float) -> float:
        """
        Converts the given number of kilometres to the number of metres
        :param kilometre: the given number kilometres
        :return: metres of the given number
        """
        return kilometre * 1000

    def calculate_the_escape_velocity(self, diameter: float, mass: float) -> float:
        """
        Calculates the escape velocity given the diameter and mass
        :param diameter: the given diameter
        :param mass: the given mass
        :return: the escape velocity
       """
        #Note: the formula is v = sqrt((2 * G * M) / r) = sqrt((4 * G * M) / d) where M is the mass, r is the radius and d is the diameter
        return math.sqrt(4 * self.G * mass / diameter)

    def convert_earths_to_kilograms(self, earths: float) -> float:
        """
        Converts the mass in earth to kilograms
        :param earths: mass of the planet in earths
        :return: mass of the planet in kilograms
        """
        return earths * self.Earth_Mass

    def calculate_time_needed_to_reach_escape_velocity(self, escape_velocity: float, number_of_engines: int, acceleration_per_engine: float) -> float:
        """
        Calculates the time needed to reach the escape velocity
        :param escape_velocity: The escape velocity of the planet
        :param number_of_engines: The number of engines the rocket has
        :param acceleration_per_engine: The acceleration per engine
        :return: the time needed to reach the escape velocity for the planet
        """
        return escape_velocity / (number_of_engines * acceleration_per_engine)

    def calculate_distance_needed_to_reach_escape_velocity(self, velocity: float, time: float, acceleration: float) ->float:
        """
        Calculates the distance needed to reach the escape velocity
        :param velocity: The starting velocity
        :param time: The time needed for the rocket to reach the escape velocity
        :param acceleration: The acceleration of the engine
        :return: the distance needed to reach the escape velocity for the planet
        """
        return velocity * time + (acceleration * time * time) / 2

    def calculate_distance_needed_to_reach_escape_velocity_from_centre(self, velocity: float, time: float, acceleration: float, diameter: int) -> float:
        """
        Calculates the distance needed to reach the escape velocity from the centre of the planet
        :param velocity: The starting velocity
        :param time: The time needed for the rocket to reach the escape velocity
        :param acceleration: The acceleration of the engine
        :return: the distance needed to reach the escape velocity for the planet from the centre of the planet
        """
        return diameter / 2 + self.calculate_distance_needed_to_reach_escape_velocity(velocity, time, acceleration)
    '''
    def cruising_velocity_two_planets(self, planet1: Planet, planet2: Planet):
        """
        Returns the cruising velocity in the journey between two planets
        :param planet1: Planet1
        :param planet2: Planet2
        :return: The cruising velocity
        """
        escape_velocity_planet1 = self.calculate_the_escape_velocity_from_file(planet1)
        escape_velocity_planet2 = self.calculate_the_escape_velocity_from_file(planet2)
        cruising_velocity = max(escape_velocity_planet1, escape_velocity_planet2)
        return cruising_velocity
    '''

    def height_in_a_triangle(self, a, b, c) -> float:
        """
        Calculates the height in a triangle where the sides are known
        :param a: First side
        :param b: Second side
        :param c: Third side
        :return: The height of the triangle perpendicular to c
        """
        if a + b <= c or b + c <= a or a + c <= b:
            raise ValueError("The triangle is not a valid one")
        perimeter = a + b + c
        p = perimeter / 2
        area_squared = p * (p - a) * (p - b) * (p - c)
        area = math.sqrt(area_squared)
        return 2 * area / c

    def time_if_velocity_and_distance_are_known(self, velocity: float, distance: float) -> float:
        """
        Calculates the time if the distance and the velocity are known
        :param velocity: The velocity in m/s
        :param distance: The distance in km
        :return: The time
        """
        return distance * 1000 / velocity

    def cos_theorem_angle(self, a, b, c) -> float:
        """
        Finds the angle A
        :param a: side a
        :param b: side b
        :param c: side c
        :return: The angle A
        """
        if a + b <= c or b + c <= a or a + c <= b:
            raise ValueError("The triangle is not a valid one")
        cosA = (b*b + c*c - a*a) / (2*b*c)
        A = math.degrees(math.acos(cosA))
        return A

    def angles_if_sides_are_known(self, a, b, c):
        """
        Returns the angles in a triangle where the sides are known
        :param a: The length of side a
        :param b: The length of side b
        :param c: The length of side c
        :return: The angles
        """
        if a + b <= c or b + c <= a or a + c <= b:
            raise ValueError("The triangle is not a valid one")
        A = self.cos_theorem_angle(a, b, c)
        B = self.cos_theorem_angle(b, a, c)
        C = self.cos_theorem_angle(c, a, b)
        return A, B, C

    def cos_theorem_side(self, a, b, C) -> float:
        """
        Finds the side c
        :param a: Side a
        :param b: Side b
        :param C: Angle between a and b
        :return: Lenght of the side c
        """
        if C > 180:
            raise ValueError("The angle is not a valid one")
        c_squared = a * a + b * b - 2 * a * b * math.cos(radians(C))
        c = math.sqrt(c_squared)
        return c

    def angular_position_point(self, known_angular_position, angle, add_angle):
        """
        Returns the angular position of a point in space if its angle to a point with a known angular position is known
        :param add_angle: This parameter tells whether the angle should be added or not
        :param known_angular_position: The angular position of the point with a known angular position
        :param angle: The angle
        :return: The angular position of the point
        """
        if known_angular_position > 360:
            raise ValueError("The angular position is not a valid one")
        if angle > 360:
            raise ValueError("The angle is not a valid one")

        if add_angle == True:
            if known_angular_position + angle >= 360:
                angular_position = known_angular_position + angle - 360
            else:
                angular_position = known_angular_position + angle

        else:
            if known_angular_position - angle < 0:
                angular_position = known_angular_position - angle + 360
            else:
                angular_position = known_angular_position - angle

        return angular_position

    def pythagorean_theorem_side(self, other_side, hypotenuse):
        """
        Returns a side in a triangle if the hypotenuse and the other side are known
        :param other_side: The other side
        :param hypotenuse: The hypotenuse
        :return: The side
        """
        side_squared = hypotenuse * hypotenuse - other_side * other_side
        side = math.sqrt(side_squared)
        return side

    def intersection_intervals(self, a, b, c, d):
        """
        Returns whether the two intervals intersect
        :param a: Left side of the first interval
        :param b: Right side of the first interval
        :param c: Left side of the second interval
        :param d: Right side of the second interval
        :return: True/False
        """
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c

        if b < c or d < a:
            return False
        return True

    def intersection_angular_intervals(self, a, b, c, d):
        """
        Returns wheter the two angular intervals intersect
        :param a: Left side of the first angular interval
        :param b: Right side of the first angular interval
        :param c: Left side of the second angular interval11
        :param d: Right side of the second angular interval
        :return: True/False
        """
        if not 0 <= a <= 360:
            raise ValueError("The left side of the first angular interval is not a valid one")
        if not 0 <= b <= 360:
            raise ValueError("The right side of the first angular interval is not a valid one")
        if not 0 <= c <= 360:
            raise ValueError("The left side of the second angular interval is not a valid one")
        if not 0 <= d <= 360:
            raise ValueError("The right side of the second angular interval is not a valid one")

        if abs(a - b) <= 180 and abs(c - d) <= 180:
            return self.intersection_intervals(a, b, c, d)

        elif abs(a - b) > 180 and abs(c - d) > 180:
            return True

        elif (b < c and a > d) or (d < a and c > b):
            return False
        return True

    def angle_between_2_ang_pos(self, angular_position1, angular_position2):
        """
        Returns the angle between the two known angular positions
        :param angular_position1: The first known angular position
        :param angular_position2: The second known angular position
        :return: The angle between the two known angular positions
        """
        if angular_position1 > 360:
            raise ValueError("The first angular position is not a valid one")
        if angular_position2 > 360:
            raise ValueError("The second angular position is not a valid one")

        result = abs(angular_position1 - angular_position2)
        return min(result, 360 - result)