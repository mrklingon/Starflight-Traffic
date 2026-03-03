# Starflight-Traffic
<img width="861" height="646" alt="image" src="https://github.com/user-attachments/assets/cd70385d-2e01-4bfa-9f54-1d07286f8965" />
<img width="861" height="646" alt="image" src="https://github.com/user-attachments/assets/055bff04-0413-45e6-aae7-3b6d04034b54" />

***Having fun running display of Starship traffic across ten star systems*
**

[How to use.](#how-to-use)

My first PyBasic-->CircuitPython project, [Project Starflight](https://github.com/mrklingon/Project-Starflight) involved defining a set of ten star systems linked with three "tramline" exits to other starsystems. The goal of the project was two-fold

1. See if I *could* write in BASIC after decades, using PyBasic and
2. To try to use an LLM to translate it into Python, Python that I could adapt to work as CircuitPython

This worked pretty well, and I admit the bot did a decent job documenting my undocumented PyBasic code.

Following that I wanted to try something different.

I'm a big fan of the Star Wars ride at Disney, "Star Tours," both for the fun flight simulator effect AND the whole spaceport ambiance of the ride queue, including (see above) the Arrival and Departure displays (ala flight info in an airport). I thought it would be fun to create a running display of spaceship arrivals and departures in a Star Wars mode.

So beginning with my Starflight BASIC code, I reused the data structures defining ships, stars, planets and hyperspace exits. I used fantasynamegenerators.com to create "Star Wars"-esque ships, stars and planets, and now refer to the exits as "hyperspace lanes" (as is the current SW parlance :). 

The program then generates the set of exits from each star, and in a new array, assigns each ship to one of the 10 star systems.

Next, in a continuous loop, a ship is chosen, and (if not currently in motion) it is assigned a new destination from one of the exits available. The location array for that ship now has the number of the destination star - to indicate it is _moving_ there the number is recorded as negative (i.e. if going to star #3, "-3") is logged.

When being  set in motion TO a star the program prints

```
Departing from [planet name] vessel [ship name] 
heading for [destination]
``` 
*note: each star has a "planet" associated with it. So departures originate from the planet **to** a star*

if the ships location is a negative number, then the program prints:
```
[Ship name] arrived!!
[Ship name] arriving at [destination star]
```
Then changes the location value to a positive number to indicate it has arrived, so the next time the ship is chosen by the main loop, it will start from their.

Output looks like:

```
Do you need instructions? (y/n)

? y
This system will display current starship traffic
across a span of ten interconnected systems.

Ships travel from system to system via hyperspace lanes
and you will see arrivals and departures.


Departing from Uverrooith Vessel: Hellhound
heading for Krithuc.
Departing from Codachaa Vessel: BS Khan
heading for Pluedurs.
Hellhound arrived!!
Hellhound arriving at Krithuc
Departing from Guvor Vessel: Omen
heading for Krithuc.
Departing from Yorar Vessel: Hellhound
heading for Olutsos.
Departing from Vuthadoh Vessel: SC Providence
heading for Pluedurs.
Hellhound arrived!!
Hellhound arriving at Olutsos
SC Providence arrived!!
SC Providence arriving at Pluedurs
Departing from Uusnes Vessel: BS Nuria
heading for Sleak.
Departing from Lesti Vessel: Saber
heading for Sleak.
Saber arrived!!
Saber arriving at Sleak
```


<a name="how-to-use">  </a>
## How to Use:
There are three sets of code here: a PyBasic version, a CircuitPython app for FruitJam and a CircuitPython version for the NeoTrinkey.

### PyBasic

* StarTraffic.bas - copy this to the examples/ directory under apps/PyBasic/ on a FruitJam. Then load and run. [_note:_ you can run this under any PyBasic install]


### FruitJam App

Copy these files into a directory on your FruitJam "apps/StarTraffic"

* code.py
* metadata.json
* startraffic.bmp  (icon)
* startraffic.py

Then you can navigate on the FruitJam to the icon, click and let the program start.

### NeoTrinkey

Copy these files to your NeoTrinkey:

* neoStarTraffic.py (rename as code.py)
* ncount.py support file for neostartraffic.py [provides blinky lights]
* prt.py support file for neostartraffic.py [allows redirect of output as if typed]

Change the variable REPL to **True** or **False** depending on whether you are running the program in a REPL like Mu or Thonny. If not the output 
will be directed via HID as if typed. If REPL=**False** the program will wait, blinking red and green till you touch one of the touch pads. This 
gives you a chance to move the cursor on the computer to where you want the output to show up (eg. in an editor window). 

Touching the touch pads when the program is running will terminate it.
 
