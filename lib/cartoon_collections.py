
dwarves = ["Doc", "Dopey", "Bashful", "Grumpy", "Snoozy", "Sleepy", "Happy"]

#def roll_call_dwarves(dwarves):
    #for i in range(len(dwarves)):
        #dwarves[i] = f"\n{i+1}. {dwarves[i]}"
    #print(('').join(dwarves))

def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def summon_captain_planet(planeteer_calls):
    for i in range(len(planeteer_calls)):
        planeteer_calls[i] = f"{planeteer_calls[i]}!".title()
    return planeteer_calls

print(summon_captain_planet(planeteer_calls))

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    cheeses = ["cheddar", "gouda", "camembert"]
    for string in strings:
        if string in cheeses:
            return string
    return None
