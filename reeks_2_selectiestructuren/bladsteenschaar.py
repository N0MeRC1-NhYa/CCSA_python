rules = {
    "blad":["steen", "Spock"], 
    "steen":["schaar", "hagedis"],
    "hagedis":["blad", "Spock"], 
    "Spock":["schaar", "steen"], 
    "schaar":["blad", "hagedis"]
         }
p1 = input()
p2 = input()
if (p1 == p2):
    print("gelijkspel")
elif (p2 in rules[p1]):
    print("speler1 wint")
else:
    print("speler2 wint")