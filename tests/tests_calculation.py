import unittest
from source.core import *
from domain.Planet import Planet
from domain.Rocket import Rocket
from source.services import ServicesCalculations
from repo.repository_solar_system import RepositoryFileSolarSystem
class Stage1Tests(unittest.TestCase):
    def setUp(self):
        print("SetUp")
        self.__srv = ServicesCalculations()
        self.__repo = RepositoryFileSolarSystem("tests/Test_Solar_System.txt", "tests/Test_Planetary_Data.txt")
        self.__calc = Calculations()

    def tearDown(self):

        print("TearDown")

    def test_convert_kilometres_to_metres(self):
        self.assertEqual(self.__calc.convert_kilometres_to_metres(1), 1000)
        self.assertEqual(self.__calc.convert_kilometres_to_metres(2), 2000)
        self.assertEqual(self.__calc.convert_kilometres_to_metres(1.312435465), 1312.435465)
        self.assertEqual(self.__calc.convert_kilometres_to_metres(0.324354), 324.354)
        self.assertEqual(self.__calc.convert_kilometres_to_metres(12345.34), 12345340)

    """
    def test_calculate_the_escape_velocity(self):
        calc = Calculations()
        self.assertEqual(round(calc.calculate_the_escape_velocity(12345, 100000000000), 5), 0.03287)
        self.assertEqual(round(calc.calculate_the_escape_velocity(12, 100000), 3), 0.001)
        self.assertEqual(round(calc.calculate_the_escape_velocity(120000000000, 10000000000000000), 5), 0.00333)
        self.assertEqual(round(calc.calculate_the_escape_velocity(12000000000000, 12000000000000000000), 5), 0.01155)
        self.assertEqual(round(calc.calculate_the_escape_velocity(129099, 1200000000), 7), 0.0011135)
    """
    def test_convert_from_earths_to_kilograms(self):
        self.assertEqual(self.__calc.convert_earths_to_kilograms(0.06), 3.58332e+23)
        self.assertEqual(self.__calc.convert_earths_to_kilograms(0.1), 5.9722000000000005e+23)
        self.assertEqual(self.__calc.convert_earths_to_kilograms(2), 1.19444e+25)
        self.assertEqual(self.__calc.convert_earths_to_kilograms(0.002), 1.1944400000000002e+22)
        self.assertEqual(self.__calc.convert_earths_to_kilograms(576), 3.4399872e+27)

    def test_calculate_the_escape_velocity_from_file(self):
        p1 = Planet("Mercury", 4900, 0.06)
        self.assertEqual(math.ceil(self.__srv.escape_velocity_planet(p1)), 4418)
        p2 = Planet("Venus", 12100, 0.82)
        self.assertEqual(math.ceil(self.__srv.escape_velocity_planet(p2)), 10392)
        p3 = Planet("Earth", 12800, 1)
        self.assertEqual(math.ceil(self.__srv.escape_velocity_planet(p3)), 11158)

    def test_calculate_time_needed_to_reach_escape_velocity(self):
        self.assertEqual(math.floor(self.__calc.calculate_time_needed_to_reach_escape_velocity(11183, 4, 10)), 279)
        self.assertEqual(math.floor(self.__calc.calculate_time_needed_to_reach_escape_velocity(4418, 4, 10)), 110)
        self.assertEqual(math.floor(self.__calc.calculate_time_needed_to_reach_escape_velocity(10392, 4, 10)), 259)

    def test_calculate_distance_needed_to_reach_escape_velocity(self):
        self.assertEqual(self.__calc.calculate_distance_needed_to_reach_escape_velocity(0, 279, 40), 1556820)

    def test_calculate_distance_needed_to_reach_escape_velocity_from_centre(self):
        self.assertEqual(self.__calc.calculate_distance_needed_to_reach_escape_velocity_from_centre(0, 279, 40, 12800000), 7956820)

    def test_calculate_distance_centre_planets_km(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        cruising_distance = self.__srv.distance_centre_planets_km(earth,  mars)
        self.assertEqual(round(cruising_distance), 77790893)

    def test_calculate_cruising_velocity(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        earth_escape_velocity = self.__srv.escape_velocity_planet(earth)
        cruising_velocity = self.__srv.cruising_velocity(earth, mars)
        self.assertEqual(round(cruising_velocity), 11157)

    def test_angular_position(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        angular_position = self.__srv.angular_position(earth, 200)
        angular_position = round(angular_position, 2)
        self.assertEqual(angular_position, 197.26)
        angular_position = self.__srv.angular_position(earth, 365)
        self.assertEqual(angular_position, 0)
        angular_position = self.__srv.angular_position(earth, 0)
        self.assertEqual(angular_position, 0)
        angular_position = self.__srv.angular_position(earth, 365 * 2)
        self.assertEqual(angular_position, 0)

    def test_height_in_a_triangle(self):
        result1 = self.__calc.height_in_a_triangle(446, 243, 425)
        result1 = round(result1, 1)
        self.assertEqual(result1, 238.2)
        result2 = self.__calc.height_in_a_triangle(124465768723345, 423564777575456, 324534664675789)
        result2 = round(result2)
        self.assertEqual(result2, 85689748852982)
        with self.assertRaises(ValueError):
            result3 = self.__calc.height_in_a_triangle(0, 5, 9)

    def test_alligned(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        self.assertEqual(self.__srv.alligned(earth, mars, 2336), False)
        self.assertEqual(self.__srv.alligned(earth, mars, 0), True)

        uranus = Planet("Uranus", 52400, 15, 30660, 19.18)
        neptune = Planet("Neptune", 48400, 17, 60148, 30.06)
        self.assertEqual(self.__srv.alligned(uranus, neptune, 1), False)

    def test_distance_between_two_planets_centres_not_alligned(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        uranus = Planet("Uranus", 52400, 15, 30660, 19.18)
        neptune = Planet("Neptune", 48400, 17, 60148, 30.06)
        result = self.__srv.distance_centres_planets_km_not_aligned(mars, uranus, 20000)
        result1 = self.__srv.distance_centres_planets_km_not_aligned(earth, neptune, 20000)

    def test_angle_between_two_planets(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        uranus = Planet("Uranus", 52400, 15, 30660, 19.18)
        neptune = Planet("Neptune", 48400, 17, 60148, 30.06)
        angle = self.__srv.angle_between_two_planets(earth, mars, 20000)
        angle = round(angle, 2)
        self.assertEqual(angle, 114.32)
        angle1 = self.__srv.angle_between_two_planets(earth, mars, 50056)
        angle1 = round(angle1, 2)
        self.assertEqual(angle1, 100.08)
        angle2 = self.__srv.angle_between_two_planets(uranus, neptune, 2345465)
        angle2 = round(angle2, 2)
        self.assertEqual(angle2, 178.46)

    def test_cruising_parameters(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        self.assertEqual(self.__srv.minimum_distance(earth, mars, 100), 164369574.1075016)
        rocket = Rocket(4, 10)
        cruising_days, distance_in_a_day, distance = self.__srv.cruising_parameters(earth, mars, rocket, 100)
        self.assertEqual(distance, 164369574.1075016)
        self.assertEqual(cruising_days, 167)

        planet = self.__srv.maximum_escape_velocity(earth, mars)
        dist_esc_vel = self.__srv.distance_escape_velocity(0, planet, rocket)
        cruising_distance = distance - 2 * dist_esc_vel
        self.assertEqual(distance_in_a_day * cruising_days, cruising_distance)

    def test_planets_between(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        neptune = Planet("Neptune", 48400, 17, 60148, 30.06)
        list_of_planets = self.__repo.get_all_planets_extended()
        planets = self.__srv.planets_betwen(earth, neptune, list_of_planets)
        self.assertEqual(len(planets), 4)

    def test_distance_interval_subjourney(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        rocket = Rocket(4, 10)
        _, distance_in_a_day, distance = self.__srv.cruising_parameters(earth, mars, rocket, 100)
        dist_yet_travelled_center, dist_to_travel_center, dist_day = self.__srv.distance_interval_subjourney(earth, mars, rocket, 4, distance_in_a_day, distance)
        sum = dist_yet_travelled_center + dist_to_travel_center + dist_day
        sum = sum - earth.diameter / 2 - mars.diameter / 2
        self.assertEqual(sum, distance)

    def test_cos_theorem_angle(self):
        A = self.__calc.cos_theorem_angle(34546, 13243, 45566)
        self.assertEqual(28.738, round(A, 3))
        B = self.__calc.cos_theorem_angle(13243, 34546, 45566)
        self.assertEqual(10.621, round(B, 3))
        C = self.__calc.cos_theorem_angle(45566, 34546, 13243)
        self.assertEqual(140.641, round(C, 3))
        total = A + B + C
        self.assertEqual(total, 180)

    def test_angles_if_sides_are_known(self):
        A, B, C = self.__calc.angles_if_sides_are_known(4567, 3245, 2344)
        self.assertEqual(round(A, 3), 108.524)
        self.assertEqual(round(B, 3), 42.355)
        self.assertEqual(round(C, 3), 29.121)
        total = A + B + C
        self.assertEqual(total, 180)

    def test_cos_theorem_side(self):
        a = self.__calc.cos_theorem_side(324546, 546567, 60)
        self.assertEqual(round(a, 5),  476108.66199)
        A, B, C = self.__calc.angles_if_sides_are_known(a, 324546, 546567)
        self.assertEqual(round(A), 60)
        total = A + B + C
        self.assertEqual(total, 180)

    def test_angular_position_point(self):
        a1 = self.__calc.angular_position_point(100, 60, True)
        self.assertEqual(a1, 160)
        a2 = self.__calc.angular_position_point(100, 60, False)
        self.assertEqual(a2, 40)
        a3 = self.__calc.angular_position_point(350, 20, True)
        self.assertEqual(a3, 10)
        a4 = self.__calc.angular_position_point(10, 20, False)
        self.assertEqual(a4, 350)

    def test_angle_between_2_ang_pos(self):
        a1 = self.__calc.angle_between_2_ang_pos(10, 20)
        self.assertEqual(a1, 10)
        a2 = self.__calc.angle_between_2_ang_pos(350, 10)
        self.assertEqual(a2, 20)
        a3 = self.__calc.angle_between_2_ang_pos(10, 350)
        self.assertEqual(a3, 20)

    def test_pythagorean_theorem_side(self):
        a1 = self.__calc.pythagorean_theorem_side(4, 5)
        self.assertEqual(a1, 3)
        a2 = self.__calc.pythagorean_theorem_side(4354, 67767)
        self.assertEqual(a2 * a2  + 4354 * 4354, 67767 * 67767)
        a3 = self.__calc.pythagorean_theorem_side(35457, 3243456)
        self.assertEqual(round(a3 * a3 + 35457 * 35457), 3243456 * 3243456)

    def test_angle_sides_interval_planet(self):
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        left_angular_position, right_angular_position, tangent_length = self.__srv.angle_sides_interval_planet(mars, 100)
        angle = self.__calc.angle_between_2_ang_pos(left_angular_position, right_angular_position)

        radius = mars.diameter / 2
        orbital_radius = mars.orbital_radius * self.__calc.AU
        self.assertEqual(radius * radius + tangent_length * tangent_length, orbital_radius * orbital_radius)
        angle_each_triangle = angle / 2
        other_angle = self.__calc.cos_theorem_angle(tangent_length, radius, orbital_radius)
        self.assertEqual(round(angle_each_triangle + other_angle), 90)

    def test_angular_positions_journey(self):
        pos_ang1, pos_ang2 = self.__srv.angular_positions_journey(200, 100, 50, 25)
        self.assertEqual(pos_ang1, 150)
        self.assertEqual(pos_ang2, 125)
        pos_ang1, pos_ang2 = self.__srv.angular_positions_journey(100, 200, 15, 50)
        self.assertEqual(pos_ang1, 115)
        self.assertEqual(pos_ang2, 150)
        pos_ang1, pos_ang2 = self.__srv.angular_positions_journey(30, 340, 20, 10)
        self.assertEqual(pos_ang1, 10)
        self.assertEqual(pos_ang2, 350)
        pos_ang1, pos_ang2 = self.__srv.angular_positions_journey(340, 50, 10, 10)
        self.assertEqual(pos_ang1, 350)
        self.assertEqual(pos_ang2, 40)
        pos_ang1, pos_ang2 = self.__srv.angular_positions_journey(50, 330, 60, 10)
        self.assertEqual(pos_ang1, 350)
        self.assertEqual(pos_ang2, 340)
        pos_ang1, pos_ang2 = self.__srv.angular_positions_journey(50, 350, 10, 20)
        self.assertEqual(pos_ang1, 40)
        self.assertEqual(pos_ang2, 10)
        pos_ang1, pos_ang2 = self.__srv.angular_positions_journey(320, 350, 10, 10)
        self.assertEqual(pos_ang1, 330)
        self.assertEqual(pos_ang2, 340)

    def test_angle_sides_interval_subjourney(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        rocket = Rocket(4, 10)
        #1
        _, distance_in_a_day, distance_surface = self.__srv.cruising_parameters(earth, mars, rocket, 0)

        yt, tt,_ = self.__srv.distance_interval_subjourney(earth, mars, rocket, 0 + 70, distance_in_a_day, distance_surface)

        self.assertEqual(self.__srv.alligned(earth, mars, 0), True)

        left_angular_position, right_angular_position, left_side_position, right_side_position =\
            self.__srv.angle_sides_interval_subjourney(earth, mars, 0, rocket, 70, distance_in_a_day, distance_surface)
        self.assertEqual(left_angular_position, right_angular_position)

        self.assertEqual(left_side_position, yt)
        self.assertEqual(right_side_position, yt + distance_in_a_day)

        #2
        # let's say we found the optimal window after 4 days since the 100-year period
        _, distance_in_a_day, distance_surface = self.__srv.cruising_parameters(earth, mars, rocket, 100 + 4)
        self.assertEqual(self.__srv.alligned(earth, mars, 100 + 4), False)

        # we've been traveling for 5 days
        left_angular_position, right_angular_position, left_side_position, right_side_position = \
            self.__srv.angle_sides_interval_subjourney(earth, mars, 100 + 4, rocket, 5, distance_in_a_day, distance_surface)

        angle = self.__calc.angle_between_2_ang_pos(left_angular_position, right_angular_position)
        test_dist_day = self.__calc.cos_theorem_side(left_side_position, right_side_position, angle)

        test_angle = self.__calc.cos_theorem_angle(distance_in_a_day, left_side_position, right_side_position)

        self.assertAlmostEqual(angle, test_angle)
        self.assertEqual(round(distance_in_a_day, 4), round(test_dist_day, 4))

        #print(left_angular_position, right_angular_position, left_side_position, right_side_position)

    def test_intersection_angular_intervals(self):
        intersect = self.__calc.intersection_angular_intervals(50, 60, 60, 70)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(50, 80, 60, 70)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(50, 60, 100, 110)
        self.assertEqual(intersect, False)
        intersect = self.__calc.intersection_angular_intervals(50, 60, 60, 70)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(60, 50, 60, 70)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(50, 60, 40, 70)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(50, 60, 110, 100)
        self.assertEqual(intersect, False)

        intersect = self.__calc.intersection_angular_intervals(350, 20, 355, 10)
        self.assertEqual(intersect, True)

        intersect = self.__calc.intersection_angular_intervals(350, 10, 60, 70)
        self.assertEqual(intersect, False)
        intersect = self.__calc.intersection_angular_intervals(350, 60, 10, 50)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(350, 60, 10, 70)
        self.assertEqual(intersect, True)

        intersect = self.__calc.intersection_angular_intervals(350, 0, 10, 50)
        self.assertEqual(intersect, False)
        intersect = self.__calc.intersection_angular_intervals(350, 60, 350, 10)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(10, 20, 350, 50)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(10, 60, 350, 50)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(350, 20, 30, 40)
        self.assertEqual(intersect, False)
        intersect = self.__calc.intersection_angular_intervals(350, 20, 10, 30)
        self.assertEqual(intersect, True)
        intersect = self.__calc.intersection_angular_intervals(10, 200, 220, 350)
        self.assertEqual(intersect, True)

    def test_intersects_a_planet_in_a_given_day(self):
        pass

    def test_find_the_optimal_window_2(self):
        earth = Planet("Earth", 12800, 1, 365, 1)
        mars = Planet("Mars", 5800, 0.11, 687, 1.52)
        rocket = Rocket(4, 10)
        list_of_planets = self.__repo.get_all_planets_extended()
        days_minimum, minimum, aligned, p1_degrees, p2_degrees = self.__srv.find_the_optimal_window_2(earth, mars, rocket, 1234, list_of_planets)
        print(days_minimum)
        print(minimum)
        print(p1_degrees)
        print(p2_degrees)
        print(aligned)

if __name__ == '__main__':
    unittest.main()