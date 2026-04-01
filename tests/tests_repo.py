import unittest
from repo.repository_planetary_data import *
from repo.repository_rocket_data import *
from repo.repository_solar_system import *
class TestRepository(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_add_planet(self):
        repo = RepositoryInMemory()
        n = len(repo.get_all_planets())
        p1 = Planet("Pluto", 2450, 0.06)
        p2 = Planet("Venus", 12100, 0.82)
        p3 = Planet("Earth", 12800, 1)
        repo.add_planet(p1)
        self.assertEqual(len(repo.get_all_planets()), n + 1)
        repo.add_planet(p2)
        self.assertEqual(len(repo.get_all_planets()), n + 2)
        repo.add_planet(p3)
        self.assertEqual(len(repo.get_all_planets()), n + 3)
        self.assertEqual(repo.get_all_planets()[n].name, "Pluto")
        self.assertEqual(repo.get_all_planets()[n + 1].diameter, 12100)
        self.assertEqual(repo.get_all_planets()[n + 2].mass, 1)

    def test_find_planet(self):
        repo = RepositoryInMemory()
        n = len(repo.get_all_planets())
        p1 = Planet("Pluto", 2450, 0.06)
        p2 = Planet("Venus", 12100, 0.82)
        p3 = Planet("Earth", 12800, 1)
        repo.add_planet(p1)
        repo.add_planet(p2)
        repo.add_planet(p3)
        planet1 = repo.find_planet("Pluto")
        self.assertEqual(planet1.diameter, 2450)
        self.assertEqual(planet1.mass, 0.06)
        self.assertEqual(p1, planet1)

        planet2 = repo.find_planet("Venus")
        self.assertEqual(planet2.diameter, 12100)
        self.assertEqual(planet2.mass, 0.82)
        self.assertEqual(p2, planet2)

        planet3 = repo.find_planet("Earth")
        self.assertEqual(planet3.diameter, 12800)
        self.assertEqual(planet3.mass, 1)
        self.assertEqual(p3, planet3)

    def test_get_all_planets(self):
        repo = RepositoryInMemory()
        n = len(repo.get_all_planets())
        p1 = Planet("Pluto", 2450, 0.06)
        p2 = Planet("Venus", 12100, 0.82)
        p3 = Planet("Earth", 12800, 1)
        repo.add_planet(p1)
        self.assertEqual(len(repo.get_all_planets()), n + 1)
        repo.add_planet(p2)
        self.assertEqual(len(repo.get_all_planets()), n + 2)
        repo.add_planet(p3)
        self.assertEqual(len(repo.get_all_planets()), n + 3)

class TestRepositoryFile(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.__repo = RepositoryFile("tests/Test_Planetary_Data.txt")

    def tearDown(self):
        print("tearDown")
        with open("tests/Test_Planetary_Data.txt", mode="w", encoding="utf-8") as file:
            fisier_default = open("tests/Default_Planetary_Data.txt", mode="r", encoding="utf-8")
            content = fisier_default.read()
            file.write(content)
            fisier_default.close()

    def test_add_planet(self):
        n = len(self.__repo.get_all_planets())
        p1 = Planet("Uranus1", 52400, 15)
        p2 = Planet("Neptune1", 48400, 17)
        p3 = Planet("Pluto1", 2450, 0.002)

        self.__repo.add_planet(p1)
        self.assertEqual(len(self.__repo.get_all_planets()), n + 1)
        self.__repo.add_planet(p2)
        self.assertEqual(len(self.__repo.get_all_planets()), n + 2)
        self.__repo.add_planet(p3)
        self.assertEqual(len(self.__repo.get_all_planets()), n + 3)

        self.assertEqual(self.__repo.get_all_planets()[n].name, "Uranus1")
        self.assertEqual(self.__repo.get_all_planets()[n + 1].diameter, 48400)
        self.assertEqual(self.__repo.get_all_planets()[n + 2].mass, 0.002)

    def test_find_planet(self):
        p1 = self.__repo.find_planet("Mercury")
        with self.assertRaises(PlanetaAlreadyExistsException):
            self.__repo.add_planet(p1)

        p2 = self.__repo.find_planet("Venus")
        self.assertEqual(p2.diameter, 12100)
        self.assertEqual(p2.mass, 0.82)

        with self.assertRaises(PlanetaDoesNotExistException):
            self.__repo.find_planet("ThisPlanetDoesNotExist")

class TestRepositoryMemoryRocket(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_add_rocket(self):
        repo = RepositoryInMemoryRocket()
        r = Rocket(4, 10)
        repo.add_rocket(r)
        self.assertEqual(repo.get_rocket(), r)
        r1 = Rocket(7, 10)
        with self.assertRaises(RepositoryRocketException):
            repo.add_rocket(r1)

    def test_get_rocket(self):
        repo = RepositoryInMemoryRocket()
        r = Rocket(4, 10)
        repo.add_rocket(r)
        r1 = repo.get_rocket()
        self.assertEqual(r1, r)
        repo.delete_rocket()
        with self.assertRaises(RepositoryRocketException):
            r2 = repo.get_rocket()

    def test_delete_rocket(self):
        repo = RepositoryInMemoryRocket()
        r = Rocket(4, 10)
        with self.assertRaises(RepositoryRocketException):
            repo.delete_rocket()
        repo.add_rocket(r)
        repo.delete_rocket()
        with self.assertRaises(RepositoryRocketException):
            r1 = repo.get_rocket()

class TestRepositoryFileRocket(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.__repo = RepositoryFileRocket("tests/Test_Rocket_Data.txt")

    def tearDown(self):
        print("tearDown")
        with open(f"tests/Test_Rocket_Data.txt", mode="w", encoding="utf-8") as file:
            fisier_default = open("tests/Default_Rocket_Data.txt", mode="r", encoding="utf-8")
            content = fisier_default.read()
            file.write(content)
            fisier_default.close()

    def test_add_rocket(self):
        self.__repo.delete_rocket()
        r = Rocket(4, 10)
        self.__repo.add_rocket(r)
        rocket = self.__repo.get_rocket()
        self.assertEqual(r, rocket)

    def test_get_rocket(self):
        r = self.__repo.get_rocket()
        self.assertEqual(r, Rocket(4, 10))
        self.__repo.delete_rocket()
        with self.assertRaises(RepositoryRocketException):
            r1 = self.__repo.get_rocket()

    def test_delete_rocket(self):
        self.__repo.delete_rocket()
        with self.assertRaises(RepositoryRocketException):
            self.__repo.delete_rocket()

        self.__repo.add_rocket(Rocket(4, 10))
        rocket = self.__repo.get_rocket()
        self.assertEqual(Rocket(4, 10), rocket)
        self.__repo.delete_rocket()
        with self.assertRaises(RepositoryRocketException):
            self.__repo.delete_rocket()

class TestRepositorySolarSystemFile(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.__repo_solar_system = RepositoryFileSolarSystem("tests/Test_Solar_System.txt", "tests/Test_Planetary_Data.txt")
    def tearDown(self):
        print("tearDown")

    def test_load_planets_from_file(self):
        self.__repo_solar_system.load_planets_from_file()
        planets = self.__repo_solar_system.get_all_planets_extended()
        self.assertEqual(planets[0].period, 88)
        self.assertEqual(planets[0].orbital_radius, 0.39)
        self.assertEqual(planets[1].period, 225)
        self.assertEqual(planets[1].orbital_radius, 0.72)
        self.assertEqual(planets[2].period, 365)
        self.assertEqual(planets[2].orbital_radius, 1)

if __name__ == '__main__':
    unittest.main()