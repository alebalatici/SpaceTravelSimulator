import math
from functools import total_ordering
from math import radians
from source.core import Calculations
from domain.Planet import Planet
from domain.Rocket import Rocket
class ServicesCalculations:
    def __init__(self):
        self.__calc = Calculations()

    def escape_velocity_planet(self, planet: Planet) -> float:
        """
        Calculates the escape velocity given the planet
        :param planet: the planet given
        :return: the escape velocity
        """
        diameter = planet.diameter
        diameter = self.__calc.convert_kilometres_to_metres(diameter)
        earths = planet.mass
        kilograms = self.__calc.convert_earths_to_kilograms(earths)
        return self.__calc.calculate_the_escape_velocity(diameter, kilograms)

    def time_escape_velocity(self, planet: Planet, rocket: Rocket) -> float:
        """
        Calculates the time needed to reach the escape velocity
        :param planet: the planet
        :param rocket: the rocket
        :return: the time needed to reach the escape velocity
        """
        escape_velocity = self.escape_velocity_planet(planet)
        number_of_engines = rocket.number_of_engines
        acceleration_per_engine = rocket.acceleration_per_engine
        return self.__calc.calculate_time_needed_to_reach_escape_velocity(escape_velocity, number_of_engines, acceleration_per_engine)

    def distance_escape_velocity(self, starting_velocity: float, planet: Planet, rocket: Rocket) -> float:
        """
        Calculates the distance needed to reach the escape velocity
        :param planet: the planet
        :param rocket: the rocket
        :return: the distance needed to reach the escape velocity
        """
        time = self.time_escape_velocity(planet, rocket)
        acceleration = rocket.number_of_engines * rocket.acceleration_per_engine
        return self.__calc.calculate_distance_needed_to_reach_escape_velocity(starting_velocity, time, acceleration)

    def distance_centre_escape_velocity(self, starting_velocity: float, planet: Planet, rocket: Rocket) -> float:
        """
        Calculates the distance needed to reach the escape velocity from the centre of the planet
        :param starting_velocity: the starting velocity
        :param planet: the planet
        :param rocket: the rocket
        :return: the distance needed to reach the escape velocity from the centre of the planet
        """
        return self.__calc.convert_kilometres_to_metres(planet.diameter) / 2 + self.distance_escape_velocity(starting_velocity, planet, rocket)

    def time_cruising_velocity(self, planet1: Planet, planet2: Planet, rocket):
        """
        Calculates needed to reach the cruising velocity in the journey between two planets
        :param planet1: The fisrt planet
        :param planet2: The second planet
        :param rocket: The rocket
        :return: The time needed to reach the cruising velocity, the planet with the maximum escape velocity
        """
        escape_velocity_planet1 = self.escape_velocity_planet(planet1)
        escape_velocity_planet2 = self.escape_velocity_planet(planet2)
        escape_velocity = max(escape_velocity_planet1, escape_velocity_planet2)
        if escape_velocity == escape_velocity_planet1:
            return self.time_escape_velocity(planet1, rocket)
        return self.time_escape_velocity(planet2, rocket)


    def maximum_escape_velocity(self, planet1: Planet, planet2: Planet):
        """
        Determines which planet has the maximum escape velocity
        :param planet1: Planet1
        :param planet2: Planet2
        :return: planet which has the maximum escape velocity
        """
        escape_velocity_planet1 = self.escape_velocity_planet(planet1)
        escape_velocity_planet2 = self.escape_velocity_planet(planet2)
        escape_velocity = max(escape_velocity_planet1, escape_velocity_planet2)
        if escape_velocity == escape_velocity_planet1:
            return planet1
        return planet2

    def cruising_velocity(self, planet1: Planet, planet2: Planet):
        """
        Calculates the cruising velocity between the two planets
        :param planet1: Planet1
        :param planet2: Planet2
        :return: The cruising velocity
        """
        planet = self.maximum_escape_velocity(planet1, planet2)
        return self.escape_velocity_planet(planet)

    def distance_centre_planets_km(self, planet1: Planet, planet2: Planet):
        """
        Calculates the distance between the two planet's centres
        :param planet1: Planet1
        :param planet2: Planet2
        :return: The distance between the two planets' centres
        Note: The planets are aligned
        """
        return abs(planet1.orbital_radius - planet2.orbital_radius) * self.__calc.AU

    def cruising_distance(self, planet1: Planet, planet2: Planet, rocket: Rocket):
        """
        Calculates the cruising distance in km
        :param planet1: Planet1
        :param planet2: Planet2
        :param rocket: Rocket
        :return: Cruising distance
        """
        planet = self.maximum_escape_velocity(planet1, planet2)
        return self.distance_centre_planets_km(planet1, planet2) - planet1.diameter/2 - planet2.diameter/2 - 2 * ((self.distance_escape_velocity(0, planet, rocket)) / 1000)

    def cruising_time(self, planet1: Planet, planet2: Planet, rocket: Rocket):
        """
        Calculates the cruising time
        :param planet1: Planet1
        :param planet2: Planet2
        :param rocket: Rocket
        :return: Cruising time
        """
        cruising_distance = self.cruising_distance(planet1, planet2, rocket)
        return self.__calc.convert_kilometres_to_metres(cruising_distance) / self.cruising_velocity(planet1, planet2)

    def total_cruising_time(self, planet1: Planet, planet2: Planet, rocket: Rocket):
        """
        Calculates the total cruising time
        :param planet1: Planet1
        :param planet2: Planet2
        :param rocket: Rocket
        :return: The total cruising time
        """
        return self.cruising_time(planet1, planet2, rocket) + 2 * self.time_cruising_velocity(planet2, planet1, rocket)


    def angular_position(self, planet: Planet, number_of_days: int) -> float:
        """
        Returns the angular position of a planet after a given number of days
        :param planet: Planet
        :param number_of_days: The number of days
        :return: The angular position
        """
        if number_of_days % planet.period == 0:
            return 0
        while number_of_days > planet.period:
            number_of_days = number_of_days - planet.period
        return number_of_days * 360 / planet.period

    def angle_between_two_planets(self, planet1: Planet, planet2: Planet, days: int) -> float:
        """
        Returns the angle between the two planets
        :param planet1: Planet1
        :param planet2: Planet2
        :param days: The number of days
        :return: The angle between the two planets' centres
        """
        ang_pos_planet1 = self.angular_position(planet1, days)
        ang_pos_planet2 = self.angular_position(planet2, days)
        result = abs(ang_pos_planet1 - ang_pos_planet2)
        return min(result, 360 - result)

    def distance_centres_planets_km_not_aligned(self, planet1: Planet, planet2: Planet, days: int) -> float:
        """
        Returns the distance between the two planets
        :param planet1: Planet1
        :param planet2: Planet2
        :return: The distance between the two planets' centres
        """
        angle = self.angle_between_two_planets(planet1, planet2, days)
        p1 = planet1.orbital_radius
        p2 = planet2.orbital_radius
        # distance_squared = p1 * p1 + p2 * p2 - 2 * p1 * p2 * math.cos(radians(angle))
        # distance = math.sqrt(distance_squared)
        distance = self.__calc.cos_theorem_side(p1, p2, angle)
        return distance * self.__calc.AU

    def alligned(self, planet1: Planet, planet2: Planet, days) -> float:
        """
        Checks if two planets are alligned after days number of days
        :param planet1: Planet1
        :param planet2: Planet2
        :param days: The number of days
        :return: True if the planets are alligned, False otherwise
        """
        return abs(self.angular_position(planet1, days) - self.angular_position(planet2, days)) < 1e-6

    def minimum_distance(self, planet1: Planet, planet2: Planet, days: int) -> float:
        """
        Returns the minimum distance between the two planets after days number of days
        :param planet1: Planet1
        :param planet2: Planet2
        :param days: The number of days
        :return: The minimum distance
        Note: The planets can be either aligned or not aligned
        """
        radius_sum_km = planet1.diameter / 2 + planet2.diameter / 2
        if self.alligned(planet1, planet2, days):
            return self.distance_centre_planets_km(planet1, planet2) - radius_sum_km

        else:
            return self.distance_centres_planets_km_not_aligned(planet1, planet2, days) - radius_sum_km

    def distance_planets_centre_and_journey(self, planet1: Planet, planet2: Planet, planet3: Planet, days: int) -> float:
        """
        Returns the distance between the two planets after days number of days
        :param planet1: Planet1
        :param planet2: Planet2
        :param planet3: Planet3
        :param days: The number of days
        :return: The distance between a planet's centre and the journey between the first two planets
        Note: Mathematically, this function returns the distance between a point and a side in space
        """
        a = self.minimum_distance(planet1, planet3, days)
        b = self.minimum_distance(planet2, planet3, days)
        c = self.minimum_distance(planet1, planet2, days)
        distance = self.__calc.height_in_a_triangle(a, b, c)
        return distance


    def intersects_a_planet(self, planet1: Planet, planet2: Planet, list_of_planets: list, days: int) -> float:
        """
        Checks whether the journey between the two planets intersects other planets after days number of days
        :param planet1: Planet1
        :param planet2: Planet2
        :param list_of_planets: The list of planets
        :param days: The number of days
        :return: True/False
        """
        left = min(planet1.orbital_radius, planet2.orbital_radius)
        right = max(planet1.orbital_radius, planet2.orbital_radius)
        for planet in list_of_planets:
            if left < planet.orbital_radius < right:
                if self.distance_planets_centre_and_journey(planet1, planet2, planet, days) <= planet.diameter / 2:
                    return True
        return False

    def find_the_optimal_window(self, planet1, planet2, list_of_planets, days):
        """
        Returns the optimal window for a journey between the two planets in days, the distance of that journey in km, and whether the planets are aligned
        :param planet1: Planet1
        :param planet2: Planet2
        :param list_of_planets: The list of planets
        :param days: The starting number of days
        :return: The optimal window for a journey between the two planets in days, the distance of that journey in km, and whether the planets are aligned
        """
        minimum = math.inf
        days_minimum = -1
        aligned = False
        p1_degrees = -1
        p2_degrees = -1
        for i in range(1, 365 * 10):
            if self.intersects_a_planet(planet1, planet2, list_of_planets, i + days):
                continue
            else:
                if self.minimum_distance(planet1, planet2, i + days) < minimum:
                    minimum = self.minimum_distance(planet1, planet2, i + days)
                    days_minimum = i
                    aligned = self.alligned(planet1, planet2, i + days)
                    p1_degrees = self.angular_position(planet1, i + days)
                    p2_degrees = self.angular_position(planet2, i + days)

        return days_minimum, minimum, aligned, p1_degrees, p2_degrees

    def cruising_parameters(self, planet1: Planet, planet2: Planet, rocket, days: int):
        """
        Returns the cruising parameters for the journey between two planets
        :param planet1: Planet1
        :param planet2: Planet2
        :param rocket: The rocket
        :param days: The number of days since the planets were alligned
        :param days_since_travelling: The number of days since the start of our travel
        :return: The number of cruising days, distance that the planet has to do in a day, the total distance
        """
        #this is the distance between the planets, does not matter if they are aligned or not
        distance = self.minimum_distance(planet1, planet2, days)
        planet = self.maximum_escape_velocity(planet1, planet2)
        #this is the cruising velocity
        cruising_velocity = self.escape_velocity_planet(planet)
        #this is the distance needed to reach the escape velocity
        distance_to_reach = self.distance_escape_velocity(0, planet, rocket)
        #this is the cruising distance
        cruising_distance = distance - 2 * distance_to_reach

        #this is the cruising time in seconds needed for the journey
        cruising_time = self.__calc.time_if_velocity_and_distance_are_known(cruising_velocity, cruising_distance)
        #this is the total days needed for the cruising part of the journey
        cruising_days = cruising_time // 86400
        cruising_days = int(cruising_days)

        if cruising_days == 0:
            distance_in_a_day = cruising_distance
        else:
            distance_in_a_day = cruising_distance / cruising_days

        return cruising_days, distance_in_a_day, distance

    def planets_betwen(self, planet1: Planet, planet2: Planet, list_of_planets: list):
        """
        Returns the list of planets between two planets
        :param planet1: Planet1
        :param planet2: Planet2
        :param list_of_planets: The list of all planets
        :return: The list of planets between Planet1 and Planet2
        """
        left = min(planet1.orbital_radius, planet2.orbital_radius)
        right = max(planet1.orbital_radius, planet2.orbital_radius)
        planets_between = []
        for planet in list_of_planets:
            if left < planet.orbital_radius < right:
                planets_between.append(planet)
        return planets_between

    def distance_interval_subjourney(self, planet1, planet2, rocket, days_since_travelling, distance_in_a_day, distance):
        """
        Returns the distance that the rocket has travelled until this day, the distance that it has to travel from tomorrow until the end of the journey and the distance that it has to travel in a day
        :param distance: The total distance that the rocket has to travel
        :param distance_in_a_day: The distance that the rocket travels in a day
        :param planet1: Planet1
        :param planet2: Planet2
        :param rocket: The rocket
        :param days_since_travelling: The number of days since the start of our travel
        :return: The distance that the rocket has travelled until this day, the distance that it has to travel from tomorrow until the end of the journey and the distance that it has to travel in a day
        """
        #the redius of the starting planet
        radius1 = planet1.diameter / 2
        #the radius of the second planet
        radius2 = planet2.diameter / 2
        #the planet that has the maximum escape velocity
        planet = self.maximum_escape_velocity(planet1, planet2)
        #the distance needed to reach that escape velocity
        dist_esc_velocity = self.distance_escape_velocity(0, planet, rocket)

        distance_yet_travelled_center = days_since_travelling * distance_in_a_day + dist_esc_velocity + radius1
        distance_to_travel_center = radius2 + radius1 + distance - distance_in_a_day - distance_yet_travelled_center
        return distance_yet_travelled_center, distance_to_travel_center, distance_in_a_day

    def angle_sides_interval_subjourney(self, planet1: Planet, planet2: Planet, days, rocket, days_since_travelling, distance_in_a_day, distance_surface):
        """
        Returns the interval of the angular position of the starting point of the journey in a day and the ending point of a journey in a day
        :param distance_surface: The distance of the surface that the rocket travels
        :param distance_in_a_day: The distance of the journey in a day
        :param planet1: Planet1
        :param planet2: Planet2
        :param days: The number of days since the start of the simulation (ex: 100 + how_many_days_after_we_found_the_optimal_window)
        :param rocket: The rocket
        :param days_since_travelling: The number of days since the start of the journey
        :return: The intervali sides
        """
        dist_yet_completed_center, dist_to_complete_center,_ = self.distance_interval_subjourney(planet1, planet2, rocket, days_since_travelling, distance_in_a_day, distance_surface)

        if self.alligned(planet1, planet2, days):
            left_angular_position = self.angular_position(planet1, days)
            right_angular_position = left_angular_position
            return left_angular_position, right_angular_position, dist_yet_completed_center, dist_yet_completed_center + distance_in_a_day

        else:
            distance = self.distance_centres_planets_km_not_aligned(planet1, planet2, days)
            #orbital radius in km
            distance_p1 = planet1.orbital_radius * self.__calc.AU
            distance_p2 = planet2.orbital_radius * self.__calc.AU
            #the angles of the triangle made by the two planets and the center of our solar system
            p1, p2, d = self.__calc.angles_if_sides_are_known(distance_p1, distance_p2, distance)

            #these will be the distances from center to the starting point of the journey in a given day and the ending point of the journey in a given day
            side_1 = self.__calc.cos_theorem_side(distance_p1, dist_yet_completed_center, p2)
            side_2 = self.__calc.cos_theorem_side(distance_p2, dist_to_complete_center, p1)

            #these will be the two angles between the planets and the points of the journey in a given day
            angle1 = self.__calc.cos_theorem_angle(dist_yet_completed_center, distance_p1, side_1)
            angle2 = self.__calc.cos_theorem_angle(dist_to_complete_center, distance_p2, side_2)

            #these are the angular positions of the two planets in the given day
            p1_a = self.angular_position(planet1, days)
            p2_a = self.angular_position(planet2, days)

            #these are the angular positions of the starting point and the ending point of the journey
            pos_ang_1, pos_ang_2 = self.angular_positions_journey(p1_a, p2_a, angle1, angle2)

            left_angular_position = min(pos_ang_1, pos_ang_2)
            right_angular_position = max(pos_ang_1, pos_ang_2)
            left_side_position = min(side_1, side_2)
            right_side_position = max(side_1, side_2)
            return left_angular_position, right_angular_position, left_side_position, right_side_position
            #return pos_ang_1, pos_ang_2, side_1, side_2

    def angular_positions_journey(self, p1_a, p2_a, angle1, angle2):
        """
        Determines the angular positions of the journey given the angular positions of the planets and the angles between the planets and the two point of the journey
        :param p1_a: The angular position of the first planet
        :param p2_a: The angular position of the second planet
        :param angle1: The angle between the first planet and the start of the journey
        :param angle2: The angle between the second planet and the end of the journey
        :return: The angular positions of the journey
        """
        substract_angle = True
        if abs(p1_a - p2_a) <= 180:
            if p1_a < p2_a:
                substract_angle = False
        else:
            if p1_a > p2_a:
                substract_angle = False

        pos_ang_1 = self.__calc.angular_position_point(p1_a, angle1, not substract_angle)
        pos_ang_2 = self.__calc.angular_position_point(p2_a, angle2, substract_angle)
        return pos_ang_1, pos_ang_2

    def angle_sides_interval_planet(self, planet: Planet, days):
        """
        Returns the angular positions of each tanget and the lenght of the tangents of a planet after a given number of days
        :param planet: The planet
        :param days: The given number of days
        :return: The angular positions of each of the tangents and the lenght of the tangents of a planet after a given number of days
        """

        radius = planet.diameter / 2
        orbital_radius = planet.orbital_radius * self.__calc.AU

        tangent_length = self.__calc.pythagorean_theorem_side(radius, orbital_radius)
        angular_position = self.angular_position(planet, days)

        angle = self.__calc.cos_theorem_angle(radius, orbital_radius, tangent_length)

        pos_ang_1 = self.__calc.angular_position_point(angular_position, angle, True)
        pos_ang_2 = self.__calc.angular_position_point(angular_position, angle, False)

        left_angular_position = min(pos_ang_1, pos_ang_2)
        right_angular_position = max(pos_ang_1, pos_ang_2)

        return left_angular_position, right_angular_position, tangent_length

    def intersects_a_planet_in_a_given_day(self, planet1: Planet, planet2: Planet, planet3: Planet, days, rocket, days_since_travelling, distance_in_a_day, distance_surface):
        planet_left_angular_position, planet_right_angular_position, tangent_length = self.angle_sides_interval_planet(planet3, days)
        journey_left_angular_position, journey_right_angular_position, left_side_position, right_side_position = self.angle_sides_interval_subjourney(planet1, planet2, days, rocket, days_since_travelling, distance_in_a_day, distance_surface)
        #checking the interval for length
        if left_side_position < tangent_length < right_side_position:
            #checking the interval for angular position
            return self.__calc.intersection_angular_intervals(planet_left_angular_position, planet_right_angular_position, journey_left_angular_position, journey_right_angular_position)
        return False

    def find_the_optimal_window_2(self, planet1: Planet, planet2: Planet, rocket, days: int, list_of_planets: list):
        minimum = math.inf
        days_minimum = -1
        aligned = False
        p1_degrees = -1
        p2_degrees = -1
        #the list of planets in between the starting planet and the destination planet
        planets_between = self.planets_betwen(planet1, planet2, list_of_planets)
        #for every day of the journey
        for i in range(1, 365 * 10):
            # calculating the distance between the starting planet and the destination planet, comparing it with minimum distance
            distance = self.minimum_distance(planet1, planet2, i + days)
            if distance < minimum:
                intersect = False
                # determining the cruising parameters
                cruising_days, distance_in_a_day, _ = self.cruising_parameters(planet1, planet2, rocket, days + i)
                # checking for every day of the cruise if our journey intersects another planet
                for j in range(int(cruising_days), intersect == False):
                    #for every planet:
                    for planet in planets_between:
                        if self.intersects_a_planet_in_a_given_day(planet1, planet2, planet, days, rocket, i + j, distance_in_a_day, distance):
                            intersect = True
                            break
                    if intersect:
                        break

                if not intersect:
                    #minimum = self.minimum_distance(planet1, planet2, i + days)
                    minimum = distance
                    days_minimum = i
                    aligned = self.alligned(planet1, planet2, i + days)
                    p1_degrees = self.angular_position(planet1, i + days)
                    p2_degrees = self.angular_position(planet2, i + days)

        return days_minimum, minimum, aligned, p1_degrees, p2_degrees

    def find_angular_positions_journey_2(self, planet1, planet2, days):
        distance_p1 = planet1.orbital_radius * self.__calc.AU
        distance_p2 = planet2.orbital_radius * self.__calc.AU

        if self.alligned(planet1, planet2, days):
            left_angular_position = self.angular_position(planet1, days)
            right_angular_position = left_angular_position
            return left_angular_position, right_angular_position, min(distance_p1, distance_p2), max(distance_p1, distance_p2)

        else:
            distance = self.distance_centres_planets_km_not_aligned(planet1, planet2, days)
            # orbital radius in km
            # the angles of the triangle made by the two planets and the center of our solar system
            p1, p2, d = self.__calc.angles_if_sides_are_known(distance_p1, distance_p2, distance)
            radius1 = planet1.diameter / 2
            radius2 = planet2.diameter / 2
            side_1 = self.__calc.cos_theorem_side(distance_p1, radius1, p2)
            side_2 = self.__calc.cos_theorem_side(distance_p2, radius2, p1)
            ang_pos1 = self.angular_position(planet1, days)
            ang_pos2 = self.angular_position(planet2, days)
            return min(ang_pos1, ang_pos2), max(ang_pos1, ang_pos2), min(side_1, side_2), max(side_1, side_2)

    def intersects_a_planet_in_a_given_day_2(self, planet1: Planet, planet2: Planet, planet3: Planet, days):
        planet_left_angular_position, planet_right_angular_position, tangent_length = self.angle_sides_interval_planet(planet3, days)
        journey_left_angular_position, journey_right_angular_position, left_side_position, right_side_position = self.find_angular_positions_journey_2(planet1, planet2, days)
        if left_side_position < tangent_length < right_side_position:
            return self.__calc.intersection_angular_intervals(planet_left_angular_position, planet_right_angular_position, journey_left_angular_position, journey_right_angular_position)
        return False

    def find_the_optimal_window_1_optimised(self, planet1: Planet, planet2: Planet, days: int, list_of_planets: list):
        minimum = math.inf
        days_minimum = -1
        aligned = False
        p1_degrees = -1
        p2_degrees = -1
        # the list of planets in between the starting planet and the destination planet
        planets_between = self.planets_betwen(planet1, planet2, list_of_planets)
        # for every day of the journey
        for i in range(1, 365 * 10):
            # calculating the distance between the starting planet and the destination planet, comparing it with minimum distance
            distance = self.minimum_distance(planet1, planet2, i + days)
            intersects = False
            if distance < minimum:
                for planet in planets_between:
                    if self.intersects_a_planet_in_a_given_day_2(planet1, planet2, planet, i + days):
                        intersects = True
                        break

                if not intersects:
                    minimum = distance
                    days_minimum = i
                    aligned = self.alligned(planet1, planet2, i + days)
                    p1_degrees = self.angular_position(planet1, i + days)
                    p2_degrees = self.angular_position(planet2, i + days)

        return days_minimum, minimum, aligned, p1_degrees, p2_degrees
