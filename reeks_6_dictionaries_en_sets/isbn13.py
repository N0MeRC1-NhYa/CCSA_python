def code_check(code):
    if len(code) != 13:
        return False
    if code[:3] not in ["978", "979"]:
        return False
    odd_sum = 0
    even_sum = 0
    for i in range(len(code) - 1):
        if i % 2 == 0:
            odd_sum+= int(code[i])
        else:
            even_sum += int(code[i])
    return (10 - (odd_sum + 3 * even_sum) % 10 ) % 10 == int(code[-1])


def overzicht(codes):
    land = {"0":"Engelstalige landen",
            "1":"Engelstalige landen",
            "2":"Franstalige landen",
            "3":"Duitstalige landen",
            "4":"Japan", 
            "5":"Russischtalige landen",
            "7":"China",
            "8":"Overige landen",
            "6":"Overige landen",
            "9":"Overige landen"
            }
    land_cnt = dict.fromkeys(land.values(), 0)
    land_cnt["Fouten"] = 0
    for c in codes:
        if code_check(c):
            land_cnt[land.get(c[3])] += 1
        else:
            land_cnt["Fouten"] += 1

    for k in land_cnt.keys():
        print(f"{k}: {land_cnt.get(k)}")
