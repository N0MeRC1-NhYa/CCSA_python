side = input()
val = input()
ans = input()

#print(side, val, ans, sep=", ")

if (side == "waarde"):
    if (int(val) % 2 == 0 and ans == "ja"):
        print(f"Juist: kaarten met {side} {val} moeten gedraaid worden.")
    elif (int(val) % 2 != 0 and ans == "nee"):
        print(f"Juist: kaarten met {side} {val} moeten niet gedraaid worden.")
    elif (int(val) % 2 == 0 and ans == "nee"):
        print(f"Fout: kaarten met {side} {val} moeten gedraaid worden.")
    else:
        print(f"Fout: kaarten met {side} {val} moeten niet gedraaid worden.")
else:
    #print(side, val, ans, sep=", ")
    if (val != "rood" and ans == "ja"):
        print(f"Juist: kaarten met {side} {val} moeten gedraaid worden.")
    elif (val == "rood" and ans == "nee"):
        print(f"Juist: kaarten met {side} {val} moeten niet gedraaid worden.")
    elif (val != "rood" and ans == "nee"):
        #print(side, val, ans, sep=", ")
        print(f"Fout: kaarten met {side} {val} moeten gedraaid worden.")
    else:
        print(f"Fout: kaarten met {side} {val} moeten niet gedraaid worden.")
