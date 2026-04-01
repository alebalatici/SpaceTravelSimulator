import unittest
from domain.Planet import Planet
from domain.Rocket import Rocket
class PlanetTest(unittest.TestCase):
    def setUp(self):
        print("SetUp")

    def tearDown(self):
        print("TearDown")

    def test_planet(self):
        p1 = Planet("Pluto", 2450, 0.06)
        p2 = Planet("Venus", 12100, 0.82)
        p3 = Planet("Earth", 12800, 1)

        self.assertEqual(p1.name, "Pluto")
        self.assertEqual(p2.name, "Venus")
        self.assertEqual(p3.name, "Earth")

        self.assertEqual(p1.diameter, 2450)
        self.assertEqual(p2.diameter, 12100)
        self.assertEqual(p3.diameter, 12800)

        self.assertEqual(p1.mass, 0.06)
        self.assertEqual(p2.mass, 0.82)
        self.assertEqual(p3.mass, 1)

    def test_equal(self):
        p1 = Planet("Pluto", 2450, 0.06)
        p2 = Planet("Pluto", 2450, 0.06)
        p3 = Planet("Venus", 12100, 0.82)

        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        self.assertNotEqual(p2, p3)

class RocketTest(unittest.TestCase):
    def setUp(self):
        print("SetUp")

    def tearDown(self):
        print("TearDown")

    def test_rocket(self):
        r1 = Rocket(4, 10)
        r2 = Rocket(4, 20)
        r3 = Rocket(5, 10)
        self.assertEqual(r1.number_of_engines, 4)
        self.assertEqual(r2.number_of_engines, 4)
        self.assertEqual(r3.number_of_engines, 5)

        self.assertEqual(r1.acceleration_per_engine, 10)
        self.assertEqual(r2.acceleration_per_engine, 20)
        self.assertEqual(r3.acceleration_per_engine, 10)

    def test_equal_rocket(self):
        r1 = Rocket(4, 10)
        r2 = Rocket(4, 20)
        r3 = Rocket(4, 10)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1, r3)
        self.assertNotEqual(r2, r3)

if __name__ == "__main__":
    unittest.main()