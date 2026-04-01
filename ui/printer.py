class Printer_Ui_Exception(Exception):
    def __init__(self, message):
        self.message = message

class Printer:
    def __init__(self, lang):
        self.__lang = lang

    def print_language_menu(self):
        print("Please choose the language you wish to use: ")
        print("Vă rugăm alegeți limba pe care doriți să o utilizați: ")
        print("1. English")
        print("2. Română")

    def print_menu(self):
        if self.__lang == "1":
            print("Menu :)")
            print("1. Print all the planets stored in the application")
            print("2. Calculate the escape velocity for each planet stored in a given file")
            print("3. Calculate the time and distance needed to reach escape velocity for a rocket stored in a given file")
            print("4. Simulate a journey between two planets")
            print("5. Display the angular position for a chosen day")
            print("6. Find the optimal transfer window for two planets")
            print("7. Find the optimal transfer window for two planets (the other planets are not stationary)")
            print("8. Change the language")
            print("9. Exit the application")

        else:
            print("Meniu :)")
            print("1. Afișează toate planetele stocate in aplicație")
            print("2. Calculează viteza de evadare pentru fiecare planetă stocată într-un fișier dat")
            print("3. Calculează timpul și distanta necesara pentru a atinge viteza de evadare pentru o rachetă stocată într-un fișier dat")
            print("4. Simulează o călătorie între două planete")
            print("5. Afișează poziția unghiulară pentru ziua aleasă")
            print("6. Găsește fereastra optimă de transfer pentru două planete")
            print("7. Găsește fereastra de transfer optimă pentru două planete (celelalte planete nu sunt staționare)")
            print("8. Schimbă limba")
            print("9. Ieșire din aplicație")

    def print_default_file_menu(self):
        if self.__lang == "1":
            print("1. Type the adress of the file you wish to use")
            print("2. Use the default file")

        else:
            print("1. Tastați adresa fișierului pe care doriți să îl utilizați")
            print("2. Utilizați un fișierul default")

    def print_loop_menu(self):
        if self.__lang == "1":
            print("1. Try again")
            print("2. Exit")
        else:
            print("1. Mai incearca")
            print("2. Iesire")

    def print_select_planet_file_text(self):
        if self.__lang == "1":
            print("Select an option for the file that contains all the planets stored in the system:")
        else:
            print("Selectati o optiune pentru fisierul care contine toate planetele stocate in sistem:")

    def print_select_rocket_file_text(self):
        if self.__lang == "1":
            print("Select an option for the file that contains the rocket stored in the system:")
        else:
            print("Selectati o optiune pentru fisierul care contine racheta stocata in sistem:")

    def print_select_solar_system_file_text(self):
        if self.__lang == "1":
            print("Select an option for the file that contains the solar system data stored in the system:")
        else:
            print("Selectati o optiune pentru fisierul care contine toate datele despre sistemul solar in sistem:")

    def print_file_menu(self):
        self.print_default_file_menu()
        option = input(">>> ")
        match option:
            case "1":
                if self.__lang == "1":
                    print(
                        "Type the full path of the file you wish to use, with the prefix ../data/\neg: ../data/Planetary_Data.txt")
                else:
                    print(
                        "Tastați calea completa a fișierului pe care doriți să îl utilizați, cu prefixul ../data/\nex: ../data/Planetary_Data.txt")

                filename = input(">>> ")
                if filename not in ["../data/Planetary_Data.txt"]:
                    if self.__lang == "1":
                        raise Printer_Ui_Exception(
                            "Invalid file name. Please enter a valid file name, or use the default file.")
                    else:
                        raise Printer_Ui_Exception(
                            "Numele fișierului este invalid. Vă rugăm introduceți un fișier valid, sau folosiți fișierul default.")
                else:
                    return filename
            case "2":
                return "../data/Planetary_Data.txt"
            case _:
                if self.__lang == "1":
                    text = "Invalid file name. Please enter a valid file name."
                else:
                    text = "Nume de fisier invalid. Va rugam introduceti un nume valid"
                raise Printer_Ui_Exception(text)

    def print_file_menu_rocket(self):
        self.print_default_file_menu()
        option = input(">>> ")
        match option:
            case "1":
                if self.__lang == "1":
                    print(
                        "Type the full path of the file you wish to use, with the prefix ../data/\neg: ../data/Rocket_Data.txt")
                else:
                    print(
                        "Tastați calea completa a fișierului pe care doriți să îl utilizați, cu prefixul ../data/\nex: ../data/Rocket_Data.txt")

                filename = input(">>> ")
                if filename not in ["../data/Rocket_Data.txt"]:
                    if self.__lang == "1":
                        raise Printer_Ui_Exception(
                            "Invalid file name. Please enter a valid file name, or use the default file.")
                    else:
                        raise Printer_Ui_Exception(
                            "Numele fișierului este invalid. Vă rugăm introduceți un fișier valid, sau folosiți fișierul default.")
                else:
                    return filename
            case "2":
                return "../data/Rocket_Data.txt"
            case _:
                if self.__lang == "1":
                    text = "Invalid file name. Please enter a valid file name."
                else:
                    text = "Nume de fisier invalid. Va rugam introduceti un nume valid"
                raise Printer_Ui_Exception(text)

    def print_file_menu_solar_system(self):
        self.print_default_file_menu()
        option = input(">>> ")
        match option:
            case "1":
                if self.__lang == "1":
                    print(
                        "Type the full path of the file you wish to use, with the prefix ../data/\neg: ../data/Solar_System_Data.txt")
                else:
                    print(
                        "Tastați calea completa a fișierului pe care doriți să îl utilizați, cu prefixul ../data/\nex: ../data/Solar_System_Data.txt")

                filename = input(">>> ")
                if filename not in ["../data/Solar_System_Data.txt"]:
                    if self.__lang == "1":
                        raise Printer_Ui_Exception(
                            "Invalid file name. Please enter a valid file name, or use the default file.")
                    else:
                        raise Printer_Ui_Exception(
                            "Numele fișierului este invalid. Vă rugăm introduceți un fișier valid, sau folosiți fișierul default.")
                else:
                    return filename
            case "2":
                return "../data/Solar_System_Data.txt"
            case _:
                if self.__lang == "1":
                    text = "Invalid file name. Please enter a valid file name."
                else:
                    text = "Nume de fisier invalid. Va rugam introduceti un nume valid"
                raise Printer_Ui_Exception(text)

    def stage_5_6_printing_data_optimal_window_data(self, starting_planet, destination_planet, days, aligned, sp_degrees, dp_degrees):
        if days == -1:
            if self.__lang == "1":
                print("Unfortunately, there won't be any optimal transfer window in the next 10 years since the start of the simulation")
            else:
                print("Din păcate, nu va exista nicio fereastră de transfer optimă în următorii 10 ani de la începutul simulării")
            return

        else:
            if self.__lang == "1":
                print(f"We found a valid tranfer window for the journey between {starting_planet.name} and {destination_planet.name}!")
            else:
                print(f"Am gasit o fereastra validă de transfer dintre {starting_planet.name} and {destination_planet.name}!")

            if aligned:
                if self.__lang == "1":
                    print(f"The transfer window is an optimal one, since {starting_planet.name} and {destination_planet.name} are aligned at {sp_degrees} degrees.")
                else:
                    print(f"Fereastra de transfer este una optimă, deoarece {starting_planet.name} și {destination_planet.name} sunt aliniate la {sp_degrees} grade.")

            else:
                if self.__lang == "1":
                    print(f"The transfer window is not an optimal one, since {starting_planet.name} and {destination_planet.name} are not aligned.")
                    print(f"{starting_planet.name}'s angular position is at {sp_degrees} degrees.")
                    print(f"{destination_planet.name}'s angular position is at {dp_degrees} degrees.")

                else:
                    print(f"Fereastra de transfer nu este una optimă, deoarece {starting_planet.name} și {destination_planet.name} nu sunt aliniate.")
                    print(f"Poziția unghiulară a lui {starting_planet.name} este la {sp_degrees} grade.")
                    print(f"Poziția unghiulară a {destination_planet.name} este de {dp_degrees} grade.")

    def stage_3_5_6_ui_printing_data(self, time, distance, cruising_distance,
                                     cruising_time, total_cruising_time):
        if self.__lang == "1":
            print(f"Time needed to reach the cruising velocity: {round(time)} s")
        else:
            print(f"Timpul necesar pentru a atinge viteza de croaziera: {round(time)} s")

        if self.__lang == "1":
            print(f"Distance needed to reach the cruising velocity: {round(distance)} m / {round(distance // 1000)} km")
            print("Searching for the optimal window ...")
        else:
            print(f"Distanta pentru a atinge viteza de croaziera: {round(distance)} m / {round(distance // 1000)} km")
            print("Se cauta fereastra optima de transfer ...")

        if self.__lang == "1":
            print(f"The cruising distance is: {round(cruising_distance, 2)} km ...")
        else:
            print(f"Distanta de croaziera este: {round(cruising_distance, 2)} km ...")

        if self.__lang == "1":
            print(
                f"... Therefore the cruising time is {round(cruising_time, 2)} s / {round(cruising_time // 86400)} days")
        else:
            print(
                f"... Asadar timpul croazierei este {round(cruising_time, 2)} s / {round(cruising_time // 86400)} zile")

        if self.__lang == "1":
            print(f"The total cruising time is {total_cruising_time} s")
        else:
            print(f"Timpul total al croazierei este {total_cruising_time} s")

        days = total_cruising_time // 86400
        remaining = total_cruising_time % 86400

        hours = remaining // 3600
        remaining = remaining % 3600

        minutes = remaining // 60
        seconds = remaining % 60

        if self.__lang == "1":
            print(f"The total cruising time is {round(total_cruising_time)} s")
            print(f"or {round(days)} days, {round(hours)} hours, {round(minutes)} minutes, {round(seconds)} seconds")

        else:
            print(f"Timpul total al croazierei este {round(total_cruising_time)} s")
            print(f"sau {round(days)} zile, {round(hours)} ore, {round(minutes)} minute, {round(seconds)} secunde")
