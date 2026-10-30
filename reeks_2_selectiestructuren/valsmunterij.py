heaps = {
    "rechts" : {
        "rechts" : 1,
        "links": 2,
        "evenwicht" : 3
    },
    "links" : {
        "rechts" : 4,
        "links": 5,
        "evenwicht" : 6
    },
    "evenwicht" : {
        "rechts" : 7,
        "links": 8,
        "evenwicht" : 9
    } 
}
print(f"muntstuk #{heaps[input()][input()]} is vervalst")