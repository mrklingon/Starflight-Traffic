# Starflight-Traffic
<img width="861" height="646" alt="image" src="https://github.com/user-attachments/assets/cd70385d-2e01-4bfa-9f54-1d07286f8965" />
<img width="861" height="646" alt="image" src="https://github.com/user-attachments/assets/055bff04-0413-45e6-aae7-3b6d04034b54" />

*Running display of Starship traffic across ten star systems*

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
Departing from [star name] vessel [ship name] 
heading for [destination]
``` 


if the ships locaiton is a negative number, then the program prints:
```
[Ship name] arrived!!
[Ship name] arriving at [destination]
```
