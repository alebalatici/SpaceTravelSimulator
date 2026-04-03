# SpaceTravelSimulator

# Example Outputs
## Select the language (english, romanian)
```Python
Please choose the language you wish to use: 
Vă rugăm alegeți limba pe care doriți să o utilizați: 
1. English
2. Română
>>>
```
## Menu (English)
```Python
Menu :)
1. Print all the planets stored in the application
2. Calculate the escape velocity for each planet stored in a given file
3. Calculate the time and distance needed to reach escape velocity for a rocket stored in a given file
4. Simulate a journey between two planets
5. Display the angular position for a chosen day
6. Find the optimal transfer window for two planets
7. Find the optimal transfer window for two planets (the other planets are not stationary)
8. Change the language
9. Exit the application
>>>
```
## Menu (Romanian)
```Python
Meniu :)
1. Afișează toate planetele stocate in aplicație
2. Calculează viteza de evadare pentru fiecare planetă stocată într-un fișier dat
3. Calculează timpul și distanta necesara pentru a atinge viteza de evadare pentru o rachetă stocată într-un fișier dat
4. Simulează o călătorie între două planete
5. Afișează poziția unghiulară pentru ziua aleasă
6. Găsește fereastra optimă de transfer pentru două planete
7. Găsește fereastra de transfer optimă pentru două planete (celelalte planete nu sunt staționare)
8. Schimbă limba
9. Ieșire din aplicație
>>>
```
## 1. Print all the planets stored in the application
English
```Python
Name: Mercury    | Diameter: 4900.0     | Mass: 0.06      
Name: Venus      | Diameter: 12100.0    | Mass: 0.82      
Name: Earth      | Diameter: 12800.0    | Mass: 1.0       
Name: Mars       | Diameter: 5800.0     | Mass: 0.11      
Name: Jupiter    | Diameter: 142800.0   | Mass: 318.0     
Name: Saturn     | Diameter: 120000.0   | Mass: 95.0      
Name: Uranus     | Diameter: 52400.0    | Mass: 15.0      
Name: Neptune    | Diameter: 48400.0    | Mass: 17.0      
Name: Pluto      | Diameter: 2450.0     | Mass: 0.002
```
Romanian
```Python
Nume: Mercury    | Diametru: 4900.0    | Masă: 0.06      
Nume: Venus      | Diametru: 12100.0   | Masă: 0.82      
Nume: Earth      | Diametru: 12800.0   | Masă: 1.0       
Nume: Mars       | Diametru: 5800.0    | Masă: 0.11      
Nume: Jupiter    | Diametru: 142800.0  | Masă: 318.0     
Nume: Saturn     | Diametru: 120000.0  | Masă: 95.0      
Nume: Uranus     | Diametru: 52400.0   | Masă: 15.0      
Nume: Neptune    | Diametru: 48400.0   | Masă: 17.0      
Nume: Pluto      | Diametru: 2450.0    | Masă: 0.002
```
## 2. Calculate the escape velocity for each planet stored in a given file
English
```Python
Planet Name  | Escape Velocity
___________________________________
Mercury      | 4418 m/s
Venus        | 10392 m/s
Earth        | 11158 m/s
Mars         | 5498 m/s
Jupiter      | 59568 m/s
Saturn       | 35517 m/s
Uranus       | 21357 m/s
Neptune      | 23658 m/s
Pluto        | 1141 m/s
___________________________________
```
Romanian
```Python
Nume planetă | Viteză de evadare
___________________________________
Mercury      | 4418 m/s
Venus        | 10392 m/s
Earth        | 11158 m/s
Mars         | 5498 m/s
Jupiter      | 59568 m/s
Saturn       | 35517 m/s
Uranus       | 21357 m/s
Neptune      | 23658 m/s
Pluto        | 1141 m/s
___________________________________
```
## 3. Calculate the time and distance needed to reach escape velocity for a rocket stored
```Python
__________________________________________________________________________________________________________________________________
Planet Name          |    Time to reach escape velocity | Distance to reach escape velocity |            The distance from center
__________________________________________________________________________________________________________________________________
Mercury              |                            110 s |                          243885 m |                            2693885 m
Venus                |                            259 s |                         1349766 m |                            7399766 m
Earth                |                            278 s |                         1556038 m |                            7956038 m
Mars                 |                            137 s |                          377741 m |                            3277741 m
Jupiter              |                           1489 s |                        44353622 m |                          115753622 m
Saturn               |                            887 s |                        15767852 m |                           75767852 m
Uranus               |                            533 s |                         5701513 m |                           31901513 m
Neptune              |                            591 s |                         6995741 m |                           31195741 m
Pluto                |                             28 s |                           16259 m |                            1241259 m
__________________________________________________________________________________________________________________________________
```
## 4. Simulate a journey between two planets
Mars ---> Saturn
```Python
Let the journey begin! Please enter the name of the starting planet: 
>>>mars
Selected planet: Mars | Period: 687 Days | Orbital Radius: 1.52 AU
Please enter the name of the destination planet: 
>>>saturn
Selected planet: Saturn | Period: 10753 Days | Orbital Radius: 9.54 AU
______________________________________________________________________________________________________________________________________________________
Note: We assume that our rocket stops by doing what they did to get going, but in reverse
Mars ---> Saturn
Time needed to reach the cruising velocity: 888 s
Distance needed to reach the cruising velocity: 15767852 m / 15767 km
Searching for the optimal window ...
The cruising distance is: 1199680487.31 km ...
... Therefore the cruising time is 33778031.11 s / 390 days
The total cruising time is 33779806.937513135 s
The total cruising time is 33779807 s
or 390 days, 23 hours, 16 minutes, 47 seconds
______________________________________________________________________________________________________________________________________________________
```
Venus ---> Neptune
```Python
Let the journey begin! Please enter the name of the starting planet: 
>>>venus
Selected planet: Venus | Period: 225 Days | Orbital Radius: 0.72 AU
Please enter the name of the destination planet: 
>>>neptune
Selected planet: Neptune | Period: 60148 Days | Orbital Radius: 30.06 AU
______________________________________________________________________________________________________________________________________________________
Note: We assume that our rocket stops by doing what they did to get going, but in reverse
Venus ---> Neptune
Time needed to reach the cruising velocity: 591 s
Distance needed to reach the cruising velocity: 6995741 m / 6995 km
Searching for the optimal window ...
The cruising distance is: 4389157284.86 km ...
... Therefore the cruising time is 185532193.83 s / 2147 days
The total cruising time is 185533376.6871732 s
The total cruising time is 185533377 s
or 2147 days, 9 hours, 2 minutes, 57 seconds
______________________________________________________________________________________________________________________________________________________
```
## 5. Display the angular position for a chosen number of days that have passed since all the planets were aligned at 0 degrees
English
```Python
Enter the number of days: 200
_____________________________________________
Planet Name          |       Angular Position
_____________________________________________
Mercury              |          98.18 degrees
Venus                |          320.0 degrees
Earth                |         197.26 degrees
Mars                 |          104.8 degrees
Jupiter              |          16.63 degrees
Saturn               |            6.7 degrees
Uranus               |           2.35 degrees
Neptune              |            1.2 degrees
Pluto                |            0.8 degrees
_____________________________________________
```
Romanian
```Python
Introduceti numarul de zile: 120
_____________________________________________
Nume planetă         |     Poziția Unghiulară
_____________________________________________
Mercury              |         130.91 grade
Venus                |          192.0 grade
Earth                |         118.36 grade
Mars                 |          62.88 grade
Jupiter              |           9.98 grade
Saturn               |           4.02 grade
Uranus               |           1.41 grade
Neptune              |           0.72 grade
Pluto                |           0.48 grade
_____________________________________________
```
## 6. Find the optimal transfer window for two planets
Mercury ---> Jupiter
```Python
Let the journey begin! Please enter the name of the starting planet: 
>>>mercury
Selected planet: Mercury | Period: 88 Days | Orbital Radius: 0.39 AU
Please enter the name of the destination planet: 
>>>jupiter
Selected planet: Jupiter | Period: 4329 Days | Orbital Radius: 5.2 AU
______________________________________________________________________________________________________________________________________________________
Note: We assume that our rocket stops by doing what they did to get going, but in reverse
      When referring to "the start of the simulation", we consider the 100 years since the planets were all aligned
Mercury ---> Jupiter
We found a valid tranfer window for the journey between Mercury and Jupiter!
The transfer window is not an optimal one, since Mercury and Jupiter are not aligned.
Mercury's angular position is at 339.54545454545456 degrees.
Jupiter's angular position is at 339.54261954261955 degrees.
Time needed to reach the cruising velocity: 1489 s
Distance needed to reach the cruising velocity: 44353622 m / 44353 km
Searching for the optimal window ...
The cruising distance is: 630784663.52 km ...
... Therefore the cruising time is 12078593.72 s / 139 days
The total cruising time is 12081572.097564142 s
The total cruising time is 12081572 s
or 139 days, 19 hours, 59 minutes, 32 seconds
The angular position of all the planets: 
_____________________________________________
Planet Name          |       Angular Position
_____________________________________________
Mercury              |         339.55 degrees
Venus                |           24.0 degrees
Earth                |          24.66 degrees
Mars                 |         127.34 degrees
Jupiter              |         339.54 degrees
Saturn               |         216.14 degrees
Uranus               |          94.58 degrees
Neptune              |         231.72 degrees
Pluto                |          153.9 degrees
_____________________________________________
The beginning of the transfer window is after 2215 days since the start of the simulation or 38715 since all the planets were aligned.
______________________________________________________________________________________________________________________________________________________
```
Pluto ---> Earth
```Python
Let the journey begin! Please enter the name of the starting planet: 
>>>pluto
Selected planet: Pluto | Period: 90560 Days | Orbital Radius: 39.6 AU
Please enter the name of the destination planet: 
>>>earth
Selected planet: Earth | Period: 365 Days | Orbital Radius: 1.0 AU
______________________________________________________________________________________________________________________________________________________
Note: We assume that our rocket stops by doing what they did to get going, but in reverse
      When referring to "the start of the simulation", we consider the 100 years since the planets were all aligned
Pluto ---> Earth
We found a valid tranfer window for the journey between Pluto and Earth!
The transfer window is not an optimal one, since Pluto and Earth are not aligned.
Pluto's angular position is at 158.79593639575972 degrees.
Earth's angular position is at 158.7945205479452 degrees.
Time needed to reach the cruising velocity: 279 s
Distance needed to reach the cruising velocity: 1556038 m / 1556 km
Searching for the optimal window ...
The cruising distance is: 5771358107.97 km ...
... Therefore the cruising time is 517555637.91 s / 5990 days
The total cruising time is 517556195.7737177 s
The total cruising time is 517556196 s
or 5990 days, 5 hours, 36 minutes, 36 seconds
The angular position of all the planets: 
_____________________________________________
Planet Name          |       Angular Position
_____________________________________________
Mercury              |         335.45 degrees
Venus                |          193.6 degrees
Earth                |         158.79 degrees
Mars                 |           52.4 degrees
Jupiter              |          81.91 degrees
Saturn               |         257.35 degrees
Uranus               |         109.03 degrees
Neptune              |         239.09 degrees
Pluto                |          158.8 degrees
_____________________________________________
The beginning of the transfer window is after 3446 days since the start of the simulation or 39946 since all the planets were aligned.
______________________________________________________________________________________________________________________________________________________
```
## 7. Find the optimal transfer window for two planets (the other planets are not stationary)
Earth ---> Mars
```Python
Let the journey begin! Please enter the name of the starting planet: 
>>>earth
Selected planet: Earth | Period: 365 Days | Orbital Radius: 1.0 AU
Please enter the name of the destination planet: 
>>>mars
Selected planet: Mars | Period: 687 Days | Orbital Radius: 1.52 AU
______________________________________________________________________________________________________________________________________________________
Note: We assume that our rocket stops by doing what they did to get going, but in reverse
      When referring to "the start of the simulation", we consider the 100 years since the planets were all aligned
Earth ---> Mars
We found a valid tranfer window for the journey between Earth and Mars!
The transfer window is not an optimal one, since Earth and Mars are not aligned.
Earth's angular position is at 243.6164383561644 degrees.
Mars's angular position is at 243.66812227074234 degrees.
Time needed to reach the cruising velocity: 279 s
Distance needed to reach the cruising velocity: 1556038 m / 1556 km
Searching for the optimal window ...
The cruising distance is: 74669694.58 km ...
... Therefore the cruising time is 6971443.73 s / 80 days
The total cruising time is 6972001.586476273 s
The total cruising time is 6972002 s
or 80 days, 16 hours, 40 minutes, 2 seconds
The angular position of all the planets: 
_____________________________________________
Planet Name          |       Angular Position
_____________________________________________
Mercury              |         167.73 degrees
Venus                |           19.2 degrees
Earth                |         243.62 degrees
Mars                 |         243.67 degrees
Jupiter              |          358.0 degrees
Saturn               |         223.57 degrees
Uranus               |          97.19 degrees
Neptune              |         233.05 degrees
Pluto                |         154.78 degrees
_____________________________________________
The beginning of the transfer window is after 2437 days since the start of the simulation or 38937 days since all the planets were aligned.
______________________________________________________________________________________________________________________________________________________
```
Mars ---> Earth (in romanian)
```Python
Sa inceapa calatoria! Va rugam introduceti numele planetei de unde incepe calatoria: 
>>>mars
Planeta selectata: Mars | Perioada: 687 Zile| Raza Orbitală: 1.52 AU
Va rugam introduceti numele planetei destinatie: 
>>>earth
Planeta selectata: Earth | Perioada: 365 Zile| Raza Orbitală: 1.0 AU
______________________________________________________________________________________________________________________________________________________
Notă: Presupunem că racheta noastră se oprește făcând ceea ce a făcut pentru a porni, dar în sens invers
      Când ne referim la „începutul simulării”, luăm în considerare cei 100 de ani de când planetele au fost toate aliniate
Mars ---> Earth
Am gasit o fereastra validă de transfer dintre Mars and Earth!
Fereastra de transfer nu este una optimă, deoarece Mars și Earth nu sunt aliniate.
Poziția unghiulară a lui Mars este la 243.66812227074234 grade.
Poziția unghiulară a Earth este de 243.6164383561644 grade.
Timpul necesar pentru a atinge viteza de croaziera: 279 s
Distanta pentru a atinge viteza de croaziera: 1556038 m / 1556 km
Se cauta fereastra optima de transfer ...
Distanta de croaziera este: 74669694.58 km ...
... Asadar timpul croazierei este 6971443.73 s / 80 zile
Timpul total al croazierei este 6972001.586476273 s
Timpul total al croazierei este 6972002 s
sau 80 zile, 16 ore, 40 minute, 2 secunde
Pozitia unghiulara pentru toate planetele: 
_____________________________________________
Nume planetă         |     Poziția Unghiulară
_____________________________________________
Mercury              |         167.73 grade
Venus                |           19.2 grade
Earth                |         243.62 grade
Mars                 |         243.67 grade
Jupiter              |          358.0 grade
Saturn               |         223.57 grade
Uranus               |          97.19 grade
Neptune              |         233.05 grade
Pluto                |         154.78 grade
_____________________________________________
Începutul ferestrei de transfer este după 2437 zile de la începutul simulării sau 38937 zile de când toate planetele au fost aliniate.
______________________________________________________________________________________________________________________________________________________
```





