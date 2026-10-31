us_bigmac = 4.07

def waardering(price, index):
    bigmac_index = price / us_bigmac
    dif_perc = (bigmac_index - index) / index * 100
    if dif_perc <= -25:
        return "sterk ondergewaardeerd"
    elif dif_perc <= -5:
        return "ondergewaardeerd"
    elif dif_perc <= 5:
        return "ongeveer gelijk"
    elif dif_perc <= 25:
        return "overgewaardeerd"
    return "sterk overgewaardeerd"

def wisselkoersanalyse(line, index):
    return f"De {" ".join(line.split(" ")[1:])} is {waardering(float(line.split(" ")[0]), index)} ten opzichte van de dollar."