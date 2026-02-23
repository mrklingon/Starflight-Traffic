import random
import time

# Initialize data
FLEET = ["Adventurer", "Omen", "The Jellyfish", "Saber", "Hellhound", 
         "SC Providence", "CS Shade", "BS Khan", "SS Andromeda", "BS Nuria"]

PLANET = ["Vuthadoh", "Lesti", "Uverrooith", "Veohpo", "Codachaa", 
          "Yorar", "Guvor", "Bincussial", "Uusnes", "Trah"]

STAR = ["Deey", "Uguaks", "Eceub", "Vret", "Sleak", 
        "Krithuc", "Olutsos", "Huqein", "Pluedurs", "Isliursil"]

# Initialize ship locations and hyperspace lanes
sloc = [0] * 10  # ship locations (1-indexed, so index 0 unused)
ext = [[0] * 3 for _ in range(10)]  # hyperspace lane connections

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
    print("This system will display current starship traffic")
    print("across a span of ten interconnected systems.")
    print()
    print("Ships travel from system to system via hyperspace lanes")
    print("and you will see arrivals and departures.")
    print()
    delay()

def delay():
    """Simulate a delay (replaces the BASIC delay loop)"""
    time.sleep(3)


"""Main traffic control loop"""
initialize()
print("Project Starflight Traffic Control")
print()
    
# Ask for instructions
ans = input("Do you need instructions? (y/n): ").lower()
if ans == 'y':
    print_instructions()
    
print()
    
    # Main transit loop
while True:
    # Pick a random ship
    ship = random.randint(0, 9)
    # Check if ship has arrived
    if sloc[ship] < 0:
        print(f"{FLEET[ship]} arrived!!")
        sloc[ship] = abs(sloc[ship])
        # Display arrival
        print(f"{FLEET[ship]} arriving at {STAR[abs(sloc[ship]) - 1]}")
        sloc[ship] = abs(sloc[ship])
        delay()

    else:
        # Ship is departing
        frm = sloc[ship]
            
        # Pick a destination from hyperspace lanes
        p = random.randint(0, 2)
        dest = ext[sloc[ship]][p]
            
        # Display departure
        print(f"Departing from {PLANET[frm - 1]} Vessel: {FLEET[ship]}")
        print(f"heading for {STAR[dest - 1]}.")
            
        # Mark ship as in transit (negative value)
        sloc[ship] = -dest
        delay()
            
        
        print()
