import random
import time
from prt import *
from ncount import *

import touchio

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)
REPL = True

compthink()

DARK = True #prevent blinkies during run
# Initialize data
FLEET = ["Adventurer", "Omen", "The Jellyfish", "Saber", "Hellhound",
         "SC Providence", "CS Shade", "BS Khan", "SS Andromeda", "BS Nuria"]

PLANET = ["Vuthadoh", "Lesti", "Uverrooith", "Veohpo", "Codachaa",
          "Yorar", "Guvor", "Bincussial", "Uusnes", "Trah"]

STAR = ["Deey", "Uguaks", "Eceub", "Vret", "Sleak",
        "Krithuc", "Olutsos", "Huqein", "Pluedurs", "Isliursil"]

# Initialize ship locations and hyperspace lanes
sloc = [0] * 11 # ship locations (1-indexed, so index 0 unused)
ext = [[0] * 3 for _ in range(11)]  # hyperspace lane connections

def initialize():
    """Set up initial ship locations and hyperspace lane connections"""
    for i in range(10):
        sloc[i] = random.randint(1, 10)
    # Generate hyperspace lane connections
    for i in range(10):
        for t in range(3):
            e = random.randrange(10)
            ext[i][t] = e

def print_instructions():
    """Display game instructions"""
    prt("This system will display current starship traffic",REPL)
    prt("across a span of ten interconnected systems.",REPL)
    prt("",REPL)
    prt("Ships travel from system to system via hyperspace lanes",REPL)
    prt("and you will see arrivals and departures.",REPL)
    prt("",REPL)
    delay()

def delay():
    """Simulate a delay (replaces the BASIC delay loop)"""
    time.sleep(3)
if REPL == False:
    Waiter = True
    while Waiter:
        docolor(red)
        docolor(green)
        Val = 0

        if touch1.value:
            Val = Val + 1


        if touch2.value:
            Val = Val + 2
        if Val > 0:
            Waiter= False

"""Main traffic control loop"""
initialize()
prt("Project Starflight Traffic Control",REPL)
prt("",REPL)

# Ask for
if REPL:
    ans = input("Do you need instructions? (y/n): ").lower()
    if ans == 'y':
        print_instructions()

else:
    print_instructions()

prt("",REPL)

    # Main transit loop
Flying=True
while Flying:
    Val = 0

    if touch1.value:
        Val = Val + 1


    if touch2.value:
        Val = Val + 2
    if Val > 0:
        Flying= False

    # Pick a random ship
    ship = random.randint(0, 9)
    if DARK == False:
        compthink()
    # Check if ship has arrived
    if sloc[ship] < 0:
        prt(f"{FLEET[ship]} arrived!!",REPL)
        sloc[ship] = abs(sloc[ship])
        # Display arrival
        prt(f"{FLEET[ship]} arriving at {STAR[abs(sloc[ship]) - 1]}",REPL)
        sloc[ship] = abs(sloc[ship])
        delay()

    else:
        # Ship is departing
        frm = sloc[ship]

        # Pick a destination from hyperspace lanes
        p = random.randint(0, 2)
        dest = ext[sloc[ship]][p]

        # Display departure
        prt(f"Departing from {PLANET[frm - 1]} Vessel: {FLEET[ship]}",REPL)
        prt(f"heading for {STAR[dest - 1]}.",REPL)

        # Mark ship as in transit (negative value)
        sloc[ship] = -dest
        delay()


        prt("",REPL)